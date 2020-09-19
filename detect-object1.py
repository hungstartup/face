# author: Arun Ponnusamy
# website: https://www.arunponnusamy.com

# object detection webcam example
# usage: python object_detection_webcam.py

# right now YOLOv3 is being used for detecting objects.
# It's a heavy model to run on CPU. You might see the latency
# in output frames.
# To-Do: Add tiny YOLO for real time object detection

# import necessary packages
import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2

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

    # apply object detection
    bbox, label, conf = cv.detect_common_objects(frame)

    print(bbox, label, conf)

    # draw bounding box over detected objects
    out = draw_bbox(frame, bbox, label, conf)

    # display output
    cv2.imshow("Real-time object detection", out)

    # press "Q" to stop
    if cv2.waitKey(1) == 27:
        break
    
# release resources
cap.release()
cv2.destroyAllWindows()        
