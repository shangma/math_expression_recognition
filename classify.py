import os
import numpy as np
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
"""
For image classification
Input: image list for classifying(28X28), network model, network weights file
Output: list of categories
"""
def prediction(images_list, model, weight):
	net = caffe.Net(model, weight,caffe.TEST)
	transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
	transformer.set_transpose('data', (2,0,1))
	categories = []
	for image in images_list:
		img = caffe.io.load_image(image, color=False)
		net.blobs['data'].data[...] = transformer.preprocess('data', img)
		out = net.forward()
		print out['prob']
		predicted_label = np.argmax(out['prob'][0])
		categories.append(predicted_label)

	return categories

"""
image_list = ["/home/xing/Aipoly/mnist/images/test_image/3/12.bmp","/home/xing/Aipoly/mnist/images/test_image/4/41.bmp"]
results = prediction(image_list, "lenet_test.prototxt", "weights/lenet_iter_2000.caffemodel")

print results
"""
