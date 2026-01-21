from ultralytics import YOLO

if __name__ == '__main__':
    # YOLO modelini yükle
    model = YOLO('yolov8n.pt')

    # Modeli eğit
    model.train(data='dataset1.yaml', epochs=70, imgsz=640, batch=5)
