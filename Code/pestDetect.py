# author : Ayush Ujjwal
# Sem: 5th
# Topic : Pest Detection


import numpy as np
import cv2
from matplotlib import pyplot as plt
import pylab
from scipy import ndimage


def conversion():
    #os.system()
    image = cv2.imread('pestimg.jpg')
    
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    # cv2.imwrite('gray_image.png',gray_image)
    cv2.imwrite('hsv_image.png',hsv)
    cv2.imshow('color_image',image)
    # cv2.imshow('gray_image',gray_image) 
    cv2.imshow('hsvImage',hsv) 
    cv2.waitKey(0)                 # Waits forever for user to press any key
    cv2.destroyAllWindows()
    
def gaussianTest():
    image = cv2.imread('hsv_image.png')
    gaussian_kernel_x = cv2.getGaussianKernel(5,1) 
    gaussian_kernel_y = cv2.getGaussianKernel(5,1) 
    #converting to two dimensional kernel using matrix multiplication 
    gaussian_kernel = gaussian_kernel_x * gaussian_kernel_y.T 
    #you can also use cv2.GaussianBLurring(image,(shape of kernel),standard deviation) instead of cv2.filter2D 
    filtered_image = cv2.filter2D(image,-1,gaussian_kernel) 
    edges = cv2.Canny(image,100,200)
    cv2.imwrite('edges.png',edges)
    cv2.imshow('edges',edges)
    cv2.waitKey(0)                 # Waits forever for user to press any key
    cv2.destroyAllWindows()

def gaussian():
    image = cv2.imread('gray_image.png')
    cv2.getGaussianKernel(9,9)
    blur= cv2.GaussianBlur(image,(5,5),0)
    cv2.imwrite('blur.png',blur)
    cv2.imshow('blur',blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
def averagefilter():
    image=cv2.imread('blur.png')
    kernel=np.ones((5,5),np.float32)/25
    dst= cv2.filter2D(image,-1,kernel)
    plt.subplot(121),plt.imshow(image),plt.title('blur')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(dst),plt.title('averaged')
    plt.xticks([]), plt.yticks([])
    plt.show()
    cv2.imwrite('averaged.png',dst)



def segmentation():
    image = cv2.imread('pestimg.jpg')
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imwrite('thresh_image.jpg',thresh)
    cv2.imshow('thresh_image',thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

     # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 6)
    cv2.imshow('opening',thresh)
    cv2.waitKey(0)                 # Waits forever for user to press any key   
    cv2.destroyAllWindows()

     
    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=5)
    cv2.imshow('sure_bg',sure_bg)
    cv2.waitKey(0)                 # Waits forever for user to press any key   
    cv2.destroyAllWindows()
    print("No. of pests in the image: ")
    labelarray, particle_count = ndimage.measurements.label(sure_bg)
    # labelarray, particle_count = ndimage.measurements.label(opening)

    print(particle_count)
    #pylab.figure(1)
    #pylab.imshow(im_thresholded)
    #pylab.show()

def createHistogram():
    img = cv2.imread('pestimg.jpg')
    histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
  
    # show the plotting graph of an image 
    plt.plot(histr) 
    plt.show()

conversion()
gaussianTest()
# gaussian()
# averagefilter()
segmentation()
createHistogram()
