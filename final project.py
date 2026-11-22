import cv2
from ultralytics import YOLO
MODEL_PATH = "yolo26n.pt"
CAMERA_INDEX = 0
WINDOW_NAME = "YOLO26 Object Tracking"
def main():
    model = YOLO(MODEL_PATH)
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        cap.release()
        raise RuntimeError("Could not access the camera.")
    try:
        while True:
            success, frame = cap.read()
            if not success:
                print("Failed to read a frame.")
                break
            results = model.track(
                frame,
                persist=True,
                verbose=False
            )
            annotated_frame = results[0].plot()
            cv2.imshow(WINDOW_NAME, annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
