# author: Arun Ponnusamy
# website: https://www.arunponnusamy.com

# gender detection video example
# usage: python gender_detection_video.py <video_file.mp4>

# import necessary packages
import cvlib as cv
import cv2
import numpy as np
import sys

# open video file
cap = cv2.VideoCapture(sys.argv[1])

if not cap.isOpened():
    print("Could not open video file")
    exit()
    

# loop through frames
while cap.isOpened():

    # read frame from video 
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

   
    if cv2.waitKey(1) == 27:
        break
    
# release resources
cap.release()
cv2.destroyAllWindows()        
