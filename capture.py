import cv2
import time

video = cv2.VideoCapture(0) # 0= first camera

a=0
while True:

    a=a+1
    check, frame = video.read()

    print(check)
    print(frame)

    cv2.imshow("Capturing video", frame)
    key = cv2.waitKey(1)

    if key == ord("Q") or key == ord("q"):
        break

print(a)
video.release()
cv2.destroyAllWindows()
