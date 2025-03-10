from GettingInfoFromAPI import GettingInfoFromID
from matchHistory import TimeLine
from GraphCreator import GraphCreate
from DmgGraphCreator import dmgGraph
from FinallGraphCreator import PostGameCreator
from HeadToHead import HeadToHeadGraph
import logging
import sys

def CollectData(matchID,team1,team2,wynik):
    try:
        RedGold,BlueGold,KDA_red,KDA_blue,DamageRed,DamageBlue,Champions,statsFinall = GettingInfoFromID(matchID)
        logging.info("Poprawne pobranie Golda i KDA drużyn")
    except Exception:
        logging.error("Nie udalo sie pobrac Golda i KDA dryżyn - Kod wyjścia 120")
        sys.exit(120)

    try:
        FinallGoldBlue, FinallGoldRed, GoldPerMinutBlue, GoldPerMinutRed, Minuts, FeatOfStrength, DragonBlue, DragonRed, BlueStructures, RedStructures, csW14, result_kda = TimeLine(matchID)
        logging.info("Poprawnie udało się pobrać informacje historyczne")
    except Exception:
        logging.error("Nie udało się pobrać informacji historycznych - kod wyjścia 130")
        sys.exit(130)
    try:
        GraphCreate(Minuts,GoldPerMinutBlue,GoldPerMinutRed)
        logging.info("Udało się wygenerować gold diff graf")
    except Exception:
        logging.error("Nie udalo sie wygenerować gold diff graf - kod wyjścia 140")
        sys.exit(140)

    try:
        dmgGraph(DamageBlue,DamageRed,Champions)
        logging.info("Udało się wygenerować dmg graf")
    except Exception:
        logging.error("Nie udalo sie wygenerować dmg graf - kod wyjścia 150")
        sys.exit(150)

    try:
        PostGameCreator(RedGold,BlueGold,KDA_red,KDA_blue,FeatOfStrength, DragonBlue, DragonRed, BlueStructures, RedStructures, csW14, team1, team2 ,wynik)
        logging.info("Udało się wygenerować info grafikę")
    except Exception:
        logging.error("Nie udalo sie wygenerować ostatecznej grafiki - kod wyjścia 160")
        sys.exit(160)

    try:
        HeadToHeadGraph(result_kda,GoldPerMinutRed,GoldPerMinutBlue,csW14,Champions,statsFinall,team1, team2 ,wynik)
        logging.info("Udało się wygenerować headTohead grafikę")
        logging.info("Program poprawnie kończy działanie")
        sys.exit(0)
    except Exception:
        logging.error("Nie udalo sie wygenerować grafiki HeadToHead - kod wyjścia 170")
        sys.exit(170)

if "__main__" == __name__:
    matchID = ""
    CollectData(matchID)