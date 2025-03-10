from API import *
from Classes import *
from tkinter import messagebox
import logging

def GettingInfoFromID(matchID):

    with open('settings.json') as json_data:
        settings = json.load(json_data)
        server = settings['SERVER']

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',filename='LolAPI.log', encoding='utf-8', level=logging.DEBUG, filemode='w')

    matchID = server + str(matchID)

    matchinfo = MatchInfoV5(matchID)

    if 'status' in matchinfo:
        status_code = matchinfo['status']['status_code']
        message = matchinfo['status']['message']
        if status_code != 200:
            messagebox.showerror("Błąd w czytaniu API",f"Wystąpił błąd podczas pobierania API")
            logger.error(f'Błąd w wczytywaniu API o kodzie {status_code} o komunikacie\n {message}\n kod wyjścia 100')
            exit(100)

    if 'httpStatus' in matchinfo:
        status_code = matchinfo['httpStatus']
        message = matchinfo['message']
        if status_code != 200:
            messagebox.showerror("Błąd w czytaniu API", f"Wystąpił błąd podczas pobierania API")
            logger.error(f'Błąd w wczytywaniu API o kodzie {status_code} o komunikacie: {message}\n kod wyjścia 101')
            exit(101)

    logger.info("Poprawnie udało się sczytać dane z gry o ID " + matchID)

    matchinfo = matchinfo["info"]

    logger.info("Poprawnie udało się wyciągnąć dane info")

    RedGold,BlueGold,KDA_red,KDA_blue,DamageRed,DamageBlue,Champions,statsFinall = GettingGoldAndKDA(matchinfo)


    return  RedGold,BlueGold,KDA_red,KDA_blue,DamageRed,DamageBlue,Champions,statsFinall


