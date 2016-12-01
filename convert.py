import os
import config
caffe_root = config.caffe_root
image_root = config.image_root
data_root = config.data_root
K = config.K

"""
Convert images to lmdb data. image path: image_root/data_type/label/image.bmp
Input: data type
Output:Null
lmdb data will be stored in image_root/data_type+"_data"/lmdb
mean value will be stored in image_root/data_type+"_data"/lmdb/mean.binaryproto
"""
def convert(data_type="test_image"):
	
	image_list = open(image_root+data_type+".txt", 'w')
	dest = image_root+data_type+"_data"
	if os.path.isdir(dest):
		__import__('shutil').rmtree(dest)
	os.makedirs(dest)

	for i in range(0,K):
		files = os.listdir(image_root+data_type+"/"+`i`)
		for f in files:
			if f.endswith(".bmp"):
				image_list.write(`i`+"/"+f+" "+`i`+"\n")
	image_list.close()

	#convert images to leveldb
	caffe_convert_imageset = caffe_root+"build/tools/convert_imageset"
	os.popen("GLOG_logtostderr=1 "+caffe_convert_imageset+" --shuffle "+image_root+data_type+"/ "+image_root+data_type+".txt"+" "+dest+"/lmdb")
	#compute mean value
	caffe_compute_image_mean = caffe_root+"build/tools/compute_image_mean"
	os.popen(caffe_compute_image_mean+" "+dest+"/lmdb "+dest+"/mean.binaryproto")



#convert()
