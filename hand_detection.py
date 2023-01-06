import cv2
import mediapipe as mp

mp_dr=mp.solutions.drawing_utils
mphands=mp.solutions.hands
cap=cv2.VideoCapture(0)
hands=mphands.Hands()

while True:
    rt,video=cap.read()
    video=cv2.cvtColor(cv2.flip(video,1),cv2.COLOR_BGR2RGB)
    results=hands.process(video)
    video=cv2.cvtColor(video,cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_dr.draw_landmarks(
                video,
                hand_landmarks,
                mphands.HAND_CONNECTIONS)

    cv2.imshow("Hand detection frame",video)
    if cv2.waitKey(1)==ord('q'):
        break
