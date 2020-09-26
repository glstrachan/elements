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
        if count == 2 or count == 10 or count == 18 or count == 36 or count == 54 or count == 86 or count == 118:
            red, green, blue = 253, 169, 133
        elif count == 4 or count == 12 or count == 20 or count == 38 or count == 56 or count == 88:
            red, green, blue = 117, 137, 191
        elif 20 < count and count < 31 or 38 < count and count < 49 or 71 < count and count < 81 or 103 < count and count < 113:
            red, green, blue = 111, 183, 214
        elif count == 5 or 12 < count and count < 15 or 30 < count and count < 34 or 48 < count and count < 53 or 80 < count and count < 85 or 112 < count and count < 117:
            red, green, blue = 145, 210, 144
        elif count == 1 or 5 < count and count < 10 or 14 < count and count < 18 or 33 < count and count < 36 or count == 53 or count == 85 or count == 117:
            red, green, blue = 255, 250, 129
        elif 56 < count and count < 72:
            red, green, blue = 204, 236, 239
        elif 88 < count and count < 104:
            red, green, blue = 207, 236, 207

        new_image(count, x.rstrip(), red, green, blue)
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
