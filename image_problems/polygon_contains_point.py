"""
Write a Python script to load an image and the respective json data,
randomly select 10 points on the image and check whether each point is falling
inside any of the text areas or not. Display the result to console.

"""

from PIL import ImageDraw, Image
import json
from collections import OrderedDict
from shapely import geometry as gm


with open("../json/first_image.json") as json_file:
    im = Image.open('../images/first_image.jpg')
    draw = ImageDraw.Draw(im)
    json_data = json.load(json_file, object_pairs_hook=OrderedDict)
    text_areas = []
    for key, value in json_data.items():
        for any_area, co_ordinates in value.items():
            res = []
            for each_co_ordinate in co_ordinates:
                res.append(tuple(each_co_ordinate))
            text_areas.append(res)
    for text_area in text_areas:
        if len(text_area) == 4:
            if gm.Polygon(text_area).contains(gm.Point(91.5, 153)):
                print("true")
                exit()
            else:
                print('false')
