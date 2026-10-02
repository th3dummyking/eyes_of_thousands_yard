from ultralytics import YOLO
import os 

model = YOLO("yolo26n.pt")  # tải model phát hiện YOLO26n đã huấn luyện trước
path = "C:/Users/dummyking/Documents/project/eyes_of_thousands/eyes_of_thousands_yard/src/data/test/image.png"

# results = model("https://ultralytics.com/images/bus.jpg", save=True)  # dự đoán và lưu ảnh đã chú thích

# results = model(path, save = True)

results = model.track(source="https://www.youtube.com/shorts/MolA2XwLZ0A", show=True, tracker="bytetrack.yaml")
