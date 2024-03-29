
# Trong cách tiếp cận phân chia & chinh phục( devide and conquer ) bài toán được chia thành bài toán con nhỏ hơn
# và sau mỗi bài toán được giải quyết 1 cách độc lập, Khi chúng ta tiếp tục chia các bài toán con thành bài toán nhỏ hơn
# cuối cùng chúng ta có thể đạt đến 1 giai đoạn không thể phân chia được nữa . Những vấn đề con nhỏ nhất có thể có "nguyên tử"
# (phân số ) được giải quyết. Lời giải của tất cả các bài toán con cuối cùng được hợp nhất ( merge )để có được lời giải
# cho bài toán ban đầu

#               a b c d e f g h i j                           => problem                 
#   Divide      a b c d e f g h i j                           => sub-problem
#   Conquer     A B C D E F G H I J                           => Sub-solution
#   Merge       A B C D E F G H I J                           => Solution

# Ví dụ các thuật toán máy tính sau đây dựa trên cách tiếp cận lập trình chia để trị

# 1.  Hợp nhất sắp xếp ( Merge sort)
# 2.  Sắp xếp nhanh (Quick Sort)
# 3.  Tìm kiếm nhị phân (Binary Search )
# 4.  Phép nhân ma trận của Strassen (Strassen’s Matrix Multiplication)
# 5.  Cặp gần nhất ( điểm ) (Closest pair (points))

# Có nhiều cách khác nhau có sẵn để giải quyết bất kỳ vấn đề máy tính nào, nhưng những cách được đề cập là một ví dụ điển hình về phương pháp chia và chinh phục.