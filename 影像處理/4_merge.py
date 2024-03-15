import cv2, glob
import numpy

#利用glob套件掃描固定資料夾中有那些副檔名是jpg的檔案
# MAC
file_list = glob.glob("numbers/*.jpg")
# Windows PC
# file_list = glob.glob("numbers\\*.jpg")
#可以知道資料夾裡面有幾張圖
file_num=len(file_list)
print(file_list, file_num)

#把其中一張圖讀取進Python，並且計算寬&高
file_1 = cv2.imread(file_list[0])
file_h =file_1.shape[0]
file_w =file_1.shape[1]

#利用前面算出來的寬與高的資訊，建立一張符合大小的背景畫布
canvas = numpy.ones((file_h,file_w*file_num), dtype = "uint8")
#把背景顏色設定成白色
canvas[:] = 255

#enumerate與一般迴圈不同的地方，在於它會同時回傳index
for index, file in enumerate(file_list):
    #將檔案一個個讀入Python
    # 0：Gray　Scale 灰色, 1：RGB scale 彩色
    m_data = cv2.imread(file,0)
    #按照檔案內容，把數值複製到背景畫布中
    for row in range(file_h):
        for col in range(file_w):
            #為了避免圖片疊再一起，所以按照index往右邊平移
            canvas[row][col+file_w*index]=m_data[row][col]

cv2.namedWindow("Canvas")
cv2.imshow("Canvas", canvas)
cv2.imwrite("numbers\\merge.jpg", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()