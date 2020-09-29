from PIL import Image, ImageFilter

image = Image.open('../Day14/Pics/db23-izrvxmf9891695.png')
print(image.mode, image.size, image.format)
image.filter(ImageFilter.CONTOUR).show()
# image.show()
