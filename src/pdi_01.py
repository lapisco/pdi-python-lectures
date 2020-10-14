import cv2 # OpenCV
import numpy as np # biblioteca para trablahar com arrays de forme eficiente
import matplotlib.pyplot as plt # biblioteca para plotar gráficos

img = cv2.imread('../figs/lena_color_256.tif')

print(img)
print(img.shape)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()