def GettingGoldAndKDA(matchinfo):
    RedGold = 0
    BlueGold = 0
    AllKillsBlue = 0
    AllDeathsBlue = 0
    AllAssistsBlue = 0
    AllKillsRed = 0
    AllDeathsRed = 0
    AllAssistsRed = 0
    DamageRed = []
    DamageBlue = []
    Champions = []

    k1 = 0
    k2 = 0
    k3 = 0
    k4 = 0
    k5 = 0
    k6 = 0
    k7 = 0
    k8 = 0
    k9 = 0
    k10 = 0
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    d6 = 0
    d7 = 0
    d8 = 0
    d9 = 0
    d10 = 0
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    a7 = 0
    a8 = 0
    a9 = 0
    a10 = 0
    cs1 = 0
    cs2 = 0
    cs3 = 0
    cs4 = 0
    cs5 = 0
    cs6 = 0
    cs7 = 0
    cs8 = 0
    cs9 = 0
    cs10 = 0

    #Ilosc uczestnikow
    participantCount = len(matchinfo['participants'])

    #Przejscie po kazdym uczestniku
    for i in range(participantCount):
        team = matchinfo['participants'][i]['teamId']
        if team == 100:
            BlueGold = matchinfo['participants'][i]['goldEarned'] + BlueGold
            AllKillsBlue = matchinfo['participants'][i]['kills'] + AllKillsBlue
            AllDeathsBlue = matchinfo['participants'][i]['deaths'] + AllDeathsBlue
            AllAssistsBlue = matchinfo['participants'][i]['assists'] + AllAssistsBlue
            DamageBlue.append(matchinfo['participants'][i]['totalDamageDealtToChampions'])
            Champions.append(matchinfo['participants'][i]['championName'])
        elif team == 200:
            RedGold = matchinfo['participants'][i]['goldEarned'] + RedGold
            AllKillsRed = matchinfo['participants'][i]['kills'] + AllKillsRed
            AllDeathsRed = matchinfo['participants'][i]['deaths'] + AllDeathsRed
            AllAssistsRed = matchinfo['participants'][i]['assists'] + AllAssistsRed
            DamageRed.append(matchinfo['participants'][i]['totalDamageDealtToChampions'])
            Champions.append(matchinfo['participants'][i]['championName'])
        if i == 0:
            k1 = matchinfo['participants'][i]['kills']
            a1 = matchinfo['participants'][i]['assists']
            d1 = matchinfo['participants'][i]['deaths']
            cs1 = matchinfo['participants'][i]['neutralMinionsKilled'] + matchinfo['participants'][i]['totalMinionsKilled']
            stats1={
                "kda1": str(k1)+"/"+str(d1)+"/"+str(a1),
                "cs1": cs1,
            }
        elif i == 1:
            k2 = matchinfo['participants'][i]['kills']
            a2 = matchinfo['participants'][i]['assists']
            d2 = matchinfo['participants'][i]['deaths']
            cs2 = matchinfo['participants'][i]['neutralMinionsKilled'] + matchinfo['participants'][i][
                'totalMinionsKilled']
            stats2 = {
                "kda2": str(k2)+"/"+str(d2)+"/"+str(a2),
                "cs2": cs2,
            }
        elif i == 2:
            k3 = matchinfo['participants'][i]['kills']
            a3 = matchinfo['participants'][i]['assists']
            d3 = matchinfo['participants'][i]['deaths']
            cs3 = matchinfo['participants'][i]['neutralMinionsKilled'] + matchinfo['participants'][i][
                'totalMinionsKilled']
            stats3 = {
                "kda3": str(k3)+"/"+str(d3)+"/"+str(a3),
                "cs3": cs3,
            }
        elif i == 3:
            k4 = matchinfo['participants'][i]['kills']
            a4 = matchinfo['participants'][i]['assists']
            d4 = matchinfo['participants'][i]['deaths']
            cs4 = matchinfo['participants'][i]['neutralMinionsKilled'] + matchinfo['participants'][i][
                'totalMinionsKilled']
            stats4 = {
                "kda4": str(k4)+"/"+str(d4)+"/"+str(a4),
                "cs4": cs4,
            }
        elif i == 4:
            k5 = matchinfo['participants'][i]['kills']
            a5 = matchinfo['participants'][i]['assists']
            d5 = matchinfo['participants'][i]['deaths']
            cs5 = matchinfo['participants'][i]['neutralMinionsKilled'] + matchinfo['participants'][i][
                'totalMinionsKilled']
            stats5 = {
                "kda5": str(k5)+"/"+str(d5)+"/"+str(a5),
                "cs5": cs5,
            }
        elif i == 5:
            k6 = matchinfo['participants'][i]['kills']
            a6 = matchinfo['participants'][i]['assists']
            d6 = matchinfo['participants'][i]['deaths']
            cs6 = matchinfo['participants'][i]['neutralMinionsKilled'] + matchinfo['participants'][i][
                'totalMinionsKilled']
            stats6 = {
                "kda6": str(k6)+"/"+str(d6)+"/"+str(a6),
                "cs6": cs6,
            }
        elif i == 6:
            k7 = matchinfo['participants'][i]['kills']
            a7 = matchinfo['participants'][i]['assists']
            d7 = matchinfo['participants'][i]['deaths']
            cs7 = matchinfo['participants'][i]['neutralMinionsKilled'] + matchinfo['participants'][i][
                'totalMinionsKilled']
            stats7 = {
                "kda7": str(k7)+"/"+str(d7)+"/"+str(a7),
                "cs7": cs7,
            }
        elif i == 7:
            k8 = matchinfo['participants'][i]['kills']
            a8 = matchinfo['participants'][i]['assists']
            d8 = matchinfo['participants'][i]['deaths']
            cs8 = matchinfo['participants'][i]['neutralMinionsKilled'] + matchinfo['participants'][i][
                'totalMinionsKilled']
            stats8 = {
                "kda8": str(k8)+"/"+str(d8)+"/"+str(a8),
                "cs8": cs8,
            }
        elif i == 8:
            k9 = matchinfo['participants'][i]['kills']
            a9 = matchinfo['participants'][i]['assists']
            d9 = matchinfo['participants'][i]['deaths']
            cs9 = matchinfo['participants'][i]['neutralMinionsKilled'] + matchinfo['participants'][i][
                'totalMinionsKilled']
            stats9 = {
                "kda9": str(k9)+"/"+str(d9)+"/"+str(a9),
                "cs9": cs9,
            }
        elif i == 9:
            k10 = matchinfo['participants'][i]['kills']
            a10 = matchinfo['participants'][i]['assists']
            d10 = matchinfo['participants'][i]['deaths']
            cs10 = matchinfo['participants'][i]['neutralMinionsKilled'] + matchinfo['participants'][i][
                'totalMinionsKilled']
            stats10 = {
                "kda10": str(k10)+"/"+str(d10)+"/"+str(a10),
                "cs10": cs10,
            }


    statsFinall = {
        "stats1": stats1,
        "stats2": stats2,
        "stats3": stats3,
        "stats4": stats4,
        "stats5": stats5,
        "stats6": stats6,
        "stats7": stats7,
        "stats8": stats8,
        "stats9": stats9,
        "stats10": stats10,
    }

    #Liczenie KDA
    KDA_red = (AllKillsRed+AllAssistsRed) / AllKillsBlue
    KDA_blue = (AllKillsBlue+AllAssistsBlue) / AllKillsRed

    #Zaokraglanie wyniku
    KDA_red = round(KDA_red,2)
    KDA_blue = round(KDA_blue,2)

    Result = {
        'RedGold': RedGold,
        'BlueGold': BlueGold,
        'KDA_red': KDA_red,
        'KDA_blue': KDA_blue,
        'DamageRed': DamageRed,
        'DamageBlue': DamageBlue,
        'Champions': Champions
    }

    #return Result
    return RedGold,BlueGold,KDA_red,KDA_blue,DamageRed,DamageBlue,Champions,statsFinall

if __name__ == '__main__':
    matchID = ""
    GettingInfoFromID(matchID)