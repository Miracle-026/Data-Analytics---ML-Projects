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