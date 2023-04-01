import cv2

def zoning_image(img1, img2):

# Trừ ảnh thứ hai từ ảnh đầu tiên
    diff = cv2.absdiff(img1, img2)
# Chuyển đổi ảnh sang ảnh xám
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

# Ngưỡng ảnh để tách vật thể khỏi nền
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)

# Phân vùng ảnh để tìm các vật thể
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img1, contours, -1, (0, 0, 0), 2)
    cv2.drawContours(img2, contours, -1, (0, 0, 0), 2)
# Resize 2 ảnh cùng kích thước
    img1 = cv2.resize(img1, (int(img1.shape[1]/2), int(img1.shape[0]/2)))
    img2 = cv2.resize(img2, (int(img2.shape[1]/2), int(img2.shape[0]/2)))

# Ghép 2 ảnh theo chiều ngang
    result = cv2.hconcat([img1, img2])
# Hiển thị ảnh ghép    
    cv2.imshow('result1',result)

pass

# Đọc 2 ảnh đầu vào
img1 = cv2.imread('test_lv3.jpg')
img2 = cv2.imread('1.jpg')

# Gọi hàm zoning_image
zoning_image(img1,img2)

cv2.waitKey(0)
cv2.destroyAllWindows()