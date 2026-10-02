# eyes_of_thousands_yard

making a project
project vision is to make the thing able to look and detect what object is shown in:
            live camera from phones
            photos/albums and extract into mutiple outpputs


M1 : import yolo and test run
source :    https://docs.ultralytics.com/vi/quickstart

first to install model from online (using simple ver):  pip install -U ultralytics

![alt text](/img/readme/image.png)


CLI:    yolo predict model=yolo26n.pt
    install the model adn to start using the post-trained weigths


Trọng số yolo26n.pt đã huấn luyện trước sẽ tự động được tải xuống, model chạy trên hai ảnh mẫu đi kèm và lệnh sẽ in ra vị trí lưu kết quả đã chú thích, runs/detect/predict trong lần chạy đầu tiên. Trỏ source đến ảnh, video, thư mục, URL hoặc luồng của riêng bạn, hoặc đến webcam bằng source=0:

CLI:    yolo predict model=yolo26n.pt source=0 show=True

