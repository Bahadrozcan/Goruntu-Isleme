import cv2
import numpy as np

pirinc = cv2.imread("pirinc2.jpeg")

gri_tonlama = cv2.cvtColor(pirinc, cv2.COLOR_BGR2GRAY)

_, esik = cv2.threshold(gri_tonlama, 100, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(esik, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

adet = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 100:  
        cv2.drawContours(pirinc, [contour], 0, (0, 0,255), 2)  
        adet += 1

print("Pirinç Sayısı:", adet)

cv2.imshow("Gercek Goruntu", pirinc)
cv2.imshow("Esiklenmis Goruntu", esik)
cv2.waitKey(0)
cv2.destroyAllWindows()
