import tkinter as tk
from tkinter import *
from tkinter import ttk
from saveSettings import saveSettings
from GettingInfoFromAPI import *
import logging
from CollectingAndCreatingData import CollectData

#function that creates GUI
def GUI():

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', filename='LolAPI.log', encoding='utf-8',
                        level=logging.DEBUG, filemode='w')

    matchID = ""
    try:
        with open('settings.json') as json_data:
            settings = json.load(json_data)
            server = settings['SERVER']
            api = settings['API']
    except FileNotFoundError:
        api = ""
        server = "EUNE"
        logger.info("Plik settings.json nie jest utworzony - tworze plik setting.json")
        messagebox.showinfo('Możliwy brakujący plik', 'Nie można otworzyć plik settings.json')

    def updateMatchID():
        nonlocal matchID
        matchID = matchID_entry.get()

    m = tk.Tk()
    m.title("RIOT API Settings")

    # Używamy grid zamiast pack
    Label(m, text='SERVER').grid(row=1, column=0, pady=5, padx=5)
    Label(m, text='Match ID').grid(row=2, column=0, pady=5, padx=5)
    Label(m, text='Team 1').grid(row=3, column=0, pady=5, padx=5)
    Label(m, text='Team 2').grid(row=4, column=0, pady=5, padx=5)
    Label(m, text='Wynik (format np 0:0)').grid(row=5, column=0, pady=5, padx=5)
    Label(m, text='API_KEY').grid(row=6, column=0, pady=5, padx=5)

    server_entry = ttk.Combobox(m, values=["EUNE", "EUW"])
    server_entry.grid(row=1, column=1, pady=5, padx=5)
    if server == "EUN1_":
        server_entry.set("EUNE")
    elif server == "EUW1_":
        server_entry.set("EUW")

    matchID_entry = tk.Entry(m)
    matchID_entry.grid(row=2, column=1, pady=5, padx=5)

    team1_entry = tk.Entry(m)
    team1_entry.grid(row=3, column=1, pady=5, padx=5)
    team2_entry = tk.Entry(m)
    team2_entry.grid(row=4, column=1, pady=5, padx=5)
    result_entry = tk.Entry(m)
    result_entry.grid(row=5, column=1, pady=5, padx=5)
    api_key_entry = tk.Entry(m)
    api_key_entry.grid(row=6, column=1, pady=5, padx=5)

    if api != "":
        api_key_entry.insert(api)

    save_api = tk.Button(
        m,
        text='Save',
        command=lambda: [saveSettings(server_entry.get(),api_key_entry.get()), updateMatchID(), CollectData(matchID,team1_entry.get(),team2_entry.get(),result_entry.get()), m.destroy()]#after press button call saveSettings function in file saveSettings
    )
    save_api.grid(row=7, column=0, columnspan=2, pady=10)

    logger.info("Poprawnie udało się zapisać dane do pliku settings.json")

    m.mainloop()


if "__main__" == __name__:
    GUI()