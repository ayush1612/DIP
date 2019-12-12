
import numpy as np
import cv2
from matplotlib import pyplot as plt
import pylab
from scipy import ndimage

img = cv2.imread('../pestimg.jpg',0)
rows,cols = img.shape

pixels = []
for i in range(rows):
    for j in range(cols):
        k = img[i,j]
      
        pixels.append(k)
            
print(pixels)