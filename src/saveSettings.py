import json

def saveSettings(server,api):
    if server == 'EUNE':
        server = "EUN1_"
    elif server == 'EUW':
        server = "EUW1_"
    settings = {
        'SERVER': server,
        'API': api
    }
    with open('settings.json', 'w') as f:
        json.dump(settings, f)