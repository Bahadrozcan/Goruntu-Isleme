import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    kirmizialt = np.array([0, 100, 100])

    kirmiziüst = np.array([10, 255, 255])

    kirmizisinir = cv2.inRange(hsv, kirmizialt, kirmiziüst)

    kirmiziharic = cv2.bitwise_and(frame, frame, mask=kirmizisinir)

    cv2.imshow('Image', kirmiziharic)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()

cv2.destroyAllWindows()
