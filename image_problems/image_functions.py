from PIL import Image


infile = 'house_grayscale_image.jpg'
with Image.open(infile) as im:
    print(infile, im.format, im.size, im.mode)
    width, height = im.size
    box = (100, 100, 400, 400)
    region = im.crop(box)
    region.show()
    region = region.transpose(Image.ROTATE_180)
    im.paste(region, box)
    im.show()
    region.show()
    # out = im.resize((128, 128))
    # out = im.rotate(45)
    # out.show()

