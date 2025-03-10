from PIL import Image, ImageDraw, ImageFont

def PostGameCreator(RedGold,BlueGold,KDA_red,KDA_blue,FeatOfStrength, DragonBlue, DragonRed, BlueStructures, RedStructures, csW14, team1, team2 ,wynik):
    width, height = 1600,900
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('./Resources/TT Octosquares Trial Bold.ttf', 60)
    fontResult = ImageFont.truetype('./Resources/TT Octosquares Trial Bold.ttf', 90)
    fontSmall = ImageFont.truetype('./Resources/TT Octosquares Trial Bold.ttf', 30)

    Background = Image.open("./Resources/Background.png").convert('RGBA')
    image.paste(Background, (0, 0), Background)

    DMG_Graph = Image.open("./Graphs/finalDmgWithChamp.png").convert('RGBA')
    DMG_Graph = DMG_Graph.resize((900,400))
    image.paste(DMG_Graph, (33, 120), DMG_Graph)

    GOLD_Graph = Image.open("./Graphs/Gold.png").convert('RGBA')
    GOLD_Graph = GOLD_Graph.resize((905,408))
    image.paste(GOLD_Graph, (40, 450), GOLD_Graph)

    if len(team1) == 4:
        draw.text((350,40), str(team1), font=font, align='center', fill='white')
    elif len(team1) == 3:
        draw.text((370,40), str(team1), font=font, align='center', fill='white')

    draw.text((750,10),str(wynik), font=fontResult, align='center', fill='white')

    if len(team2) == 4:
        draw.text((1100,40), str(team2), font=font, align='center', fill='white')
    elif len(team2) == 3:
        draw.text((1150,40), str(team2), font=font, align='center', fill='white')


    draw.text((1000,236), str(KDA_blue), font=fontSmall, align='center', fill='white')
    text_bbox = draw.textbbox((0,0),str(KDA_red),font=font)
    text_width = text_bbox[2] - text_bbox[0]
    if len(str(KDA_red)) == 4:
        text_x_position = 1589 - text_width
    elif len(str(KDA_red)) == 3:
        text_x_position = 1540 - text_width
    draw.text((text_x_position,236),f"{KDA_red:.2f}",font=fontSmall, align='center', fill='white')

    draw.text((1000,324), str(BlueGold), font=fontSmall, align='center', fill='white')
    text_bbox = draw.textbbox((0, 0), str(RedGold), font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_x_position = 1620 - text_width
    draw.text((text_x_position,324),str(RedGold),font=fontSmall, align='center', fill='white')

    draw.text((1000, 613), str(BlueStructures), font=fontSmall, align='center', fill='white')
    text_bbox = draw.textbbox((0, 0), str(RedStructures), font=font)
    text_width = text_bbox[2] - text_bbox[0]
    if RedStructures >= 10:
        text_x_position = 1555 - text_width
    elif RedStructures < 10:
        text_x_position = 1535 - text_width
    draw.text((text_x_position, 613), str(RedStructures), font=fontSmall, align='center', fill='white')

    csW14Blue = 0
    csW14Red = 0
    for i in range(len(csW14)):
        if i < 5:
            csW14Blue += csW14[i]
        else:
            csW14Red += csW14[i]

    csW14Blue = csW14Blue/5
    csW14Red = csW14Red/5
    csW14Blue = round(csW14Blue, 2)
    csW14Red = round(csW14Red, 2)

    #7316716031
    #print(len(str(csW14Blue)), len(str(csW14Red)))

    draw.text((1000, 710), str(csW14Blue), font=fontSmall, align='center', fill='white')
    text_bbox = draw.textbbox((0, 0), str(csW14Red), font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_x_position = 1590 - text_width
    if len(str(csW14Red)) == 4:
        draw.text((text_x_position, 710), str(csW14Red), font=fontSmall, align='center', fill='white')
    elif len(str(csW14Red)) == 5:
        draw.text((text_x_position+25, 710), str(csW14Red), font=fontSmall, align='center', fill='white')
    for dragon in DragonBlue:
        if dragon == "ELDER_DRAGON":
            DragonBlue.remove(dragon)
    for dragon in DragonRed:
        if dragon == "ELDER_DRAGON":
            DragonRed.remove(dragon)

    for i in range(len(DragonBlue)):
        dragonBlue = Image.open('./Resources/' + DragonBlue[i] + '.png').convert('RGBA')
        dragonBlue = dragonBlue.resize((60, 60))
        image.paste(dragonBlue, (985 + 40 * i, 412), dragonBlue)
    for i in range(len(DragonRed)):
        dragonRed = Image.open('./Resources/' + DragonRed[i] + '.png').convert('RGBA')
        dragonRed = dragonRed.resize((60, 60))
        image.paste(dragonRed, (1470 - 40 * i, 412), dragonRed)

    red = []
    blue = []

    try:
        if FeatOfStrength.get('3monstersR') == 'yes':
            red.append('FOS_Obj_R')
    except:
        pass
    try:
        if FeatOfStrength.get('KillsR') == 'yes':
            red.append('FOS_Kill_R')
    except:
        pass
    try:
        if FeatOfStrength.get('FirstTowerR') == 'yes':
            red.append('FOS_Tower_R')
    except:
        pass
    try:
        if FeatOfStrength.get('3monstersB') == 'yes':
            blue.append('FOS_Obj_B')
    except:
        pass
    try:
        if FeatOfStrength.get('KillsB') == 'yes':
            blue.append('FOS_Kill_B')
    except:
        pass
    try:
        if FeatOfStrength.get('FirstTowerB') == 'yes':
            blue.append('FOS_Tower_B')
    except:
        pass

    for i in range(len(blue)):
        FOS_blue = Image.open('./Resources/' + blue[i] + '.png').convert('RGBA')
        FOS_blue = FOS_blue.resize((50, 50))
        image.paste(FOS_blue, (990 + 60 * i, 512), FOS_blue)
    for i in range(len(red)):
        FOS_red = Image.open('./Resources/' + red[i] + '.png').convert('RGBA')
        FOS_red = FOS_red.resize((50, 50))
        image.paste(FOS_red, (1470 - 60 * i, 512), FOS_red)


    #image.show()
    image.save("./Graphs/FinallGraph.png")

    return

if "__main__" == __name__:
    RedGold = 0
    BlueGold = 0
    KDA_red = 0
    KDA_blue = 0
    FeatOfStrength = {}
    DragonBlue = []
    DragonRed = []
    BlueStructures = 0
    RedStructures = 0
    csW14 = 0
    team1 = ""
    team2 = ""
    wynik = ""
    PostGameCreator(RedGold,BlueGold,KDA_red,KDA_blue,FeatOfStrength, DragonBlue, DragonRed, BlueStructures, RedStructures, csW14, team1, team2, wynik)