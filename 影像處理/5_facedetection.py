import cv2

# 模型檔案的存放路徑
path = cv2.data.haarcascades+"haarcascade_frontalface_default.xml"
print(path)

# 宣告 OpenCV 的分類器
faceCascade = cv2.CascadeClassifier(path)

img = cv2.imread("person5.jpg")

# detectMultiScale 意思是畫面裡面可能會有多個物件
# scaleFactor 是搜索框放大率，minNeighbors指的是判斷雜訊的標準
# minSize 指的就是人臉的最小尺寸
faces = faceCascade.detectMultiScale(img, scaleFactor=1.1,
                                     minNeighbors=5, minSize=(30,30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
print(faces)

# 通常模型回報的資料格式跟 OpenCV 預測的畫圖參數不見得一樣
# OpenCV 的矩形參數是看左上角跟右下角
# 模型通常回報的參數是 (左上角X座標,左上角Y座標,矩形寬度,矩形高度)
count = 1
for (x,y,w,h) in faces:
    # 把偵測到的臉用方框進行標記
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
    # 把偵測的臉的部分圖片單獨取出來
    face = img[y:y+h,x:x+w]
    # 把取出的臉部圖片另外進行存檔
    filename = "face"+str(count)+".jpg"
    count = count + 1
    cv2.imwrite(filename, face)

cv2.namedWindow("test")
cv2.imshow("test", img)

cv2.waitKey(0)
cv2.destroyAllWindows()