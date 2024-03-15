import cv2

cv2.namedWindow('testImage')
cv2.namedWindow('testImage_G')
img = cv2.imread('MJ.png')
img_G = cv2.imread('MJ.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('testImage', img)
cv2.imshow('testImage_G', img_G)

cv2.imwrite('MJ_G.jpg', img_G)
cv2.imwrite('MJ_G_low.jpg', img_G, [int(cv2.IMWRITE_JPEG_QUALITY),50])

cv2.waitKey(0)
cv2.destroyAllWindows()