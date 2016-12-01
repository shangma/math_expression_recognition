from skimage.morphology import skeletonize
from skimage import draw
import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.image as mpimg

def average(img):
    #img = cv2.imread(image)
    return np.average(img, axis=-1).astype('uint8')


def show(img_list,column=3):
    #image = mpimg.imread("chelsea-the-cat.png")
    fig = plt.figure()
    row = (len(img_list)-1)/column +1 
    cell = column*10+row*100
    i=0
    for img in img_list:
        i+=1
        plt.subplot(cell+i)
        plt.imshow(img, interpolation='nearest', cmap=plt.get_cmap('gray'))
    plt.show()

def skele(img):
# an empty image
	image = '/home/xing/Documents/code/127.png'
	img = cv2.imread(image)
	img = average(img)
	img = cv2.adaptiveThreshold(img,1,1,1,11,2)
	print img.shape

	# perform skeletonization
	skeleton = skeletonize(img)

	show([img,skeleton],2)
	return sketeton
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
