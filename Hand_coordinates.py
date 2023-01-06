import cv2
import mediapipe as mp
mp_dr=mp.solutions.drawing_utils
mp_dr_syl=mp.solutions.drawing_styles
mphands=mp.solutions.hands

cap=cv2.VideoCapture(0)
hands=mphands.Hands()
while True:
    rt,video=cap.read()
    video=cv2.cvtColor(cv2.flip(video,1),cv2.COLOR_BGR2RGB)
    results=hands.process(video)
    video=cv2.cvtColor(video,cv2.COLOR_RGB2BGR)
    videoHeight, videoWidth, _ = video.shape
    co=[]
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_dr.draw_landmarks(
                video,
                hand_landmarks,
                mphands.HAND_CONNECTIONS)
        for point in mphands.HandLandmark:
                    if str(point) == "HandLandmark.WRIST":
                      normalizedLandmark = hand_landmarks.landmark[point]
                      pixelCoordinatesLandmark = mp_dr._normalized_to_pixel_coordinates(
                        normalizedLandmark.x,
                        normalizedLandmark.y,
                        videoWidth,videoHeight)

                      try:
                        co.append(list(pixelCoordinatesLandmark))
                      except:
                          continue
                    print(co)

    cv2.imshow("Hand Co-ordinates frame",video)
    if cv2.waitKey(1)==ord('q'):
        break

