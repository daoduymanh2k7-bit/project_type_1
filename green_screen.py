# Chương trình này là chương trình dùng để tách nhân vật ra khỏi phông xanh,thực hiện từ 8/2/2026 - 12/2/2026
import cv2
import numpy as np

# Đọc ảnh
# Gắn địa chỉ ảnh vào path
path = r"C:\Users\TGDD\Downloads\CV\person.jpg"
img = cv2.imread(path)

if img is not None:
    # Chuyển sang HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Tạo mặt nạ để lọc màu xanh
    lower_green = np.array([45, 120, 120])
    upper_green = np.array([75, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    # Tách nhân vật ra khỏi nền
    mask_inv = cv2.bitwise_not(mask)
    result = cv2.bitwise_and(img, img, mask=mask_inv)
    
    # Hiển thị để kiểm tra trực tiếp
    cv2.imshow('Result', result)
    cv2.imshow('goc',img)
    cv2.imshow('mask',mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

