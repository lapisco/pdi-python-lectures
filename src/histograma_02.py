import cv2
import numpy as np
import matplotlib.pyplot as plt
import math as m
import navFunc as nf

img = cv2.imread('../figs/lena_color_256.tif',cv2.IMREAD_GRAYSCALE)

# Using matplotlib
plt.figure(1)
plt.hist(img.ravel(),256,[0,256])

# Using opencv
plt.figure(2)
histr = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(histr)
plt.show()