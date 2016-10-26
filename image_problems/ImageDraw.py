'''
problem 2  :
Write a Python script to load an image, draw a rectangle of shape (100*200) anywhere on the image
and fill the rectangle with the colour of your own choice.

'''

from PIL import Image, ImageDraw

im = Image.open('house_grayscale_image.jpg')
draw = ImageDraw.Draw(im)
# image = draw.arc([0, 0, 200, 200], 90, 180, fill='blue')
# image = draw.ellipse([100, 200, 300, 500], fill='red', outline='white')
image = draw.rectangle([300, 400, 400, 600], fill='blue', outline='green')
im.show()
