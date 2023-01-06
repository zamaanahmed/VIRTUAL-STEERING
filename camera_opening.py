import cv2 

cap=cv2.VideoCapture(0)
while True:
    rt,vid=cap.read()
    cv2.imshow("Frame",vid)
    if cv2.waitKey(1)==ord('q'):
        break
