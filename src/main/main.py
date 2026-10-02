from ultralytics import YOLO

model = YOLO("yolo26n.pt")  # tải model phát hiện YOLO26n đã huấn luyện trước
results = model("https://ultralytics.com/images/bus.jpg", save=True)  # dự đoán và lưu ảnh đã chú thích
