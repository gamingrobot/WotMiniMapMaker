import Image
import os


def main():
    # change working directory if this script is called from another location
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    inputimages = os.listdir("in")
    print "adding grid lines:"
    for image in inputimages:
        print str(image)
        foreground = Image.open("in/" + str(image))
        background = Image.open("grid.png")
        gridlines = Image.open("gridlines.png")

        background.paste(foreground, (30, 30))
        background.paste(gridlines, (0, 0), gridlines)

        background.save("out/" + str(image))


if __name__ == '__main__':
    main()
