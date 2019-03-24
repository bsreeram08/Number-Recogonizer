from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from statistics import mean
from functools import reduce
#defining a function that turns the image to a black and white image( grayscale )
def threshold(imagearray):
	balancearray=[] #declaring a balance array
	newarray = imagearray
	for eachrow in imagearray:
		for eachpixel in eachrow:
			averagepixel = mean(eachpixel) #reduce(lambda x,y:x+y,eachpixel[:3])/len(eachpixel[:3])
			balancearray.append(averagepixel)
	balance = mean(balancearray)  #reduce(lambda x,y:x+y,balancearray/len(balancearray))
	for eachrow in newarray:
		for eachpixel in eachrow:
			if mean(eachpixel) > balance:
				eachpixel[0]=255
				eachpixel[1]=255
				eachpixel[2]=255
				eachpixel[3]=255
			else:
				eachpixel[0]=0
				eachpixel[1]=0
				eachpixel[2]=0
				eachpixel[3]=255
	return newarray

#opening images as array
image1 = Image.open('images/numbers/0.1.png')
imagearray1 =  np.array(image1)

image2 = Image.open('images/numbers/y0.4.png')
imagearray2 =  np.array(image2)

image3 = Image.open('images/numbers/y0.5.png')
imagearray3 =  np.array(image3)

image4 = Image.open('images/sentdex.png')
imagearray4 =  np.array(image4)

threshold(imagearray2)
threshold(imagearray3)
threshold(imagearray4)

#plotting images in a graph with rows8 and column 6

figure=plt.figure()
axis1 = plt.subplot2grid((8,6),(0,0),rowspan=4,colspan=3)
axis2 = plt.subplot2grid((8,6),(4,0),rowspan=4,colspan=3)
axis3 = plt.subplot2grid((8,6),(0,3),rowspan=4,colspan=3)
axis4 = plt.subplot2grid((8,6),(4,3),rowspan=4,colspan=3)

#showing images in axis

axis1.imshow(imagearray1)
axis2.imshow(imagearray2)
axis3.imshow(imagearray3)
axis4.imshow(imagearray4)

#displaying/printing axis

plt.show()

