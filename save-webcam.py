import numpy as np
import cv2

cap=cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"MJPG")
out = cv2.VideoWriter("output.avi", fourcc, 20.0,(680,800))

while(True):

    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)  == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
