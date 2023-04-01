
import cv2
image = cv2.imread('1.jpg')

# Chuyển đổi sang ảnh trắng đen
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Hiển thị ảnh trắng đen
# cv2.imshow('Grayscale Image', gray_image)
cv2.imwrite('test_lv1.jpg',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()