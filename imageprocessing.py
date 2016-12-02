from skimage.morphology import skeletonize
from skimage import draw
import numpy as np
import cv2
import os

from display import show
from display import showname

"""
skeletonize an image
"""
def skele(img):
    #img = cv2.imread(image)
    img = average(img)
    img = cv2.adaptiveThreshold(img,1,1,1,11,2)

    # perform skeletonization
    skeleton_image = skeletonize(img)

    #show([img,skeleton_image],2)
    return skeleton_image.astype(np.uint8)

"""
blur an image using average
"""
def average(img):
    #img = cv2.imread(image)
    return np.average(img, axis=-1).astype('uint8')

"""
chage an image to squral image by adding 0(black pixels) surrounding
(for network use)
"""
def square(ilist, segment_dir):
	#sort images in the expression order
    ilist.sort()

    testdir = segment_dir+"/"+"char"
    if os.path.isdir(testdir):
		__import__('shutil').rmtree(testdir)
    os.mkdir(testdir)
    reslist = []
    i = 0
    for image in ilist:
        img = (cv2.imread(image))
        #grayscale
        if len(img.shape) == 3:
            img = average(img)

        height = img.shape[0]
        width = img.shape[1]
        #print "("+`width`+", "+`height`+")"
        length = max(height, width)
        mask = np.array([[0]*length]*length)
        #add 0 surrounding the original image
        if width<height:
            start = (height-width)/2
            addleft = np.zeros((height, start), dtype = img.dtype)
            addright = np.zeros((height, height-width-start), dtype = img.dtype)
            mask = np.concatenate((addleft, img, addright), axis=1)
        elif width>height:
            start = (width-height)/2
            addtop = np.zeros((start, width), dtype = img.dtype)
            addbottom = np.zeros((width-height-start, width), dtype = img.dtype)
            mask = np.concatenate((addtop, img, addbottom), axis=0)
        else:
            mask = np.copy(img)
        i+=1
        #res = cv2.resize(mask,(28, 28), interpolation = cv2.INTER_AREA)
        cv2.imwrite(testdir+"/"+`i`+".bmp",mask)
        

        reslist.append(testdir+"/"+`i`+".bmp")
    #showname(reslist)
    return reslist
"""
ilist=['images/test/127.png', 'images/test/132.png']
square(ilist,'images/test')
"""