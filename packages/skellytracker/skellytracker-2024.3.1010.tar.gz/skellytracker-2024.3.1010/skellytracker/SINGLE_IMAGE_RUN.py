import cv2
from pathlib import Path

from skellytracker.trackers.bright_point_tracker.brightest_point_tracker import BrightestPointTracker
from skellytracker.trackers.charuco_tracker.charuco_tracker import CharucoTracker
from skellytracker.trackers.mediapipe_tracker.mediapipe_holistic_tracker import MediapipeHolisticTracker
from skellytracker.trackers.yolo_tracker.yolo_tracker import YOLOPoseTracker

if __name__ == "__main__":
    demo_tracker = "brightest_point_tracker"
    image_path = Path("/Path/To/Your/Image.jpg")

    if demo_tracker == "brightest_point_tracker":
        BrightestPointTracker().image_demo(image_path=image_path)

    elif demo_tracker == "charuco_tracker":
        CharucoTracker(squaresX=7,
                       squaresY=5,
                       dictionary=cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)).image_demo(image_path=image_path)

    elif demo_tracker == "mediapipe_holistic_tracker":
        MediapipeHolisticTracker(model_complexity=2,
                                 min_detection_confidence=0.5,
                                 min_tracking_confidence=0.5,
                                 static_image_mode=False,
                                 smooth_landmarks=True).image_demo(image_path=image_path)

    elif demo_tracker == "yolo_tracker":
        YOLOPoseTracker(model_size="high_res").image_demo(image_path=image_path)