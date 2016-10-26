'''
Problem 1 :
Write a Python script to load any grayscale image, crop 50% of the image horizontally and 50% of the image vertically
and save them as new images.
'''

from PIL import Image

# im = Image.open('image.jpg')
# im.save('my_image.jpg')
# print(im.format, im.size, im.mode)

infile = 'house_grayscale_image.jpg'
with Image.open(infile) as im:
    print(infile, im.format, im.size, im.mode)
    width, height = im.size
    horizontal = (0, 0, width / 2, height)
    vertical = (0, 0, width, height / 2)
    horizontal_half = im.crop(horizontal)
    horizontal_half.save('image_horizontal.jpg')
    vertical_half = im.crop(vertical)
    vertical_half.save('image_vertical.jpg')
    horizontal_half.show()
    vertical_half.show()
