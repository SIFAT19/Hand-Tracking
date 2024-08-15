import cv2
import mediapipe as mp
import time
import handtrackmodule as htm



pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while True:
    success, img = cap.read()
    if not success:
        break
        
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[4])
            

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (18, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        
        # Show the image
    cv2.imshow("Image", img)
        
        # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()