import cv2
i=cv2.imread(r'C:\Users\sange\Downloads\pimple.jpg')
bblur=cv2.bilateralFilter(i,60,90.5,7)
cv2.imshow("original image",i)
cv2.imshow("BILATERAL FILTER", bblur)
cv2.imwrite("girl_bilated.png", bblur)
cv2.waitKey(0)
