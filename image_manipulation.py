import random;
import cv2;
import numpy as np;
import matplotlib as mpl;

img = cv2.imread('./assets/Oladapo AYODEJI 1.jpg', -1);
B, G, R = cv2.split(img);
# cv2.imshow('B', B);
# cv2.imshow('G', G);
# cv2.imshow('R', R);

# print(img)
# print(type(img[0][0]))
# print(len(img.shape)) 

# for i in range(100):
#   for j in range(img.shape[1]):
#     img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# Copy part of an image i.e copy part of the array
tag = img[20:50, 25:50];
img[10:40, 15:40] = tag;
# print(tag);

cv2.imshow('image', img);
cv2.waitKey(0);
cv2.destroyAllWindows();

