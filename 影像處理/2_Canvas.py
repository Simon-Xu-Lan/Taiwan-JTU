# 顏色的保存方式 (0~255)
# 彩色的狀況是 RGB(紅色、綠色、藍色)，每一個顏色各為 (0~255)
# 如果是灰階就只會有一組數字(0~255)，0代表黑色，255代表白色
# 如果是黑白各半的灰色，那麼就是128

import cv2
import numpy

# 我要一張 300*200 的畫布，因為是灰階，所以每個點只要一個數字
# 因為每個數字的範圍0~255，剛好是2的8次方
canvas_g = numpy.ones((200,300,1), dtype="uint8")
canvas_g[:]=128
print(canvas_g)

cv2.namedWindow("test_g")
cv2.imshow("test_g", canvas_g)

# 這邊要用彩色的，所以每個點要三個數字組成
canvas_c = numpy.ones((200,300,3), dtype="uint8")
# 如果依照一般慣例，彩色會是RGB。
# 那照理來講下面這個設定(255,0,0)會是紅色
canvas_c[:]=(255,0,0)
# OpenCV 的顏色配置不是 RGB，是 BGR
# 所以(255,0,0)不是紅色，是藍色
print(canvas_c)

cv2.namedWindow("test_c")
cv2.imshow("test_c", canvas_c)
cv2.imwrite("bg.jpg", canvas_c)

cv2.waitKey(0)
cv2.destroyAllWindows()