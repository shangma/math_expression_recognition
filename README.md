# math_expression_recognition
This project is used to recognize an mathematics expression image and give calculate result.

Requirements:

0. python 2.7
0. caffe
0. python package:
	0. OpenCV
	0. scikit-image
0. Training images are saved in folder images as:
	images/train_images/'lable'/image_file_end_in_.bmp
	images/test_images/'lable'/image_file_end_in_.bmp
0. Only tested on Ubuntu 14.04.

Processing Pipeline:

0. Collect data and train the network (preprocessing.py):

	a. I used the MNIST images.
	Images of operators, such as '+', '-', and 'x', are taken from CHROHME dataset which provides a list of <x,y> coordinates drawn by users and transferred to bitmap images. The star operator '*' images are drawn by myself.

	b. I choose to use the lenet network because it is proved to be more proper for recognizing handwritten and machine-printed expression. Besides, the network itself is relatively small so I can train it on my own computer.

0. Image segmentation, a.k.a segment the expression to numbers and operators (segmentation.py):

	a. Convert images from rgb to grayscale
	I tried cv2.cvtColor function and my own average function which simply averages the rgb values and use that for a specific bit.

	b. Smooth the image to remove noises
	I tried median, gaussian, and bilateral filters, respectively. The first two cannot preserve the borders of an image. So I choose bilateralFilter instead.

	c. Convert to binary image
	To find the contours of numbers/operators, the image need to be binary. I used adaptiveThreshold to do so.

	d. Rotate image
	Rotating the image to a right angle can help separate original images to numbers and operators. It is also useful at the recognition stage. 
	To rotate an image, I first dilate it to make sure there is only one big blob. Based on the minimum bounding box of this blob, I can calculate the angle for rotation and do it afterwards.

	e. Find contours of digits/operators
	I use findContours function to find contours of digits/operators, and masks to cut them out from left to right. Here I remove the contours which are much closed to the border of the original image. That might be from other expression.

	After that, I found it's still very difficult to segment some characters since they are too closed to each other. So to solve the problem, I write a split function, which separates the segmentations which are twice width of the average of other small images.
		
	All the cropped images are converted to a square, resized to 28x28, and then saved as bitmap images.

0. Classify the saved bitmap images (classify.py)

0. Calculate the expression

Performance:

0. Segmentation Performance:
	The segmentation performance is very good. Accuracy is above 90% based on the given test images. Some errors happen when there is a narrow character such as a written '1'. In these cases, some very wide characters will be split to half.

0. Recognition Performance:

	0. Recognition for digits looks good, especially for machine-printed numbers. 
	0. However, due to the lack of training data of operators, there is still room for improvement on this part.

Usage:

0. Run:

	a. Run 'python run.py path_to_an_image_file' will do the recognition. You should be able to see three windows. The first one is the original image; the second one is the segmentation result; and the last one is the recognition result together with the original image. There are four test images inside the test_image folder for your convenience.

	b. Run 'python test_all.py path_to_a_directory' will do recognition for all the expressions in that directory. The test_image folder is there for your convenience.

The following are optional. You may follow them if re-training the network is needed:

0. Configuration: To use this code, you need to firstly do some configuration. Go to config.py to configure all the parameters you might want to modify, such as the caffe root, categories of the classification...

0. Train: Run 'python preprocessing.py' to train the network. The weight file with an extension of '.caffemodel' will be saved in the directory of 'weights'.







