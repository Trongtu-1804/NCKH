import cv2 # Import thư viện OpenCV

# Tạo bộ nhận diện khuôn mặt
faceCascade = cv2.CascadeClassifier("D:\\DATA_C_coppy\\Admin\\Documents\\Python\\tuhocxulyanh\\haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

img = cv2.imread('./face.jpg') # Đọc hình với OpenCV

img = cv2.resize(img, (480, 480)) # Thay đổi kích thước hình

# Quá trình nhận diện sẽ được thực hiện trên ảnh xám (Đen/Trắng)
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Chuyển ảnh màu sang ảnh xám

# Thực thi Face Detection
faces = faceCascade.detectMultiScale(
    grayImg,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Vẽ một hình tứ giác xung quanh những khuôn mặt phát hiện được. Vẽ trên ảnh màu.
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Face Detection', img) # Hiển thị kết quả ra màn hình
cv2.waitKey(0)
