from GUI import GUI
import logging
import os
import sys

def main():
    os.makedirs("./ChampionsImg", exist_ok=True)
    os.makedirs("./Graphs", exist_ok=True)

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', filename='LolAPI.log', encoding='utf-8',
                        level=logging.DEBUG, filemode='w')

    GUI() #calling function to create GUI in file GUI

    sys.exit()

if __name__ == '__main__':
    main()
