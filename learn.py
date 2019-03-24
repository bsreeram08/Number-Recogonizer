from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

image = Image.open('images/numbers/y0.5.png') # open image
imagearray=np.asarray(image) # open image as array

print(imagearray) #prints array [red,green,blue,alpha] alpha is transparancy

#image.show() # to show image

