import cv2
import pytesseract
import numpy as np
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img=cv2.imread('1.jpg')
#cv2.imshow("image", img)
plt.imshow(img)
 
print(pytesseract.image_to_string(img))
print(pytesseract.image_to_boxes(img))

plt.waitforbuttonpress()
plt.close('all')
