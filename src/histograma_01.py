import cv2
import numpy as np
import matplotlib.pyplot as plt
import math as m
import navFunc as nf

img = cv2.imread('../figs/lena_color_256.tif',cv2.IMREAD_GRAYSCALE)

# Cria variavel do tipo struct (similar ao matlab):

Filter = nf.structtype()                

Filter.img = np.array(img)

Filter.imgSize = nf.structtype()
Filter.imgSize.lin, Filter.imgSize.col = Filter.img.shape

Hist = nf.calcHist(Filter.img)

#############################################################################################
########## Plot images:

########## Using matplotlib #################
plt.figure(1)
#plt.subplot(121)
plt.imshow(img, 'gray')
plt.title('Imagem Original')

#plt.subplot(122)
plt.figure(2)
plt.stem(Hist)
plt.title('Histograma da imagem')
plt.show()
