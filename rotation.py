import sys
import math
import cv2
import numpy as np
from display import show

def angle(p0, p1, p2):
    dx1 = p1[0] - p0[0]
    dy1 = p1[1] - p0[1]
    dx2 = p2[0] - p0[0]
    dy2 = p2[1] - p0[1]
    print `dx1`+", "+`dx2`+", "+`dy1`+", "+`dy2`
    x = (dx1*dx2 + dy1*dy2)/(math.sqrt(dx1*dx1 + dy1*dy1)*math.sqrt(dx2*dx2 + dy2*dy2))
    print "x = "+`x`
    return x

def findDegree(box):
    coordinates = {}
    for i in xrange(4):
        coordinates[box[i][0]] = box[i][1]
        print box[i]
    #order 
    orders = sorted(coordinates.items(),key=lambda t:t[0],reverse=False)
    print orders
    x1 = (orders[0][0]+orders[1][0])/2
    y1 = (orders[0][1]+orders[1][1])/2
    x2 = (orders[2][0]+orders[3][0])/2
    y2 = (orders[2][1]+orders[3][1])/2
    print "("+`x1`+", "+`y1`+")"
    print "("+`x2`+", "+`y2`+")"
    if y1<y2:
        print "y1<y2"
        return math.acos(angle((x1,y1),(x2,y2),(x2,y1)))
    elif y1>y2:
        print "y1>y2"
        return -math.acos(angle((x2,y2),(x1,y1),(x1,y2)))
    else:
        return 0

def rotateImage(img):
    #image = cv2.imread(image)
    """
    print img
    bilateral = cv2.bilateralFilter(img,5,75,75)
    thresh = cv2.adaptiveThreshold(bilateral,255,1,1,11,6)   
    equal =  cv2.dilate(thresh,None,iterations = 21)   
    show([bilateral,thresh, equal],3)
    
    equal = cv2.equalizeHist(img)
    equal = cv2.medianBlur(equal,7)
    show([img,equal],2)
    """
    margin = 5
    height, width = img.shape
    crop = np.copy(img)
    contours,hierarchy = cv2.findContours(crop,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        if x<margin:
            crop = crop[0:height, w+margin:width]
        if x+w>width-margin:
            crop = crop[0:height, 0:width-w-margin]
        if y<margin:
            crop = crop[w+margin:height, 0:width]  
        if y+h>height-margin:
            crop = crop[0:height-w-margin, 0:width]  
    for i in range(1,100,2):
        equal =  cv2.dilate(crop,None,iterations = i)
        contours,hierarchy = cv2.findContours(equal,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours)==1:
            break  
    #find minimum rectangle
    cnt = contours[0]
    rect = cv2.minAreaRect(cnt)
    #cv2.drawContours(equal, contours, 0,  (255,0,0), -1)
    #show([img, crop, equal],3)

    box = cv2.cv.BoxPoints(rect)
    box = np.int0(box)

    degree = findDegree(box)
    #print "degree is "+`degree`

    #rotate rectangle
    image_center = rect[0]
    rot_mat = cv2.getRotationMatrix2D(image_center,degree*180/3.14159,1.0)
    rotation1 = cv2.warpAffine(img, rot_mat, (img.shape[1],img.shape[0]))
    #show([img,rotation1],2)
    return rotation1
"""
img = cv2.imread(sys.argv[1])
#gray = average(img) 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.bitwise_not(gray)

bilateral = cv2.bilateralFilter(gray,5,75,75)

img = cv2.imread(sys.argv[1])
gray = average(img) 
bilateral = cv2.bilateralFilter(gray,5,75,75)
thresh = cv2.adaptiveThreshold(bilateral,255,1,1,11,2)   
rotateImage(thresh)
"""


