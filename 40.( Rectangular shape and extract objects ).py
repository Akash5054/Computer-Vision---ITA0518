#Draw Rectangular shape and extract objects

import cv2
img = cv2.imread("msd1.jpg")
x, y = 700, 600
width, height = 700, 650
roi = img[y:y+height, x:x+width]
cv2.imshow("image",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
