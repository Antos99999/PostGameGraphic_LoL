import json
import logging
from API import MatchTimeLine


def TimeLine(matchID):

    with open('settings.json') as json_data:
        settings = json.load(json_data)
        server = settings['SERVER']

    csW14 = []
    BlueStructures = 0
    RedStructures = 0
    FinallGoldBlue = 0
    FinallGoldRed = 0
    GoldPerMinutBlue = []
    GoldPerMinutRed = []
    Minuts = []
    FeatOfStrength = " "
    DragonBlue = []
    DragonRed = []

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', filename='LolAPI.log', encoding='utf-8',
                        level=logging.DEBUG, filemode='w')
    logging.getLogger("matplotlib.font_manager").setLevel(logging.WARNING)

    matchID = server + str(matchID)


    timeline = MatchTimeLine(matchID)
    logger.info("Poprawnie udało się wczytać timeline")

    #FinallGold, Minuts, GoldPerMinut, FeatOfStrength, DragonBlue, DragonRed, BlueStructures, RedStructures, csW14

    for user in range(1,11):
        if user <= 5:
            FinallGoldBlue += GettingTimeStamp(timeline, user)[0]
            GoldPerMinutBlue.append(GettingTimeStamp(timeline, user)[2])
            csW14.append(GettingTimeStamp(timeline, user)[8])
            _, Minuts,_,_, DragonBlue, DragonRed, BlueStructures, RedStructures, _ = GettingTimeStamp(timeline, user)
            FeatOfStrength = GettingTimeStamp(timeline, user)[3]
        else:
            csW14.append(GettingTimeStamp(timeline, user)[8])
            FinallGoldRed += GettingTimeStamp(timeline, user)[0]
            GoldPerMinutRed.append(GettingTimeStamp(timeline, user)[2])

    result_kda = GettingKDAin14(timeline)

    return FinallGoldBlue, FinallGoldRed, GoldPerMinutBlue, GoldPerMinutRed, Minuts, FeatOfStrength, DragonBlue, DragonRed, BlueStructures, RedStructures, csW14, result_kda

def GettingKDAin14(timeline):
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


    for frame in range(len(timeline['info']['frames'])):
        for event in range(len(timeline['info']['frames'][frame]['events'])):
            if frame <= 14 and timeline['info']['frames'][frame]["events"][event]["type"] == "CHAMPION_KILL":
                killer = timeline['info']['frames'][frame]["events"][event]["killerId"]
                try:
                    assistantList = timeline['info']['frames'][frame]['events'][event]["assistingParticipantIds"]
                except:
                    assistantList = []
                victim = timeline['info']['frames'][frame]['events'][event]["victimId"]
                if killer == 1:
                    k1 += 1
                elif killer == 2:
                    k2 += 1
                elif killer == 3:
                    k3 += 1
                elif killer == 4:
                    k4 += 1
                elif killer == 5:
                    k5 += 1
                elif killer == 6:
                    k6 += 1
                elif killer == 7:
                    k7 += 1
                elif killer == 8:
                    k8 += 1
                elif killer == 9:
                    k9 += 1
                elif killer == 10:
                    k10 += 1

                if victim == 1:
                    d1 += 1
                elif victim == 2:
                    d2 += 1
                elif victim == 3:
                    d3 += 1
                elif victim == 4:
                    d4 += 1
                elif victim == 5:
                    d5 += 1
                elif victim == 6:
                    d6 += 1
                elif victim == 7:
                    d7 += 1
                elif victim == 8:
                    d8 += 1
                elif victim == 9:
                    d9 += 1
                elif victim == 10:
                    d10 += 1

                for player in assistantList:
                    if player == 1:
                        a1 += 1
                    elif player == 2:
                        a2 += 1
                    elif player == 3:
                        a3 += 1
                    elif player == 4:
                        a4 += 1
                    elif player == 5:
                        a5 += 1
                    elif player == 6:
                        a6 += 1
                    elif player == 7:
                        a7 += 1
                    elif player == 8:
                        a8 += 1
                    elif player == 9:
                        a9 += 1
                    elif player == 10:
                        a10 += 1
    kills = {
        "k1": k1,
        "k2": k2,
        "k3": k3,
        "k4": k4,
        "k5": k5,
        "k6": k6,
        "k7": k7,
        "k8": k8,
        "k9": k9,
        "k10": k10,
    }

    assists = {
        "a1": a1,
        "a2": a2,
        "a3": a3,
        "a4": a4,
        "a5": a5,
        "a6": a6,
        "a7": a7,
        "a8": a8,
        "a9": a9,
        "a10": a10,
    }

    deaths = {
        "d1": d1,
        "d2": d2,
        "d3": d3,
        "d4": d4,
        "d5": d5,
        "d6": d6,
        "d7": d7,
        "d8": d8,
        "d9": d9,
        "d10": d10,
    }

    result_kda = {
        "kda1": str(k1)+"/"+str(d1)+"/"+str(a1),
        "kda2": str(k2)+"/"+str(d2)+"/"+str(a2),
        "kda3": str(k3)+"/"+str(d3)+"/"+str(a3),
        "kda4": str(k4)+"/"+str(d4)+"/"+str(a4),
        "kda5": str(k5)+"/"+str(d5)+"/"+str(a5),
        "kda6": str(k6)+"/"+str(d6)+"/"+str(a6),
        "kda7": str(k7)+"/"+str(d7)+"/"+str(a7),
        "kda8": str(k8)+"/"+str(d8)+"/"+str(a8),
        "kda9": str(k9)+"/"+str(d9)+"/"+str(a9),
        "kda10": str(k10)+"/"+str(d10)+"/"+str(a10),
        "kills": kills,
        "assists": assists,
        "deaths": deaths
    }

    return result_kda


