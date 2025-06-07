#!/bin/python3
"""
Introduction to pillow
Pillow is a third-party library that is used to manipulate images. It is known as PIL (Python Imaging Library).
This library can be used to read, manipulate and save images. It also allows the image processing capability to the python interpreter. Pillow also offers a robust image processing capabilities along with support for multiple file formats.
Alex Clark is one of the prominent names in the list of Pillow contributors. 
"""
#To blur images:
from PIL import Image, ImageFilter
my_image = Image.open('C:\\Users\Anugo\pic.jpg')
image_blur = my_image.filter(ImageFilter.BLUR)
image_blur.save("pic.jpg")
image_blur.show()
#To flip images:
my_image2 = Image.open("C:\\Users\Anugo\pic.jpg")
image_flip = my_image2.transpose(Image.FLIP_LEFT_RIGHT)
image_flip.save("C:\\Users\Anugo\pic_flip.jpg")
image_flip.show()
#To sharpen images:
my_image3 = Image.open("C:\\Users\Anugo\picz.jpg")
image_sharpen = my_image3.filter(ImageFilter.SHARPEN)
image_sharpen.save("C:\\Users\Anugo\picz_sharpen.jpg")
image_sharpen.show()
#To set images to greyscale:
my_image4 = Image.open("C:\\Users\Anugo\picz.jpg")
image_convert = my_image4.convert('L')
image_convert.save("C:\\Users\Anugo\picz_greyscale.jpg")
image_convert.show()
#To enhance images:
from PIL import ImageEnhance
my_image5 = Image.open("C:\\Users\Anugo\pic.jpg")
image_enhance = ImageEnhance.Contrast(my_image5)
image_enhance.enhance(1.8).show("30% more contrast")

#Other image editing tools in Python include:
#Scikit-image (skimage):
import matplotlib.pyplot as plt
from skimage import data, filters
image = data.coins()
edges = filters.sobel(image)
plt.imshow(edges, cmap='gray')
plt.show()
#How to import multiple images with names:
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from skimage import data
images = ('astronaut', 'brick', 'camera', 'cell')
for name in images:
	caller = getattr(data, name)
	image = caller()
	plt.figure()
	plt.title(name)
	if image.ndim == 2:
		plt.imshow(image, cmap=plt.cm.gray)
	else:
		plt.imshow(image)
plt.show()
#To show multiple images as thumbnail:
fig, axs = plt.subplots(nrows=3, ncols=3)
for ax in axs.flat:
	ax.axis("off")
axs[0, 0].imshow(data.astronaut())
axs[0, 1].imshow(data.binary_blobs())
axs[0, 2].imshow(data.brick(), cmap='gray_r')
axs[1, 0].imshow(data.colorwheel())
axs[1, 1].imshow(data.camera(), cmap='Spectral')
axs[1, 2].imshow(data.cat())
axs[2, 0].imshow(data.checkerboard(), cmap='Greys')
axs[2, 1].imshow(data.clock(), cmap='Oranges')
further_img = np.full((300, 300), 255)
for xpos in [100, 150, 200]:
	further_img[150 - 10 : 150 + 10, xpos - 10 : xpos + 10]
axs[2, 2].imshow(further_img, cmap=plt.cm.gray)
plt.subplots_adjust(wspace=0.1, hspace=0.1)
plt.show()

#NumPy
#Masking an image
import numpy as np
from skimage import data
import matplotlib.pyplot as plt
image1 = data.camera()
type(image1) 
np.ndarray
mask = image1 < 87
image1[mask]=255
plt.imshow(image1, cmap='Greys_r')
plt.show()

#SciPy
import scipy as sp
from scipy import misc, ndimage
face = misc.face()
blurred_face = ndimage.gaussian_filter(face, sigma=3)
very_blurred = ndimage.gaussian_filter(face, sigma=5)
plt.imshow(face)
plt.imshow(blurred_face)
plt.imshow(very_blurred)
plt.show()