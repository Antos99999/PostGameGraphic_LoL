import time
import requests
import urllib.parse
import json


def AccountsV1(tagLine,gameName):
    Nick = urllib.parse.quote(gameName)
    try:
        accountInfo = requests.get('https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/'+Nick+'/'+tagLine+'?api_key=RGAPI-eaedea2d-4a12-4005-97e5-4466a2397777')
    except:
        time.sleep(121)
        accountInfo = requests.get('https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/'+Nick+'/'+tagLine + '?api_key=' + key)
    return accountInfo.json()

def MatchV5(puuid):
    try:
        metch = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/'+puuid+'/ids?start=0&count=20&api_key=RGAPI-eaedea2d-4a12-4005-97e5-4466a2397777')
    except:
        time.sleep(121)
        metch = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/'+puuid+'/ids?start=0&count=20&api_key=RGAPI-eaedea2d-4a12-4005-97e5-4466a2397777')
    return metch.json()

def MatchInfoV5(matchId):
    try:
        matchInfo = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/'+matchId+'?api_key=RGAPI-eaedea2d-4a12-4005-97e5-4466a2397777')
    except:
        time.sleep(121)
        matchInfo = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/'+matchId+'?api_key=RGAPI-eaedea2d-4a12-4005-97e5-4466a2397777')
    return matchInfo.json()

def MatchTimeLine(matchId):
    try:
        matchTimeLine = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/'+matchId+'/timeline?api_key=RGAPI-eaedea2d-4a12-4005-97e5-4466a2397777')
    except:
        time.sleep(121)
        matchTimeLine = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/' + matchId + '/timeline?api_key=' + key)
    return matchTimeLine.json()