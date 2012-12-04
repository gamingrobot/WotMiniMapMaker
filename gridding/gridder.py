import Image
import os


def main():
    inputimages = os.listdir("in")
    for image in inputimages:
        foreground = Image.open("in/" + str(image))
        background = Image.open("grid.png")
        gridlines = Image.open("gridlines.png")

        background.paste(foreground, (30, 30))
        background.paste(gridlines, (0, 0), gridlines)

        background.save("out/" + str(image))


if __name__ == '__main__':
    main()
