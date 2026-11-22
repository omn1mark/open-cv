import time
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
    previous_time = time.perf_counter()
    fps = 0.0
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
            # Count objects detected in the current frame
            boxes = results[0].boxes
            object_count = len(boxes) if boxes is not None else 0
            # Calculate and smooth FPS
            current_time = time.perf_counter()
            elapsed = current_time - previous_time
            previous_time = current_time
            if elapsed > 0:
                current_fps = 1.0 / elapsed
                fps = (
                    current_fps if fps == 0.0
                    else 0.8 * fps + 0.2 * current_fps
                )
            # Draw an information panel
            cv2.rectangle(
                annotated_frame,
                (5, 5),
                (250, 85),
                (0, 0, 0),
                -1
            )
            cv2.putText(
                annotated_frame,
                f"FPS: {fps:.1f}",
                (15, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )
            cv2.putText(
                annotated_frame,
                f"Objects: {object_count}",
                (15, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )
            cv2.imshow(WINDOW_NAME, annotated_frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
