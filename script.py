from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from statistics import mean
from functools import reduce
from collections import Counter #counts number of items in list and prints dictionary
import pyttsx3
engine = pyttsx3.init()
def say(text):
    engine.say("The number is " + str(text))
    engine.runAndWait()
def createExamples():
	numberArrayExamples = open('numArEx.txt','a')
	numbersWeHave = range(0,10)
	versionsWeHave = range(1,10)

	for eachnumbers in numbersWeHave:
		for eachversion in versionsWeHave:
			#print (str(eachnumbers)+'.'+str(eachversion))
			imagefilepath='images/numbers/' + (str(eachnumbers)+'.'+str(eachversion))+'.png'
			exampleimage = Image.open(imagefilepath)
			exampleimagearray=np.array(exampleimage)
			exampleimagearray1=str(exampleimagearray.tolist())
			linetowrite = str(eachnumbers)+'::'+exampleimagearray1+'\n'
			numberArrayExamples.write(linetowrite)

#createExamples() #function call to train the program for values
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
def whatNumberisthis(filepath):
	matchedArray=[]
	loadExamples = open('numArEx.txt','r').read()
	loadExamples = loadExamples.split('\n')
	image = Image.open(filepath)
	imagearray = np.array(image)
	imagearray1 = imagearray.tolist()

	inQuestion = str(imagearray1)

	for eachExamples in loadExamples:
		if(len(eachExamples)>3):
			splitExamples = eachExamples.split("::")
			currentElement = splitExamples[0]
			currentArray = splitExamples[1]

			eachpixelExample = currentArray.split('],')

			eachpixelinQuestion = inQuestion.split('],')

			element = 0
			while(element<len(eachpixelExample)):
				if eachpixelExample[element] == eachpixelinQuestion[element]:
					matchedArray.append(int(currentElement))
				element = element + 1
	#print (matchedArray)
	element = Counter(matchedArray)
	print(element)

	graphX=[]
	graphY=[]
	maxele=-1
	ele = 0
	for eachelement in element:
		print(eachelement)
		graphX.append(eachelement)
		#printnum =(str) (element[eachelement] / 10) + '%' 
		print(element[eachelement])
		if(maxele<element[eachelement]):
			maxele = element[eachelement]
			ele=eachelement
		#if (element[eachelement] > 4600):
		graphY.append(element[eachelement])	
	say (ele)
	say (ele)

	figure = plt.figure()
	axis1=plt.subplot2grid((4,4),(0,0),rowspan=1,colspan=4)
	axis2=plt.subplot2grid((4,4),(1,0),rowspan=1,colspan=4)

	axis1.imshow(imagearray)
	axis2.bar(graphX,graphY,align='center')

	xlocation = plt.MaxNLocator(12)
	axis2.xaxis.set_major_locator(xlocation)


	plt.ylim(400)   #limit y axis
	plt.show()



whatNumberisthis('images/test.png')


'''
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
'''
