import cv2
cap = cv2.VideoCapture(0)
ret, previous = cap.read()
previous = cv2.cvtColor(previous, cv2.COLOR_BGR2GRAY)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(previous, gray)
    _, mask = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Camera", frame)
    previous = gray
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()