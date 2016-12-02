from skimage.morphology import skeletonize
from skimage import draw
import numpy as np
import cv2


from display import show
from display import showname



def skele(img):
# an empty image
	image = '/home/xing/Documents/code/127.png'
	img = cv2.imread(image)
	img = average(img)
	img = cv2.adaptiveThreshold(img,1,1,1,11,2)
	print img.shape

	# perform skeletonization
	skeleton_image = skeletonize(img)

	show([img,skeleton_image],2)
	return skeleton_image
"""
# display results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5), sharex=True, sharey=True, subplot_kw={'adjustable':'box-forced'})

ax1.imshow(image, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('original', fontsize=20)

ax2.imshow(skeleton, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('skeleton', fontsize=20)

fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.98,
                    bottom=0.02, left=0.02, right=0.98)

plt.show()
"""
