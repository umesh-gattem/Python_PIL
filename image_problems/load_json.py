'''
problem 3 :
Write a Python script to load the json data of text and line area markings for an image(from Annotation project)
and count how many line areas and text areas are there in that image.
'''

import json
from collections import OrderedDict

with open("../json/first_image.json") as json_file:
    json_data = json.load(json_file, object_pairs_hook=OrderedDict)
    # print(json_data)
    count = []
    for key, value in json_data.items():
        res = 0
        for any_area, co_ordinates in value.items():
            res += 1
        count.append(res)
    print("text areas are :", count[0])
    print("line areas are :", count[1])


