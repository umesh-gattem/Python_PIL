"""
Write a Python script to load an image and the respective json data,
randomly select 10 points on the image and check whether each point is falling
inside any of the text areas or not. Display the result to console.

"""

from PIL import ImageDraw, Image
import json
import random
from collections import OrderedDict
from shapely import geometry as gm

with open("../json/first_image.json") as json_file:
    im = Image.open('../images/first_image.jpg')
    width, height = im.size
    draw = ImageDraw.Draw(im)
    json_data = json.load(json_file, object_pairs_hook=OrderedDict)
    text_areas = []
    for key, value in json_data.items():
        for any_area, co_ordinates in value.items():
            res = []
            for each_co_ordinate in co_ordinates:
                res.append(tuple(each_co_ordinate))
            text_areas.append(res)
    points = [(random.randint(0, width), random.randint(0, height)) for k in range(10)]
    print("Co_ordinates", "  " 'Falling in text areas')
    for point in points:
        flag = 0
        for text_area in text_areas:
            if len(text_area) == 4:
                if gm.Polygon(text_area).contains(gm.Point(point)):
                    print(point, "    ", 'True')
                    flag = 1
        if flag == 0:
            print(point, "   ", 'False')
