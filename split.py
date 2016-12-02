import cv2
import numpy as np

from display import show
from display import showname

"""
check if there are chars connected together in one image
if yes split them
"""
def split(ilist):
    dictionary = {}
    for image in ilist:
        img = cv2.imread(image)
        height, width, channels = img.shape
        dictionary[image] = width
    #sort image according to width
    orders = sorted(dictionary.items(),key=lambda t:t[1],reverse=False)

    avewid = orders[0][1]
    sumwid = orders[0][1]
    #for each iteration, computer the average of the width of images so fall, if the current width is larger than the twice of avg, then it should be splitted
    for i in range(1,len(orders)):
        if orders[i][1] > 1.95*avewid:
            #for j in  range(i,len(orders)):
                #print orders[j][0]
            return splitimage(orders, i, avewid)
            
        sumwid += orders[i][1]
        avewid = sumwid/(i+1)
    return ilist

"""
split images 
""" 
def splitimage(ilist, start, avg):
    newlist = []
    for i in xrange(0,start):
    	newlist.append(ilist[i][0])
    #split images	
    for i in xrange(start,len(ilist)):
        img = cv2.imread(ilist[i][0])
        height, width, channels = img.shape

    	cut = 1
    	while((cut+2)*avg<width):
    		cut+=1
    	print `cut`+": "+ilist[i][0]
        #check how many times we need to split accoring to images width
    	newwid = width/(cut+1)

    	for k in xrange(0, cut+1):
    		crop_img = img[0:height, k*newwid:(k+1)*newwid][:]
    		cv2.imwrite(ilist[i][0]+"_"+`k`+".png",crop_img)
    		newlist.append(ilist[i][0]+"_"+`k`+".png")

    return newlist