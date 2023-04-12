import cv2
import numpy as np

cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)   # Can resize If u want
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))


while True:
    cam.set(cv2.CAP_PROP_POS_FRAMES, 0)
    ret, frame = cam.read()
    if ret:
        resized_frame = cv2.resize(frame, (640, 480)) # resize

        out.write(resized_frame)
    frame = cv2.GaussianBlur(frame, (5, 5), 0) 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_yellow = np.array([18, 94, 149]) #avg
    high_yellow = np.array([48, 255, 255])
    mask = cv2.inRange(hsv, low_yellow, high_yellow)
    lines = cv2.HoughLinesP(mask, 1, np.pi/180, 50, minLineLength=10,maxLineGap=50)
    kernel = np.ones((5, 5), np.uint8)

    if lines is not None:
        for line in lines:
            x1, y1 , x2, y2 = line[0]
            cv2.line(frame, (x1,y1),(x2,y2),(0,255,0),5) # u can edit color and thcik

    if not ret:
        break

    cv2.resizeWindow('frame', 800, 600)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == 27:
        break