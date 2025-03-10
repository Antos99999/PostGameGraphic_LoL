from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
from ChampionImgDownloader import ImageDownload
import logging
import sys

def dmgGraph(BlueDMG, RedDMG, Champions):

    try:
        ImageDownload(Champions)
        logging.info("Poprawnie udało się pobrać ikony championów")
    except:
        logging.error("Nie udalo sie pobrac ikon championow- Kod wyjścia 151")
        sys.exit(151)

    width, height = 900, 400
    image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('./Resources/TT Octosquares Trial Bold.ttf', 20)
    plt.figure(figsize=(10, 7))

    # Usunięcie zbędnych osi i etykiet
    plt.rcParams['axes.spines.left'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.bottom'] = False

    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=0.4)

    x = BlueDMG + RedDMG

    # Plot 1
    plt.subplot(1, 2, 1)

    x1 = BlueDMG
    y1 = Champions[:5]

    plt.barh(y1, x1, height=0.3, color='goldenrod', align='center')

    plt.gca().invert_yaxis()

    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False, labelright=False, bottom=False,labelbottom=False)
    plt.tick_params(axis='x', which='both', left=False, right=False, labelleft=False, labelright=False, bottom=False,labelbottom=False)

    # Plot 2
    plt.subplot(1, 2, 2)
    x2 = RedDMG
    y2 = Champions[5:]

    plt.barh(y2, x2, height=0.3, color='darkred', align='center') #slategrey

    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()

    plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=False, labelright=False, bottom=False,
                    labelbottom=False)
    plt.tick_params(axis='x', which='both', left=False, right=False, labelleft=False, labelright=False, bottom=False,
                    labelbottom=False)

    #plt.show()
    plt.savefig('Graphs/dmg.png', bbox_inches='tight', facecolor='none', transparent=True)

    for i in range(10):
        if i < 5:
            champIcon = Image.open('./ChampionsImg/'+Champions[i]+'.png').convert('RGBA')
            champIcon = champIcon.resize((60,60))
            image.paste(champIcon,(15,20+67*i),champIcon)
            draw.text((83,45+67*i),str(x[i]),fill='white',font=font)
        else:
            champIcon = Image.open('./ChampionsImg/' + Champions[i] + '.png').convert('RGBA')
            champIcon = champIcon.resize((60, 60))
            image.paste(champIcon, (825, 20+67*(i-5)), champIcon)
            text_bbox = draw.textbbox((0, 0), str(x[i]), font=font)
            text_width = text_bbox[2] - text_bbox[0]  # Szerokość tekstu
            text_x_position = 749 + 70 - text_width  # Dopasowanie do prawej
            draw.text((text_x_position, 45+67* (i-5)), str(x[i]), fill='white', font=font, align ="right")
    DMG_graph = Image.open('./Graphs/dmg.png').convert('RGBA')
    DMG_graph = DMG_graph.resize((750,328))
    image.paste(DMG_graph,(75,0),DMG_graph)
    #image.show()
    image.save("./Graphs/finalDmgWithChamp.png")

if "__main__" == __name__:
    BlueDMG = []
    RedDMG = []
    Champions = []
    dmgGraph(BlueDMG, RedDMG, Champions)