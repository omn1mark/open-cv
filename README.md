
# Computer Vision with Python and OpenCV

A collection of computer vision experiments built using Python, OpenCV, and Ultralytics YOLO26.

This repository documents my progress from basic image processing to real-time object detection and tracking.

## Main Project: Real-Time Object Tracking

The main application uses a pretrained YOLO26 model to detect and track objects through a webcam.

### Features

- Real-time object detection using YOLO26
- Multi-object tracking with unique tracking IDs
- Bounding boxes and confidence scores
- Live FPS monitoring
- Real-time object counter
- Camera error handling and resource cleanup

### Technologies

- **Python** — Main programming language
- **OpenCV** — Video capture and image processing
- **Ultralytics YOLO26** — Object detection and tracking
- **NumPy** — Numerical operations used by the computer vision libraries

## Installation

Clone the repository:

```bash
git clone https://github.com/omn1mark/open-cv.git
cd open-cv
```

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the main object tracking application:

```bash
python "final project.py"
```

Allow access to your webcam if prompted.

Press **Q** while the video window is active to stop the application.

The YOLO26 model weights may be downloaded automatically on the first run.

## Additional Experiments

| File | Description |
|------|-------------|
| `camera_opener.py` | Basic webcam capture |
| `cv2 with objects.py` | Green color detection using HSV masks and contours |
| `green.py` | Basic color-based contour detection |
| `motion detect.py` | Motion detection using consecutive frame differences |
| `rectangles.py` | Drawing rectangles using OpenCV |
| `yolo.py` | Basic YOLO object detection |

## How It Works

The main application captures frames from a webcam and passes them to a pretrained YOLO26 model.

The model detects objects and uses tracking to associate detections across frames.

OpenCV displays the annotated video alongside the current object count and an approximate FPS measurement.

The motion detection experiment uses a different approach: it compares consecutive grayscale frames and highlights regions with significant pixel changes.

## Limitations

- Detection accuracy depends on lighting and image quality.
- Performance depends on the hardware.
- Motion detection may react to camera movement or lighting changes.
- Object tracking IDs are not guaranteed to remain consistent after an object disappears.
- The YOLO26 model is pretrained and has not been trained or fine-tuned in this project.

## Future Improvements

- Evaluate detection performance on sample videos
- Add configurable detection confidence thresholds
- Explore model fine-tuning on a custom dataset

## Author

Developed by [omn1mark](https://github.com/omn1mark) as part of my Python and computer vision learning journey.
