import sys
import os
import time
import cv2
import numpy as np
from imageprocessing import average
from imageprocessing import square
from skimage.morphology import skeletonize
from skimage import draw
from rotation import rotateImage
from split import split
from display import show
from display import showname

def segment(image):
    timestamp = time.time()
    splitstrs = image.split('/')
    segment_dir = "segmentation/"+splitstrs[-1]+"_"+`timestamp`
    os.mkdir(segment_dir)
    # Load the image
    img = cv2.imread(image)
    print type(img)
    height, width, channels = img.shape
    
    # convert to grayscale
    gray = average(img) 
    #different way to conver image to grayscale
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    
   
	
    #smooth the image to avoid noises
    bilateral = cv2.bilateralFilter(gray,5,75,75)
    #different way to smooth image
    #blur = cv2.medianBlur(gray,5)
    #blur = cv2.GaussianBlur(gray,(5,5),0)
      
    #convert to binary image
    thresh = cv2.adaptiveThreshold(bilateral,255,1,1,11,2)
    #th, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY);
    
    #skele = skeletonize(thresh).astype(np.uint8)
    
    #rotate image
    rotated = rotateImage(thresh)
    # apply some dilation and erosion to join the gaps
    #dilated = cv2.dilate(rotated,None,iterations = 1)
    #thresh = cv2.erode(thresh,None,iterations = 2)
    
    #show([bilateral, thresh, rotated],4)

    #binary image (for cropping)
    blackimg = np.copy(rotated)

    # Find the contours
    margin = 5
    segs = {}
    max_w = 0
    max_h = 0
    contours,hierarchy = cv2.findContours(rotated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #index contours according to x coordinate
    idx = {}
    for i in xrange(len(contours)):
        cnt = contours[i]
        x,y,w,h = cv2.boundingRect(cnt)
        if x<margin or x+w>width-margin or y<margin or y+h>height-margin:
            if(h < height/3):
                continue
        if w>max_w:
            max_w = w
        if h>max_h:
            max_h = h
        idx[i] = x
    #order contours accoring to x coordinate
    orders = sorted(idx.items(),key=lambda t:t[1],reverse=False)

    num = 0
    image_list = []
    #store contours
    for data in orders:
        i = data[0]
        cnt = contours[i]
        x,y,w,h = cv2.boundingRect(cnt)
        #delete noise data 
        if w>max_w/5 or h>max_h/5:
            #crop character using mask
            #Create mask where white is what we want, black otherwise
            mask = np.zeros_like(blackimg) 
            # Draw filled contour in mask
            cv2.drawContours(mask, contours, i, 255, -1) 
            out = np.zeros_like(blackimg) 
            # Extract out the object and place into output image
            out[mask == 255] = blackimg[mask == 255]

            crop_img = out[y:y+h, x:x+w]
            segs[x] = crop_img
            num+=1
            name = chr(num+ord('a'))
            #resize to 28*28 for lenet network
            #res = cv2.resize(crop_img,(28, 28), interpolation = cv2.INTER_CUBIC)
            cv2.imwrite(segment_dir+"/"+name+".png",crop_img)
            image_list.append(segment_dir+"/"+name+".png")

    #split if two chars are connected 
    image_list = split(image_list)
    
    #convert chopped images to squre shape
    image_list = square(image_list, segment_dir)
    #showname(image_list,4)
    print segment_dir
    
    return image_list

#segment(sys.argv[1])




