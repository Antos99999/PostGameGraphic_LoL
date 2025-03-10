import os
import requests

def ImageDownload(champList):
    DownloadedChamipon = []
    championsPath = 'ChampionsImg/'
    ItemsInPath = os.listdir(championsPath)

    for i in ItemsInPath:

        file = os.path.splitext(i)[0]
        DownloadedChamipon.append(file)

    for i in champList:
        if i in DownloadedChamipon:
            continue
        else:
            url = 'https://ddragon.leagueoflegends.com/cdn/15.3.1/img/champion/'+str(i)+'.png'
            response = requests.get(url)
            with open("ChampionsImg/" + str(i) + ".png", "wb") as file:
                file.write(response.content)
            DownloadedChamipon.append(i)

if "__main__" == __name__:
    champList = []
    ImageDownload(champList)