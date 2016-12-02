import os
import cv2
import sys
import config
caffe_root = config.caffe_root
image_root = config.image_root
data_root = config.data_root
K = config.K

from display import showwithtitle
from display import showname

import matplotlib
matplotlib.use('Agg')
import sys
sys.path.insert(0, caffe_root + 'python')
import caffe
caffe.set_mode_cpu()

from classify import prediction
import segmentation
model = "lenet_test.prototxt"
weight = "weights/lenet_iter_5000.caffemodel"
input_image = sys.argv[1]
print "image is "+input_image


showname([input_image],1)

segments = segmentation.segment(input_image)
showname(segments)
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
character = ["0","1","2","3","4","5","6","7","8","9","+","-","*","*"]
expression = ""
for label in categories:
	expression += character[label]
print expression
try:
	print expression + " = " + `eval(expression)`
except SyntaxError:
	print "Oops, I think there is something wrong. I can't understand this expression"

