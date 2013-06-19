from xml.dom.minidom import parseString
from bs4 import BeautifulSoup
import os
import re
import string
import math
import Image


def main():
    for filename in os.listdir("arena_defs_decoded"):
        readxml(filename)
    #readxml('siegfried_line_14.xml')
    #readxml('malinovka_02.xml')
    #readxml('komarin_15.xml')
    #readxml('westfeld_23.xml')


def readxml(filename):
    file = open('arena_defs_decoded/' + filename, 'r')
    #convert to string:
    data = file.read()
    #close file because we dont need it anymore:
    file.close()

    filenum = filename[-6:-4]
    filename = filenum + '_' + filename[:-7]
    print filename

    soup = BeautifulSoup(data, 'xml')

    bottomLeft = soup.find("bottomLeft")
    upperRight = soup.find("upperRight")
    bottomLeft = bottomLeft.contents
    upperRight = upperRight.contents
    x2, y2 = string.split(bottomLeft[0])
    x1, y1 = string.split(upperRight[0])
    x2, y2 = float(x2), float(y2)
    x1, y1 = float(x1), float(y1)
    #print x1, y1

    if math.fabs(x1) != math.fabs(y2) or math.fabs(x2) != math.fabs(y1):
        print "could not process " + str(filename)
        return

    ctf = soup.find("ctf")
    ass = soup.find("assault")
    dom = soup.find("domination")
    if ctf != None:
        #print "CTF"
        background = Image.open("mapsRaw/" + filename + "/mmap.png")
        teamBasePositions = ctf.find("teamBasePositions")
        team1 = teamBasePositions.find("team1")
        team2 = teamBasePositions.find("team2")
        team1Position = team1.find(re.compile("^position"))
        team2Position = team2.find(re.compile("^position"))
        #print team1Position, team2Position
        #scale and place on map
        foreground = Image.open("icon/" + 'green' + ".png")
        inx, iny = convertScaleToXY(team1Position.contents[0], x1)
        background.paste(foreground, (int(inx), int(500 - iny)), foreground)
        #put second team in
        foreground = Image.open("icon/" + 'red' + ".png")
        inx, iny = convertScaleToXY(team2Position.contents[0], x1)
        background.paste(foreground, (int(inx), int(500 - iny)), foreground)
        #do spawn points
        teamSpawnPoints = ctf.find("teamSpawnPoints")
        if teamSpawnPoints != None:
            team1 = teamSpawnPoints.find("team1")
            team2 = teamSpawnPoints.find("team2")
            team1SpawnPoint = team1.find_all("position")
            team2SpawnPoint = team2.find_all("position")
            #print team1SpawnPoint, team2SpawnPoint
            #team1 first
            counter = 1
            for spawn in team1SpawnPoint:
                foreground = Image.open("icon/" + 'gs' + str(counter) + ".png")
                inx, iny = convertScaleToXY(spawn.contents[0], x1)
                background.paste(foreground, (int(inx), int(500 - iny)), foreground)
                counter += 1
            #team2 second
            counter = 1
            for spawn in team2SpawnPoint:
                foreground = Image.open("icon/" + 'rs' + str(counter) + ".png")
                inx, iny = convertScaleToXY(spawn.contents[0], x1)
                background.paste(foreground, (int(inx), int(500 - iny)), foreground)
                counter += 1
        background.save("gridding/in/" + filename + "_" + "ctf" + ".png")

    if ass != None:
        #print "ASS"
        background = Image.open("mapsRaw/" + filename + "/mmap.png")
        teamBasePositions = ass.find("teamBasePositions")
        if teamBasePositions != None:
            team1 = teamBasePositions.find("team1")
            team2 = teamBasePositions.find("team2")
            team1Position = team1.find(re.compile("^position"))
            team2Position = team2.find(re.compile("^position"))
            #print team1Position, team2Position
            #first team: scale and place on map
            if team1Position != None:
                foreground = Image.open("icon/" + 'green' + ".png")
                inx, iny = convertScaleToXY(team1Position.contents[0], x1)
                background.paste(foreground, (int(inx), int(500 - iny)), foreground)
            #put second team in
            if team2Position != None:
                foreground = Image.open("icon/" + 'red' + ".png")
                inx, iny = convertScaleToXY(team2Position.contents[0], x1)
                background.paste(foreground, (int(inx), int(500 - iny)), foreground)
        #find spawn points
        teamSpawnPoints = ass.find("teamSpawnPoints")
        if teamSpawnPoints != None:
            team1 = teamSpawnPoints.find("team1")
            team2 = teamSpawnPoints.find("team2")
            team1SpawnPoint = team1.find_all("position")
            team2SpawnPoint = team2.find_all("position")
            #print team1SpawnPoint, team2SpawnPoint
            #team1 first
            counter = 1
            for spawn in team1SpawnPoint:
                foreground = Image.open("icon/" + 'gs' + str(counter) + ".png")
                inx, iny = convertScaleToXY(spawn.contents[0], x1)
                background.paste(foreground, (int(inx), int(500 - iny)), foreground)
                counter += 1
            #team2 second
            counter = 1
            for spawn in team2SpawnPoint:
                foreground = Image.open("icon/" + 'rs' + str(counter) + ".png")
                inx, iny = convertScaleToXY(spawn.contents[0], x1)
                background.paste(foreground, (int(inx), int(500 - iny)), foreground)
                counter += 1
        background.save("gridding/in/" + filename + "_" + "ass" + ".png")

    if dom != None:
        #print "DOM"
        background = Image.open("mapsRaw/" + filename + "/mmap.png")
        controlPoint = dom.find("controlPoint")
        #print controlPoint
        #scale and place on map
        foreground = Image.open("icon/" + 'blank' + ".png")
        inx, iny = convertScaleToXY(controlPoint.contents[0], x1)
        background.paste(foreground, (int(inx), int(500 - iny)), foreground)
        #find spawn points
        teamSpawnPoints = dom.find("teamSpawnPoints")
        team1 = teamSpawnPoints.find("team1")
        team2 = teamSpawnPoints.find("team2")
        team1SpawnPoint = team1.find_all("position")
        team2SpawnPoint = team2.find_all("position")
        #print team1SpawnPoint, team2SpawnPoint
        #team1 first
        counter = 1
        for spawn in team1SpawnPoint:
            foreground = Image.open("icon/" + 'gs' + str(counter) + ".png")
            inx, iny = convertScaleToXY(spawn.contents[0], x1)
            background.paste(foreground, (int(inx), int(500 - iny)), foreground)
            counter += 1
        #team2 second
        counter = 1
        for spawn in team2SpawnPoint:
            foreground = Image.open("icon/" + 'rs' + str(counter) + ".png")
            inx, iny = convertScaleToXY(spawn.contents[0], x1)
            background.paste(foreground, (int(inx), int(500 - iny)), foreground)
            counter += 1
        background.save("gridding/in/" + filename + "_" + "dom" + ".png")


def convertScaleToXY(input, scale):
    inx, iny = string.split(input)
    inx, iny = int(round(float(inx.replace(',', '.')))), int(round(float(iny.replace(',', '.'))))
    #0-1000 instead of -500-500
    inx += scale
    iny += scale
    #scale to 500x500
    doublescale = scale * 2
    divscale = doublescale / 500.0
    inx /= divscale
    iny /= divscale
    #fix icon size
    inx -= 24
    iny += 24
    return inx, iny


if __name__ == '__main__':
    main()
