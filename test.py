import cv2

# Đọc ảnh vào
image = cv2.imread('1.jpg')

# Lấy kích thước ảnh ban đầu
height, width = image.shape[:2]

# Tọa độ và kích thước của vật thể cần phóng to
x, y, w, h = 100, 100, 200, 200

# Sử dụng hàm resize để phóng to vật thể
resized_object = cv2.resize(image[y:y+h, x:x+w], (int(width*1.5), int(height*1.5)))

# Tạo ảnh mới với kích thước ban đầu
resized_image = cv2.resize(image, (int(width*1.5), int(height*1.5)))

# Vẽ hình chữ nhật để đánh dấu vật thể
cv2.rectangle(resized_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('Original Image', image)
cv2.imshow('Resized Object', resized_object)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()