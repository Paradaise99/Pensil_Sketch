import cv2

img = cv2.imread('img/both.jpeg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inverted_gray_img = 255 - gray_img

blurred_img = cv2.GaussianBlur(inverted_gray_img, (21, 21), 0)

inverted_blurred_img = 255 - blurred_img

pencil_img = cv2.divide(gray_img, inverted_blurred_img, scale = 256.0)


cv2.imshow('Pencil Sketch', pencil_img)

cv2.waitKey(0)