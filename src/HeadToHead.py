from PIL import Image, ImageDraw, ImageFont

def HeadToHeadGraph(result_kda,GoldPerMinutRed,GoldPerMinutBlue,csW14,Champions,statsFinall,team1, team2 ,wynik):
    width, height = 1600, 900
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('./Resources/TT Octosquares Trial Bold.ttf', 15)
    fontTeam = ImageFont.truetype('./Resources/TT Octosquares Trial Bold.ttf', 60)
    fontResult = ImageFont.truetype('./Resources/TT Octosquares Trial Bold.ttf', 90)

    Background = Image.open("./Resources/secound_background.png").convert('RGBA')
    image.paste(Background, (0, 0), Background)

    if len(team1) == 4:
        draw.text((350,750), str(team1), font=fontTeam, align='center', fill='white')
    elif len(team1) == 3:
        draw.text((370,750), str(team1), font=fontTeam, align='center', fill='white')

    draw.text((725,730),str(wynik), font=fontResult, align='center', fill='white')

    if len(team2) == 4:
        draw.text((1050,750), str(team2), font=fontTeam, align='center', fill='white')
    elif len(team2) == 3:
        draw.text((1100,750), str(team2), font=fontTeam, align='center', fill='white')

    champIcon = Image.open('./ChampionsImg/' + Champions[0] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (230, 360), champIcon)
    draw.text((265+5, 350), result_kda["kda1"], fill='goldenrod', font=font)
    draw.text((265+5, 367), str(csW14[0]), fill='goldenrod', font=font)
    draw.text((265+5, 384), str(GoldPerMinutBlue[0][13]), fill='goldenrod', font=font)

    champIcon = Image.open('./ChampionsImg/' + Champions[1] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (420, 490), champIcon)
    draw.text((455+5, 480), result_kda["kda2"], fill='goldenrod', font=font)
    draw.text((455+5, 497), str(csW14[1]), fill='goldenrod', font=font)
    draw.text((455+5, 514), str(GoldPerMinutBlue[1][13]), fill='goldenrod', font=font)

    champIcon = Image.open('./ChampionsImg/' + Champions[2] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (350, 440), champIcon)
    draw.text((385+5, 430), result_kda["kda3"], fill='goldenrod', font=font)
    draw.text((385+5, 447), str(csW14[2]), fill='goldenrod', font=font)
    draw.text((385+5, 464), str(GoldPerMinutBlue[2][13]), fill='goldenrod', font=font)

    champIcon = Image.open('./ChampionsImg/' + Champions[3] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (550, 570), champIcon)
    draw.text((585+5, 560), result_kda["kda4"], fill='goldenrod', font=font)
    draw.text((585+5, 577), str(csW14[3]), fill='goldenrod', font=font)
    draw.text((585+5, 594), str(GoldPerMinutBlue[3][13]), fill='goldenrod', font=font)

    champIcon = Image.open('./ChampionsImg/' + Champions[4] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (440, 570), champIcon)
    draw.text((475+5, 560), result_kda["kda5"], fill='goldenrod', font=font)
    draw.text((475+5, 577), str(csW14[4]), fill='goldenrod', font=font)
    draw.text((475+5, 594), str(GoldPerMinutBlue[4][13]), fill='goldenrod', font=font)

    #RED
    champIcon = Image.open('./ChampionsImg/' + Champions[5] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (350, 280), champIcon)
    draw.text((385+5, 270), result_kda["kda6"], fill='slategrey', font=font)
    draw.text((385+5, 287), str(csW14[5]), fill='slategrey', font=font)
    draw.text((385+5, 304), str(GoldPerMinutRed[0][13]), fill='slategrey', font=font)

    champIcon = Image.open('./ChampionsImg/' + Champions[6] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (410, 330), champIcon)
    draw.text((445+5, 320), result_kda["kda7"], fill='slategrey', font=font)
    draw.text((445+5, 337), str(csW14[6]), fill='slategrey', font=font)
    draw.text((445+5, 354), str(GoldPerMinutRed[1][13]), fill='slategrey', font=font)

    champIcon = Image.open('./ChampionsImg/' + Champions[7] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (460, 390), champIcon)
    draw.text((495+5, 380), result_kda["kda8"], fill='slategrey', font=font)
    draw.text((495+5, 397), str(csW14[7]), fill='slategrey', font=font)
    draw.text((495+5, 414), str(GoldPerMinutRed[2][13]), fill='slategrey', font=font)

    champIcon = Image.open('./ChampionsImg/' + Champions[8] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (640, 510), champIcon)
    draw.text((675+5, 500), result_kda["kda9"], fill='slategrey', font=font)
    draw.text((675+5, 517), str(csW14[8]), fill='slategrey', font=font)
    draw.text((675+5, 534), str(GoldPerMinutRed[3][13]), fill='slategrey', font=font)

    champIcon = Image.open('./ChampionsImg/' + Champions[9] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (620, 430), champIcon)
    draw.text((655+5, 420), result_kda["kda10"], fill='slategrey', font=font)
    draw.text((655+5, 437), str(csW14[9]), fill='slategrey', font=font)
    draw.text((655+5, 454), str(GoldPerMinutRed[4][13]), fill='slategrey', font=font)



    #End of game
    champIcon = Image.open('./ChampionsImg/' + Champions[0] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (982, 360), champIcon)
    draw.text((265 + 752+5, 350), statsFinall["stats1"]["kda1"], fill='goldenrod', font=font)
    draw.text((265 + 752+5, 367), str(statsFinall["stats1"]["cs1"]), fill='goldenrod', font=font)
    draw.text((265 + 752+5, 384), str(GoldPerMinutBlue[0][-1]), fill='goldenrod', font=font)

    champIcon = Image.open('./ChampionsImg/' + Champions[1] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (420 + 752, 490), champIcon)
    draw.text((455 + 752+5, 480), statsFinall["stats2"]["kda2"], fill='goldenrod', font=font)
    draw.text((455 + 752+5, 497), str(statsFinall["stats2"]["cs2"]), fill='goldenrod', font=font)
    draw.text((455 + 752+5, 514), str(GoldPerMinutBlue[1][-1]), fill='goldenrod', font=font)

    champIcon = Image.open('./ChampionsImg/' + Champions[2] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (350 + 752, 440), champIcon)
    draw.text((385 + 752+5, 430), statsFinall["stats3"]["kda3"], fill='goldenrod', font=font)
    draw.text((385 + 752+5, 447), str(statsFinall["stats3"]["cs3"]), fill='goldenrod', font=font)
    draw.text((385 + 752+5, 464), str(GoldPerMinutBlue[2][-1]), fill='goldenrod', font=font)

    champIcon = Image.open('./ChampionsImg/' + Champions[3] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (550 + 752, 570), champIcon)
    draw.text((585 + 752+5, 560), statsFinall["stats4"]["kda4"], fill='goldenrod', font=font)
    draw.text((585 + 752+5, 577), str(statsFinall["stats4"]["cs4"]), fill='goldenrod', font=font)
    draw.text((585 + 752+5, 594), str(GoldPerMinutBlue[3][-1]), fill='goldenrod', font=font)

    champIcon = Image.open('./ChampionsImg/' + Champions[4] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (440 + 752, 570), champIcon)
    draw.text((475 + 752+5, 560), statsFinall["stats5"]["kda5"], fill='goldenrod', font=font)
    draw.text((475 + 752+5, 577), str(statsFinall["stats5"]["cs5"]), fill='goldenrod', font=font)
    draw.text((475 + 752+5, 594), str(GoldPerMinutBlue[4][-1]), fill='goldenrod', font=font)

    # RED
    champIcon = Image.open('./ChampionsImg/' + Champions[5] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (350 + 752, 280), champIcon)
    draw.text((385 + 752+5, 270), statsFinall["stats6"]["kda6"], fill='slategrey', font=font)
    draw.text((385 + 752+5, 287), str(statsFinall["stats6"]["cs6"]), fill='slategrey', font=font)
    draw.text((385 + 752+5, 304), str(GoldPerMinutRed[0][-1]), fill='slategrey', font=font)

    champIcon = Image.open('./ChampionsImg/' + Champions[6] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (410 + 752, 330), champIcon)
    draw.text((445 + 752+5, 320), statsFinall["stats7"]["kda7"], fill='slategrey', font=font)
    draw.text((445 + 752+5, 337), str(statsFinall["stats7"]["cs7"]), fill='slategrey', font=font)
    draw.text((445 + 752+5, 354), str(GoldPerMinutRed[1][-1]), fill='slategrey', font=font)

    champIcon = Image.open('./ChampionsImg/' + Champions[7] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (460 + 752, 390), champIcon)
    draw.text((495 + 752+5, 380), statsFinall["stats8"]["kda8"], fill='slategrey', font=font)
    draw.text((495 + 752+5, 397), str(statsFinall["stats8"]["cs8"]), fill='slategrey', font=font)
    draw.text((495 + 752+5, 414), str(GoldPerMinutRed[2][-1]), fill='slategrey', font=font)

    champIcon = Image.open('./ChampionsImg/' + Champions[8] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (640 + 752, 510), champIcon)
    draw.text((675 + 752+5, 500), statsFinall["stats9"]["kda9"], fill='slategrey', font=font)
    draw.text((675 + 752+5, 517), str(statsFinall["stats9"]["cs9"]), fill='slategrey', font=font)
    draw.text((675 + 752+5, 534), str(GoldPerMinutRed[3][-1]), fill='slategrey', font=font)

    champIcon = Image.open('./ChampionsImg/' + Champions[9] + '.png').convert('RGBA')
    champIcon = champIcon.resize((35, 35))
    image.paste(champIcon, (620 + 752, 430), champIcon)
    draw.text((655 + 752+5, 420), statsFinall["stats10"]["kda10"], fill='slategrey', font=font)
    draw.text((655 + 752+5, 437), str(statsFinall["stats10"]["cs10"]), fill='slategrey', font=font)
    draw.text((655 + 752+5, 454), str(GoldPerMinutRed[4][-1]), fill='slategrey', font=font)


    #image.show()
    image.save("./Graphs/HeadToHeadGraph.png")


if "__main__" == __name__:
    result_kda = 0
    GoldPerMinutRed = 0
    GoldPerMinutBlue = 0
    csW14 = 0
    Champions = []
    statsFinall = {}
    team1 = ""
    team2 = ""
    wynik = 0
    HeadToHeadGraph(result_kda,GoldPerMinutRed,GoldPerMinutBlue,csW14,Champions,statsFinall,team1, team2 ,wynik)