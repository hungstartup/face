# author: Arun Ponnusamy
# website: https://www.arunponnusamy.com

# gender detection webcam example
# usage: python gender_detection_webcam.py 

# import necessary packages
import cvlib as cv
import cv2
import numpy as np

# open webcam
cap = cv2.VideoCapture(cv2.CAP_DSHOW)
h = cap.get( cv2.CAP_PROP_FRAME_HEIGHT )
w = cap.get( cv2.CAP_PROP_FRAME_WIDTH )
print("Camera H=%d, W=%d" % (h,w) )
# If I remove these two lines it works but is stuck at 640x480
cap.set( cv2.CAP_PROP_FRAME_HEIGHT, 10000 )
cap.set( cv2.CAP_PROP_FRAME_WIDTH, 10000 )
h = cap.get( cv2.CAP_PROP_FRAME_HEIGHT )
w = cap.get( cv2.CAP_PROP_FRAME_WIDTH )
print("Camera H=%d, W=%d" % (h,w) )

if not cap.isOpened():
    print("Could not open webcam")
    exit()
    

# loop through frames
while cap.isOpened():

    # read frame from webcam 
    status, frame = cap.read()

    if not status:
        print("Could not read frame")
        exit()

    # apply face detection
    face, confidence = cv.detect_face(frame)

    print(face)
    print(confidence)

    # loop through detected faces
    for idx, f in enumerate(face):
        
        (startX, startY) = f[0], f[1]
        (endX, endY) = f[2], f[3]

        # draw rectangle over face
        cv2.rectangle(frame, (startX,startY), (endX,endY), (0,255,0), 2)

        face_crop = np.copy(frame[startY:endY, startX:endX])

        # apply face detection    
        (label, confidence) = cv.detect_gender(face_crop)

        print(confidence)
        print(label)

        idx = np.argmax(confidence)
        label = label[idx]

        label = "{}: {:.2f}%".format(label, confidence[idx] * 100)

        Y = startY - 10 if startY - 10 > 10 else startY + 10

        # write detected gender and confidence percentage on top of face rectangle
        cv2.putText(frame, label, (startX,Y), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (0,255,0), 2)

    # display output
    cv2.imshow("Real-time gender detection", frame)

    # press "Q" to stop
    if cv2.waitKey(1000)  == 27:
        break
    
# release resources
cap.release()
cv2.destroyAllWindows()        
