import os
import cv2
import sys
import config
caffe_root = config.caffe_root
image_root = config.image_root
data_root = config.data_root
K = config.K
model = config.model
weight = config.weight
character = config.character

from display import showwithtitle
from display import showname

import Tkinter
import tkMessageBox

import matplotlib
matplotlib.use('Agg')
import sys
sys.path.insert(0, caffe_root + 'python')
import caffe
caffe.set_mode_cpu()

from classify import prediction
import segmentation

if os.path.isdir("segmentation") is not True:
	os.makedirs("segmentation")

input_image = sys.argv[1]
print "image is "+input_image

showname([input_image],1,"Original Image")

segments = segmentation.segment(input_image)
showname(segments,3,"Segmentation Results")

#weight = "weights/lenet_iter_3000.caffemodel"


categories = prediction(segments, model, weight)
print categories
"""
result = {}
for i in xrange(len(categories)):
   print i
   print categories[i]
   result[categories[i]] = segments[i]
showwithtitle(result,5)
"""

expression = ""
for label in categories:
	expression += character[label]
print expression
msg = ""
try:
	msg = "Your expression is:\n"+expression + " = " + `eval(expression)`
except SyntaxError:
	msg = "Oops, I think there is something wrong.\n I can't understand this expression\n"+expression
print "Showing result of:\n "+input_image
showname([input_image],1,msg)




