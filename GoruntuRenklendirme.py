# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 20:11:07 2024

@author: 90553
"""

import time
start_time = time.time()

import cv2
image = cv2.imread("data/00351v.jpg")
print("İlk görsel boyutu:",image.shape)
cv2.imshow("Ilk gorsel",image)
cv2.waitKey(0)


b = image[14:344,10:385][:, :, 0]
cv2.imshow("mavi",b)
cv2.waitKey(0)

g = image[345:675,10:385][:, :, 1]
cv2.imshow("yesil",g)
cv2.waitKey(0)

r = image[676:1006,10:385][:, :, 2]
cv2.imshow("kirmizi",r)
cv2.waitKey(0)


merged = cv2.merge([b,g,r])
print("Birleşen görsel boyutu", merged.shape)
cv2.imshow("Renkli gorsel",merged)
cv2.waitKey(0)

end_time= time.time()
total_time = end_time - start_time
print("Geçen zaman:", total_time, "saniye")
