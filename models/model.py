from ultralytics import YOLO


model = YOLO('models/best-5.pt')

def predict(img, conf):
    results = model(img, conf=conf)
    return results

