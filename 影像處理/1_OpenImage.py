# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

# build a window named 'testImage'
cv2.namedWindow('testImage')
# Read image
img = cv2.imread('MJ.png')
# display image
cv2.imshow('testImage', img)

# wait for user to press key. 0 means at fastest speed to receive input.
cv2.waitKey(0)
# close the window
cv2.destroyAllWindows()