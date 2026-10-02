from ultralytics import YOLO
import cv2

URL = "http://10.187.9.47:8080/video"

model = YOLO("yolo26n.pt")
cap = cv2.VideoCapture(URL)

if not cap.isOpened():
    raise SystemExit("Can't open the stream. Check the URL and that the app's server is running.")

while True:
    ok, frame = cap.read()
    if not ok:
        print("Lost the stream")
        break
    res = cv2.resize(frame, (300,300))
    results = model(frame, device="cpu", imgsz=416, verbose=True)
    
    cv2.imshow("YOLO phone cam", results[0].plot())

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()