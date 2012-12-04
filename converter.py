

def main():
    import Image

    themap = raw_input("Map: ")
    background = Image.open("mapsRaw/" + themap + "/mmap.png")
    gametype = raw_input("Gametype: ")
    thescale = int(raw_input("Scale: "))
    done = False
    while(done != True):
        foreground = Image.open("icon/" + raw_input("Marker Filename: ") + ".png")
        inx = int(raw_input("X:"))
        iny = int(raw_input("Y:"))
        #0-1000 instead of -500-500
        inx += thescale
        iny += thescale
        #scale to 500x500
        doublescale = thescale * 2
        divscale = doublescale / 500.0
        inx /= divscale
        iny /= divscale
        #fix icon size
        inx -= 24
        iny += 24

        background.paste(foreground, (int(inx), int(500 - iny)), foreground)

        if raw_input("Done?") == "y":
            done = True

    background.save("maps/" + themap + "_" + gametype + ".png")


if __name__ == '__main__':
    main()
