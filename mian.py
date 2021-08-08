import cv2

img_location = './img'

filename = 'both.jpeg'

img = cv2.imread(img_location + filename)

gray_img = cv2.imread(img, cv2.COLOR_BGR2GRAY)

inverted_gray_img = 255 - gray_img

blurred_img = cv2.GaussianBlur(inverted_gray_img, (21, 21), 0)

inverted_blurred_img = 255 - blurred_img

pencil_img = cv2.divide(gray_img, inverted_blurred_img, scale = 256.0)

cv2.imshow('Pencil Sketch', pencil_img)

cv2.waitKey('q')