def GettingTimeStamp(timeline,user):

    FeatOfStrength = " "
    redFirstTower = False
    blueFirstTower = False
    red3Kills = False
    blue3Kills = False
    red3Monsters = False
    blue3Monsters = False

    RedKills = 0
    BlueKills = 0
    RedMonsters = 0
    BlueMonsters = 0
    RedVoidsGrubs = 0
    BlueVoidsGrubs = 0
    VoidGrubsCounter = 0
    FirstVoidBrubs = False
    SecondVoidBrubs = False

    FinallGold = 0
    Minuts = []
    GoldPerMinut = []

    DragonBlue = []
    DragonRed = []

    BlueStructures = 0
    RedStructures = 0

    csW14 = 0

    FeatOfStrength = {}

    #100 -> Blue
    #200 -> Red
    for frame in range(len(timeline['info']['frames'])):
        for participantFrames in range(len(timeline['info']['frames'][frame]['participantFrames'])):
            player = timeline['info']['frames'][frame]['participantFrames'][str(participantFrames+1)]['participantId']
            if str(player) == str(user):
                gold = timeline['info']['frames'][frame]['participantFrames'][str(participantFrames + 1)]['totalGold']
                cs = timeline['info']['frames'][frame]['participantFrames'][str(participantFrames + 1)]['minionsKilled']
                jglCS = timeline['info']['frames'][frame]['participantFrames'][str(participantFrames + 1)]['jungleMinionsKilled']
                timestamp = round(int(timeline['info']['frames'][frame]['timestamp']) / 60000)  # co jedną minute
                GoldPerMinut.append(gold)
                Minuts.append(timestamp)
                FinallGold = GoldPerMinut[-1]
                if frame == 14:
                    csW14 = cs + jglCS


        for event in range(len(timeline['info']['frames'][frame]['events'])):

            if redFirstTower == False and blueFirstTower == False:
                if timeline['info']['frames'][frame]["events"][event]["type"] == "BUILDING_KILL" and timeline['info']['frames'][frame]["events"][event]["teamId"] == 200:
                    blueFirstTower = True
                elif timeline['info']['frames'][frame]["events"][event]["type"] == "BUILDING_KILL" and timeline['info']['frames'][frame]["events"][event]["teamId"] == 100:
                    redFirstTower = True

            if red3Kills == False and blue3Kills == False:
                if timeline['info']['frames'][frame]["events"][event]["type"] == "CHAMPION_KILL" and 1 <= int(timeline['info']['frames'][frame]["events"][event]["victimId"]) <= 5:
                    RedKills += 1
                    if RedKills == 3:
                        red3Kills = True
                elif timeline['info']['frames'][frame]["events"][event]["type"] == "CHAMPION_KILL" and 6 <= int(timeline['info']['frames'][frame]["events"][event]["victimId"]) <= 10:
                    BlueKills += 1
                    if BlueKills == 3:
                        blue3Kills = True

            if blue3Monsters == False and red3Monsters == False:
                event_info = timeline['info']['frames'][frame]["events"][event]
                if event_info["type"] == "ELITE_MONSTER_KILL" and event_info["monsterType"] == "HORDE":
                    team_id = event_info["killerTeamId"]
                    if team_id == 100:  # Blue team
                        VoidGrubsCounter += 1
                        BlueVoidsGrubs += 1
                        if VoidGrubsCounter == 3:
                            FirstVoidBrubs = True
                        if VoidGrubsCounter == 6:
                            SecondVoidBrubs = True
                        if FirstVoidBrubs and BlueVoidsGrubs == 3:
                            BlueMonsters += 1
                        if FirstVoidBrubs:
                            FirstVoidBrubs = False
                            BlueVoidsGrubs = 0
                            RedVoidsGrubs = 0
                        if SecondVoidBrubs and BlueVoidsGrubs == 3:
                            BlueMonsters += 1
                        if BlueMonsters == 3:
                            blue3Monsters = True
                    elif team_id == 200:  # Red team
                        VoidGrubsCounter += 1
                        RedVoidsGrubs += 1
                        if VoidGrubsCounter == 3:
                            FirstVoidBrubs = True
                        if VoidGrubsCounter == 6:
                            SecondVoidBrubs = True
                        if FirstVoidBrubs and RedVoidsGrubs == 3:
                            RedMonsters += 1
                        if FirstVoidBrubs:
                            FirstVoidBrubs = False
                            RedVoidsGrubs = 0
                            BlueVoidsGrubs = 0
                        if SecondVoidBrubs and RedVoidsGrubs == 3:
                            RedMonsters += 1
                        if RedMonsters == 3:
                            red3Monsters = True

                if event_info["type"] == "ELITE_MONSTER_KILL" and event_info["monsterType"] == "DRAGON":
                    team_id = event_info["killerTeamId"]
                    if team_id == 100:
                        BlueMonsters += 1
                        if BlueMonsters == 3:
                            blue3Monsters = True
                    if team_id == 200:
                        RedMonsters += 1
                        if RedMonsters == 3:
                            red3Monsters = True

                if event_info["type"] == "ELITE_MONSTER_KILL" and event_info["monsterType"] == "RIFTHERALD":
                    team_id = event_info["killerTeamId"]
                    if team_id == 100:
                        BlueMonsters += 1
                        if BlueMonsters == 3:
                            blue3Monsters = True
                    if team_id == 200:
                        RedMonsters += 1
                        if RedMonsters == 3:
                            red3Monsters = True

            if timeline['info']['frames'][frame]["events"][event]["type"] == "BUILDING_KILL":
                team_id = timeline['info']['frames'][frame]["events"][event]["teamId"]
                if team_id == 200:
                    BlueStructures += 1
                if team_id == 100:
                    RedStructures += 1

            if timeline['info']['frames'][frame]["events"][event]["type"] == "ELITE_MONSTER_KILL" and timeline['info']['frames'][frame]["events"][event]["monsterType"] == "DRAGON":
                team_id = timeline['info']['frames'][frame]["events"][event]["killerTeamId"]
                if team_id == 200:
                    DragonRed.append(timeline['info']['frames'][frame]["events"][event]["monsterSubType"])
                if team_id == 100:
                    DragonBlue.append(timeline['info']['frames'][frame]["events"][event]["monsterSubType"])


    if red3Monsters and red3Kills or red3Monsters and redFirstTower or red3Kills and redFirstTower:
        FeatOfStrength.update({"Who": "red"})
    if red3Monsters:
        FeatOfStrength.update({"3monstersR": "yes"})
    if red3Kills:
        FeatOfStrength.update({"KillsR": "yes"})
    if redFirstTower:
        FeatOfStrength.update({"FirstTowerR": "yes"})

    if blue3Monsters and blue3Kills or blue3Monsters and blueFirstTower or blue3Kills and blueFirstTower:
        FeatOfStrength.update({"Who": "blue"})
    if blue3Monsters:
        FeatOfStrength.update({"3monstersB": "yes"})
    if blue3Kills:
        FeatOfStrength.update({"KillsB": "yes"})
    if blueFirstTower:
        FeatOfStrength.update({"FirstTowerB": "yes"})

    return FinallGold, Minuts, GoldPerMinut, FeatOfStrength, DragonBlue, DragonRed, BlueStructures, RedStructures, csW14


if "__main__" == __name__:
    matchID = ""
    TimeLine(matchID)