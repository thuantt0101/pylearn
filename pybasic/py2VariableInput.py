
# Declare Var, không đặt tên biến bắt đầu bằng ký tự đặc biêt, chữ số, không được trùng các keyword.
# Quy ước đặt tên biến : Tên biến có có 2 chữ thì cách nhau bằng "_" ví dụ input_name
# Biến nhận giá trị usr nhập vào luôn mặc định là string.
hello = "Xin Chào"
input_name = "hello"

# Có thể gáng lại giá trị của biến
input_name = 123


# Cho người dùng input thông tin vào 
input_name  = input("nhập tên của bạn :")
age = input("nhập tuổi của bạn")

print(f"tên của bạn{input_name}, tuổi của bạn {age}")