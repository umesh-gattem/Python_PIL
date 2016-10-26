'''
problem 4 :
Write a Python script to load an image and the respective json data, mark the text areas on the image with red color
and mark the line areas on the image with blue color
(increase the thickness for proper visualization) and save the new marked image.
'''

from PIL import ImageDraw, Image
import json
from collections import OrderedDict

with open("../json/first_image.json") as json_file:
    im = Image.open('../images/first_image.jpg')
    draw = ImageDraw.Draw(im)
    json_data = json.load(json_file, object_pairs_hook=OrderedDict)
    for key, value in json_data.items():
        for any_area, co_ordinates in value.items():
            all_co_ordinates = []
            for each_co_ordinate in co_ordinates:
                for elements in each_co_ordinate:
                    all_co_ordinates.append(elements)
            if len(all_co_ordinates) == 4:
                image = draw.polygon(all_co_ordinates, fill=None, outline='blue')
            else:
                image = draw.polygon(all_co_ordinates, fill=None, outline='red')
    im.save('../images/annotated_first_image.jpg')
    im.show()
