"""
Convert images file to lmdb data and train network
Network weights will be stored in 'weights' directory
"""
import os

import config

caffe_root = config.caffe_root
image_root = config.image_root
data_root = config.data_root
K = config.K
solver = config.solver

import matplotlib
matplotlib.use('Agg')
import sys
sys.path.insert(0, caffe_root + 'python')
import caffe
caffe.set_mode_cpu()

import convert

if os.path.isdir("weights") is not True:
	os.makedirs("weights")

#create lmdb data
convert.convert("train_image")
convert.convert("test_image")

#train net
cmd = caffe_root + "build/tools/caffe train --solver=" + solver
os.popen(cmd)
