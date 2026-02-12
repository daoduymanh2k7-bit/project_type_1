import cv2
import numpy as np

img = cv2.imread('C:\Users\TGDD\Downloads\mui.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)