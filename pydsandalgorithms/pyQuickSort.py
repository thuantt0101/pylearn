# tham khảo https://topdev.vn/blog/thuat-toan-quick-sort-la-gi/

# Quicksort là 1 thuật toán sắp xếp, còn được gọi là thuật toán sắp xếp kiểu phân chia (Part Sort)
# Là 1 thuật toán hiệu quả dựa trên việc phân chia mảng dữ liệu thành các nhóm nhỏ hơn.

# Giải thích thuật toán

# Giải thuật sắp xếp nhanh chia mảng thành 2 phần bằng cách so sánh từng phần tử của mảng với 1 phần tử được
# gọi là phần tử chốt. Một mảng bao gồm các phần tử nhỏ hơn hoặc bằng phần tử chốt và một mảng bao gồm các
# phần tử lớn hơn phần tử chốt
# Quá trình phần chia này diễn ra cho đến khi độ dài của các mảng con đều bằng 1. Với phương pháp đệ quy ta
# có thể sắp xếp nhanh các mảng con sau khi kết thúc chương trình ta được 1 mảng được sắp xếp hoàn chỉnh.



# Kỹ thuật chọn phần tử chốt

# Kỹ thuật chọn phần tử chốt ảnh hưởng khá nhiều đến khả năng rơi vào các vòng lặp vô hạn đối với các
# trường hợp đặc biệt. Tốt nhất chọn  phần tử chốt nằm ở trung vị của danh sách. Khi đó sau log2(n) lần chia
# ta đạt được kích thước mảnh con bằng 1. Dưới đây là 1 số cách chọn phần tử chốt:

# 1. Chọn phần tử đứng đầu hoặc đứng cuối làm phần tử chốt.
# 2. Chọn phần tử đứng giữa danh sách làm phần tử chốt.
# 3. Chọn phần tử trung vị sau 3 phần tử đứng đầu, đứng giữa và đứng cuối làm phần tử chốt.
# 4. Chọn phần tử ngẫu nhiên làm phần tử chốt. Tuy nhiên cách này rất dễ dẫn đến khả năng rơi vào
# các trường hợp đặc biệt.

# Ví dụ: [10, 80, 30, 90, 40, 50, 70]
# Chọn 70 làm phần tử chốt 
#                           [10, 80, 30, 90, 40, 50, 70]
#  Partition  70                 ||                  ||                      
#                           [10, 30, 40, 50]        [90, 80] Partion arround 80
#  Partition 50                 ||                    || 
#                       [10, 30 ,40 ]                [90] 
#  Partition 40                ||
#                      [10, 30]
#  Partition 30             ||
#                       [10]

# Ý tưởng :

# 1. Chọn phân tử chốt
# 2. Khai báo 2 biến con trỏ để duyệt 2 phía của phân tử chốt
# 3. Biến bên trái trỏ đến từng phần tử mảng con bên trái của phần tử chốt
# 4. Biến bên phải trỏ đến từng phần tư con mảng bên phải phần tử chốt
# 5. Khi biến bên trái nhỏ hơn phần tử chốt thì nhảy sang phải
# 6. Khi biến bên phải nhỏ hơn phần tử chốt thì di chuyển sang trái
# 7. Nếu không xảy ra trường hợp 5 6 thì hoán đổi giá trị 2 biến trái phải
# 8. Nếu trái lớn hơn phải thì đây là giá trị chốt mới.

def max(list):
    result = None

    for i in arr:

        if result is None:
            result = i
        else: 
            result = i if i >= result else result

    return result


def min(list):

    result = None

    for i in list:

        if result is None:
            result = i
        else:
            result = i  if i <= result else result

    return result

def quickSort(numbers, left, right):
    
    if arr is None:
        return
    
    if left >= right:
        return
    
    middle = int(left + ( right - left ) / 2 )        

    pivot = arr[middle]
    i, j = left, right
    
    while (i <= j) :

        while (arr[i] < pivot):
             i = i + 1
        
        while( arr[j] > pivot ):
            j = j - 1

        if ( i <= j ):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i = i + 1
            j = j - 1        
    
    print('-----------------------------------')
    print(f"(i,j) = ( {i},{j} ) , left,right  = ( {left},{right} )")
    print(arr)
        
    if left < j:
        print(f"( left, j ) = ({left},{j})")
        quickSort(arr, left, j)

    if right > i:
        print(f"( i, right ) = ({i},{right})")
        quickSort(arr, i, right)

if __name__=="__main__":
    
    arr = [6, 2, 3, 4, 5, 9, 1]   

    left = 0
    right = len(arr) - 1

    quickSort(arr, left, right)
    print('--------------------')
    print(arr)











