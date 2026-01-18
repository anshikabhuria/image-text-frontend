from ultralytics import YOLO
from pathlib import Path

# Absolute path to weights
BASE_DIR = Path(__file__).resolve().parent
WEIGHTS_PATH = BASE_DIR / "weights" / "best.pt"

class YoloService:
    def __init__(self):
        self.model = YOLO(str(WEIGHTS_PATH))

    def run_inference(self, image_path: str, conf: float = 0.4):
        results = self.model(image_path, conf=conf)

        detections = []

        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            confidence = float(box.conf[0])
            label = self.model.names[cls_id]

            x_min, y_min, x_max, y_max = box.xyxy[0].tolist()

            detections.append({
                "species": label.capitalize(),   # important
                "bbox": [x_min, y_min, x_max, y_max],
                "confidence": confidence
            })

        return detections




# Singleton instance (loaded ONCE)
yolo_service = YoloService()
