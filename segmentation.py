import sys
import cv2
import numpy as np
from skeleton import average
from skeleton import skele
from skeleton import show

def segment(image):
    # Load the image
    img = cv2.imread(image)
    print type(img)
    height, width, channels = img.shape
    
    # convert to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    
   
    #smooth the image to avoid noises
    #gray = cv2.medianBlur(gray,5)
    #show(gray,"medianblur")
    #blur = cv2.GaussianBlur(gray,(5,5),0)
    #show(blur,"GaussianBlur")
    #gray = cv2.bilateralFilter(gray,5,75,75)
    #show(gray,"bilateralFilter") 
	gray = average(img)
      
    #th, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY);
    thresh = cv2.adaptiveThreshold(gray,1,1,1,11,2)
	show([img,gray,thresh],3)
    
    #thresh_color = cv2.cvtColor(thresh,cv2.COLOR_GRAY2BGR)
    # apply some dilation and erosion to join the gaps
    
    #thresh = cv2.dilate(thresh,None,iterations = 1)
    #show(thresh,"thresh")

    #thresh = cv2.erode(thresh,None,iterations = 2)
    cv2.imwrite("black.png",thresh)
    blackimg = cv2.imread("black.png")
    
    # Find the contours
    margin = 5
    segs = {}
    max_w = 0
    max_h = 0
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #index contours according to x coordinate
    idx = {}
    for i in xrange(len(contours)):
        cnt = contours[i]
        x,y,w,h = cv2.boundingRect(cnt)
        if x<margin or x+w>width-margin or y<margin or y+h>height-margin:
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
        #delete noise
        if w>max_w/3 or h>max_h/3:
            #crop character using mask
            mask = np.zeros_like(img) # Create mask where white is what we want, black otherwise
            # Draw filled contour in mask
            cv2.drawContours(mask, contours, i, (255,255,255), -1) 
            out = np.zeros_like(img) 
            # Extract out the object and place into output image
            out[mask == 255] = blackimg[mask == 255]
            #crop using square		
            l = max(w,h)
            x = max(0, x-(l-w)/2)
            y = max(0, y-(l-h)/2)
            crop_img = out[y:y+l, x:x+l]
            segs[x] = crop_img
            num+=1

            #resize to 28*28 for lenet network
            res = cv2.resize(crop_img,(28, 28), interpolation = cv2.INTER_CUBIC)
            cv2.imwrite(image+"_"+`num`+".png",res)
            image_list.append(image+"_"+`num`+".png")

    return image_list


print segment(sys.argv[1])




