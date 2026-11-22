import cv2
CAMERA_INDEX = 0
MIN_CONTOUR_AREA = 1000
MOTION_THRESHOLD = 30
WINDOW_NAME = "Motion Detection"
def main():
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        cap.release()
        raise RuntimeError("Could not access the camera.")
    try:
        success, previous_frame = cap.read()
        if not success:
            raise RuntimeError("Could not read the first frame.")
        previous_gray = cv2.cvtColor(
            previous_frame, cv2.COLOR_BGR2GRAY
        )
        while True:
            success, frame = cap.read()
            if not success:
                print("Failed to read a frame.")
                break
            gray = cv2.cvtColor(
                frame, cv2.COLOR_BGR2GRAY
            )
            # Compare consecutive frames
            difference = cv2.absdiff(previous_gray, gray)
            # Create a binary motion mask
            _, mask = cv2.threshold(
                difference,
                MOTION_THRESHOLD,
                255,
                cv2.THRESH_BINARY
            )
            # Find moving regions
            contours, _ = cv2.findContours(
                mask,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )
            for contour in contours:
                if cv2.contourArea(contour) > MIN_CONTOUR_AREA:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(
                        frame,
                        (x, y),
                        (x + w, y + h),
                        (0, 255, 0),
                        2
                    )
            cv2.imshow(WINDOW_NAME, frame)
            previous_gray = gray
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
