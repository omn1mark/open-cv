import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.rectangle(frame, (50, 50), (200, 400), (0, 255, 0), 15)
    cv2.rectangle(frame, (250, 100), (400, 300), (255, 0, 0), 3)
    cv2.rectangle(frame, (450, 200), (600, 400), (0, 0, 255), 2)
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()