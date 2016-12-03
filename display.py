import matplotlib.pyplot as plt
import matplotlib.image as mpimg

"""
show images
input: list of image names
"""
def showname(img_list,column=3,title="My Calculation"):
    fig = plt.figure()
    row = (len(img_list)-1)/column +1 
    cell = column*10+row*100
    i=0
    for image in img_list:
        img = mpimg.imread(image)
        i+=1
        plt.subplot(cell+i)
        plt.imshow(img, interpolation='nearest', cmap=plt.get_cmap('gray'))
    plt.suptitle(title)
    plt.show()

"""
show images
input: list of image files
"""
def show(img_list,column=3,title="My Calculation"):
    fig = plt.figure()
    row = (len(img_list)-1)/column +1 
    cell = column*10+row*100
    i=0
    for img in img_list:
        i+=1
        plt.subplot(cell+i)
        plt.imshow(img, interpolation='nearest', cmap=plt.get_cmap('gray'))
    plt.suptitle(title)
    plt.show()

"""
show images with titles
input: list of image names
"""
def showwithtitle(img_list,column=3,title="My Calculation"):
    fig = plt.figure()
    row = (len(img_list)-1)/column +1 
    cell = column*10+row*100
    i=0
    for title in img_list.keys():
        img = mpimg.imread(img_list[title])
        i+=1
        plt.subplot(cell+i)
        plt.title(title)
        plt.imshow(img, interpolation='nearest', cmap=plt.get_cmap('gray'))
    plt.suptitle(title)
    plt.show()

"""
ilist={'42':'images/test/42.jpg', '67':'images/test/67.jpg'}
showwithtitle(ilist)
"""