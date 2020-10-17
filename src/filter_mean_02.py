import cv2
import numpy as np
import matplotlib.pyplot as plt
import math as m
import navFunc as nf


img = cv2.imread('../figs/lena_color_256.tif', cv2.IMREAD_GRAYSCALE)

edges = cv2.Laplacian(img,cv2.CV_64F)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()