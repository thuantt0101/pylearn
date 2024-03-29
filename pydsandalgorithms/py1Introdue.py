# Tại sao phải học cấu trúc dữ liệu và thuật toán
#==> 1.
#   Tìm kiếm dữ liệu: tìm kiếm 1 sản phẩm nào đó trong cả tỷ dữ liệu càng ngày càng lớn, khi dữ liệu càng lớn
#   dữ tìm dữ liệu sẽ trở nên chậm hơn
#==>2.
#   Tốc độ bộ xử lý : Tốc độ bộ xử lý mặc dù rất cao nhưng sẽ bị giới hạn nếu dữ liệu tăng lên hàng tỷ dữ liệu.
#==>3.
#   Vì hàng triệu người dùng có thể tìm kiếm dữ liệu đồng thời trên 1 máy chủ web, ngay cả máy chủ nhanh cũng bị
#   lỗi trong khi tìm kiếm.

# Ứng dụng của nó:

# 1. Tìm kiếm ( Search ) - Thuật toán tìm kiếm 1 mục trong cấu trúc dữ liệu
# 2. Sắp xếp (Sort)  - Thuật toán sắp xếp các mục theo 1 thứ tự nhất định
# 3. Chèn (Insert )     - Thuật toán chèn mục trong cấu trúc dữ liệu
# 4. Cập nhật ( Update )  - Thuật toán cập nhật một mục hiện có trong cấu trúc dữ liệu
# 5. Xóa (Delete)       - Thuật toán xóa một mục hiện có khỏi cấu trúc dữ liệu

# Các vấn đề sau có thể giải quyết bằng cách sử dụng Data Structure

# 1. Chuỗi số Fibonacci
# 2. Vấn đề Knapsack
# 3. Tháp hà nội
# 4. Tất cả các cặp đường đi ngắn nhất của Floyd-Warshall
# 5. Con đường ngắn nhất của Dijksra
# 6. Lập kế hoạch dự án


# Các đặc điểm nhận biết 1 thuật toán - không phải tất cả các thủ tục đều có thể được gọi là thuật toán, thuật toán phải có các đặc điểm sau:

# 1. Rõ ràng ( unambiguous) : Thuật toán phải rõ ràng và rõ ràng. Mỗi bước ( hoặc giai đoạn) của nó, input và output phải rõ ràng
# và chỉ dẫn đến 1 ý nghĩa

# 2. Input : Một thuật toán phải có 0 hoặc nhiều đầu vào được xác định rõ ràng
# 3. Output: Một thuật toán phải có 1 hoặc nhiều đàu ra được xác định rõ ràng và phải phù hợp với đầu ra mong muốn
# 4. Tính hữu hạn (Finiteness) : Thuật toán phải kết thúc sau một số bước hữu hạn
# 5. Tính khả thi ( Feasiability ) : Phải khả thi với các nguồn lực có sẵn (Tài nguyên - thiết bị hiện có)
# 6. Độc lập (Independent ) : Một thuật toán nến có hướng dẫn từng bước , điều này phải độc lập với bất kỳ code lập trình nào.


# Bài toán 1 :Thiết kế 1 thuật toán cộng 2 số và hiển thị kết quả

# Phương pháp mô tả 1:

# Bước 1 : Bắt đầu

# Bước 2: Khai báo 3 số nguyên a, b, c

# Bước 3: Xác định các giá trị của a, b

# Bước 4: Thêm các giá trị của a, b

# Bước 5: Lưu trữ đầu ra của bước 4 đến c

# Bước 6: in c

# Bước 7: Dừng.

def sum(first_number, second_number):
    result = first_number + second_number
    return result

print(sum(10, 20)) # 30



