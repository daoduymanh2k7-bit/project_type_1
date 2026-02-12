# Chương trình này là bản nâng cấp của green_screen ,có thể tùy chỉnh lower_green và upper_green bằng thanh trượt ,giúp tối thiểu viền xanh,có dùng gemeni hoàn thành trong ngày 12/2/2026
import cv2
import numpy as np

def nothing(x):
    # Hàm này bắt buộc phải có để Trackbar hoạt động, dù không làm gì cả
    pass

# 1. Đọc ảnh
# dán đường dẫn vào path
path = r"C:\Users\TGDD\Downloads\CV\person.jpg" # Đường dẫn ảnh của bạn
img = cv2.imread(path)

# Tạo cửa sổ chính có khả năng thay đổi kích thước
cv2.namedWindow('Bo Dieu Khien Tach Nen', cv2.WINDOW_NORMAL)

# 2. Tạo các thanh trượt (Trackbars)
# Cấu trúc: ("Tên thanh trượt", "Tên cửa sổ", Giá trị mặc định, Giá trị tối đa, Hàm gọi lại)

# --- LOWER (Cận dưới) ---
cv2.createTrackbar('Low H', 'Bo Dieu Khien Tach Nen', 50, 179, nothing) # H tối đa là 179
cv2.createTrackbar('Low S', 'Bo Dieu Khien Tach Nen', 120, 255, nothing)
cv2.createTrackbar('Low V', 'Bo Dieu Khien Tach Nen', 120, 255, nothing)

# --- UPPER (Cận trên) ---
cv2.createTrackbar('Up H', 'Bo Dieu Khien Tach Nen', 65, 179, nothing)
cv2.createTrackbar('Up S', 'Bo Dieu Khien Tach Nen', 255, 255, nothing)
cv2.createTrackbar('Up V', 'Bo Dieu Khien Tach Nen', 255, 255, nothing)

while True:
    # 3. Lấy giá trị hiện tại từ các thanh trượt
    l_h = cv2.getTrackbarPos('Low H', 'Bo Dieu Khien Tach Nen')
    l_s = cv2.getTrackbarPos('Low S', 'Bo Dieu Khien Tach Nen')
    l_v = cv2.getTrackbarPos('Low V', 'Bo Dieu Khien Tach Nen')

    u_h = cv2.getTrackbarPos('Up H', 'Bo Dieu Khien Tach Nen')
    u_s = cv2.getTrackbarPos('Up S', 'Bo Dieu Khien Tach Nen')
    u_v = cv2.getTrackbarPos('Up V', 'Bo Dieu Khien Tach Nen')

    # Tạo mảng Lower và Upper từ giá trị thanh trượt
    lower_green = np.array([l_h, l_s, l_v])
    upper_green = np.array([u_h, u_s, u_v])

    # 4. Xử lý ảnh (Tách nền)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask_inv = cv2.bitwise_not(mask)
    
    # Kết quả tách nền
    result = cv2.bitwise_and(img, img, mask=mask_inv)

    # 5. Ghép ảnh để hiển thị
    # Chuyển mask sang 3 kênh màu để ghép được với ảnh gốc
    mask_3ch = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    
    # Nối 3 ảnh theo chiều ngang
    stacked_img = np.hstack((img, mask_3ch, result))

    # Tùy chọn: Resize ảnh hiển thị nếu nó quá to tràn màn hình
    # Ở đây mình thu nhỏ còn 60% (scale = 0.6), bạn có thể chỉnh số này
    scale_percent = 0.6
    width = int(stacked_img.shape[1] * scale_percent)
    height = int(stacked_img.shape[0] * scale_percent)
    dim = (width, height)
    resized_show = cv2.resize(stacked_img, dim, interpolation = cv2.INTER_AREA)

    # 6. Hiển thị
    cv2.imshow('Bo Dieu Khien Tach Nen', resized_show)

    # Bấm phím 'q' hoặc 'ESC' để thoát
    key = cv2.waitKey(1)
    if key == 27 or key == ord('q'):
        break


cv2.destroyAllWindows()

