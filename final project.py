import cv2
from ultralytics import YOLO
model = YOLO("yolo26n.pt")
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model.track(frame, persist=True)
    frame = results[0].plot()
    cv2.imshow("Object Tracking", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()