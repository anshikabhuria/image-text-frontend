import os
import uuid
from typing import Dict

from app.nlp.mission_parser import parse_mission

from app.cv.yolo_model import yolo_service
from app.nlp.mission_parser import parse_mission


UPLOAD_DIR = "storage/images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

db: Dict[int, dict] = {}
counter = 1


def save_image_and_text(image_file, text: str):
    global counter

    file_extension = image_file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{file_extension}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as f:
        f.write(image_file.file.read())

    # 🔹 NLP processing
    nlp_result = parse_mission(text)

    # YOLO
    vision_result = yolo_service.run_inference(file_path)

    record = {
        "id": counter,
        "text": text,
        "image_path": file_path,
        "nlp": nlp_result,
        "vision": vision_result
    }

    db[counter] = record
    counter += 1

    return record
