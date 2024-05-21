import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER #used to convert c data types in python format
from comtypes import CLSCTX_ALL #used to access the c/c++ components in python
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

############################
wCam, hCam = 640, 480
############################

# cap = cv2.VideoCapture(1) # 1 for external webcam
cap = cv2.VideoCapture(0) # 0 for webcam 
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.5)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPer = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw= False)

    
    # if len(lmList) != 0:
    #     print(lmList[4], lmList[8])

    if lmList is not None and len(lmList) >= 9:
        # print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2

        cv2.circle(img, (x1,y1), 15, (255,0,255), cv2.FILLED)
        cv2.circle(img, (x2,y2), 15, (255,0,255), cv2.FILLED)
        cv2.line(img, (x1,y1),(x2,y2),(255,0,255),3)
        cv2.circle(img, (cx,cy), 15, (255,255,0), cv2.FILLED)
        
        # euclidean distance (around 260 pixels is the max distace shown when i was lying on bed flat with left hand near my waist)
        length = math.hypot(abs(x2-x1), abs(y2-y1))
        # print(length)

        #manhattan distance (around 360 pixels is the max distace shown when i was lying on bed flat with left hand near my waist)
        # length = abs(x2 - x1) + abs(y2 - y1)
        # print(length)
        
        #chebyshev distance (around 240 pixels is the max distace shown when i was lying on bed flat with left hand near my waist)
        # length = max(abs(x2 - x1), abs(y2 - y1))
        # print(length) 


        # hand range was from 300 to 50
        # volume range was from -65 to 0 (-65 is lowest vol and 0 is highest vol)


        # write the new code here
        
        vol = np.interp(length, [50,300],[minVol, maxVol])
        volBar = np.interp(length, [50,300],[400, 150])
        volPer = np.interp(length, [50, 300], [0, 100])
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(img, (cx,cy), 15, (0,255,255), cv2.FILLED)

        cv2.rectangle(img, (50,150), (85,400), (0,255,0), 3)
        cv2.rectangle(img, (50, int(volBar)), (85,400), (0,255,0), cv2.FILLED)
        cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
            1, (255, 0, 0), 3)

            
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS:{int(fps)}', (40, 70), cv2.FONT_HERSHEY_COMPLEX,
    1, (255, 0, 0), 2 )

    cv2.imshow("Img", img)
    cv2.waitKey(1)