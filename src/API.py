import time
import requests
import urllib.parse
import json



def AccountsV1(tagLine,gameName):
    Nick = urllib.parse.quote(gameName)
    with open('settings.json') as json_data:
        settings = json.load(json_data)
        API = settings['API']
    try:
        accountInfo = requests.get('https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/'+Nick+'/'+tagLine+'?api_key='+API)
    except:
        time.sleep(121)
        accountInfo = requests.get('https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/'+Nick+'/'+tagLine + '?api_key='+API)
    return accountInfo.json()

def MatchV5(puuid):
    with open('settings.json') as json_data:
        settings = json.load(json_data)
        API = settings['API']
    try:
        metch = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/'+puuid+'/ids?start=0&count=20&api_key='+API)
    except:
        time.sleep(121)
        metch = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/'+puuid+'/ids?start=0&count=20&api_key='+API)
    return metch.json()

def MatchInfoV5(matchId):
    with open('settings.json') as json_data:
        settings = json.load(json_data)
        API = settings['API']
    try:
        matchInfo = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/'+matchId+'?api_key='+API)
    except:
        time.sleep(121)
        matchInfo = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/'+matchId+'?api_key='+API)
    return matchInfo.json()

def MatchTimeLine(matchId):
    with open('settings.json') as json_data:
        settings = json.load(json_data)
        API = settings['API']
    try:
        matchTimeLine = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/'+matchId+'/timeline?api_key='+API)
    except:
        time.sleep(121)
        matchTimeLine = requests.get('https://europe.api.riotgames.com/lol/match/v5/matches/' + matchId + '/timeline?api_key='+API)
    return matchTimeLine.json()
