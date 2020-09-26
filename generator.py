from PIL import Image, ImageDraw, ImageFont

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path

# Gets the names of the elements
def get_name():
    file = open(dir_path + '\\names.txt', "r")

    count = 1;
    red, green, blue = 0, 0, 0

    for x in file:
        x = x.rstrip()
        colour = x[len(x) - 2:len(x)]

        if colour == "YE":
            red, green, blue = 240, 255, 143
        elif colour == "BL":
            red, green, blue = 192, 255, 255
        elif colour == "RE":
            red, green, blue = 255, 157, 157
        elif colour == "OR":
            red, green, blue = 255, 222, 173
        elif colour == "GR":
            red, green, blue = 204, 204, 153
        elif colour == "DB":
            red, green, blue = 204, 204, 204
        elif colour == "LR":
            red, green, blue = 255, 192, 192
        elif colour == "PU":
            red, green, blue = 255, 191, 255
        elif colour == "MA":
            red, green, blue = 255, 153, 204
        elif colour == "GE":
            red, green, blue = 232, 232, 232

        new_image(count, x[0:len(x) - 2], red, green, blue)
        count += 1;
    file.close()

# Creates an image with desired properties
def new_image(number, name, red, green, blue):
    img = Image.new('RGB', (1000, 1000), color = (red, green, blue))

    fnt = ImageFont.truetype(dir_path + '\Helvetica.ttf', 500)
    d = ImageDraw.Draw(img)
    d.text((190, 245), name, font=fnt, fill=(0, 0, 0))

    img.save(dir_path + '\images\\' + name + '.png')

get_name()
