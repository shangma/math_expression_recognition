import os
import cv2
import sys
import config
caffe_root = config.caffe_root
image_root = config.image_root
data_root = config.data_root
K = config.K

import matplotlib
matplotlib.use('Agg')
import sys
sys.path.insert(0, caffe_root + 'python')
import caffe
caffe.set_mode_cpu()

import classify
import segmentation
model = "lenet_test.prototxt"
weight = "weights/lenet_iter_1000.caffemodel"
input_image = sys.argv[1]
print "image is "+input_image
"""
segments = segmentation.segment(input_image)
categories = test.prediction(segments, model, weight)
print categories

character = ["0","1","2","3","4","5","6","7","8","9","0","+","-","*","*"]
expression = ""
for label in categories:
	expression += character[lable]
print expression+" = "+eval(expression)
"""
