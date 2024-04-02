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
#                           [10, 30, 40, 50]        [90, 80] Partion arround 80  ==> []
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

# https://www.youtube.com/watch?v=r637qlJvtlk
# The algorithm finished when all the numbers have been considered as pivots.

# 13, 21, 15, 3, |12|, 9, 14, 7, 6
# 3, 9, |7|, 6, 12, 13, 21, |15|, 14 
# 3, |6|, 7, |9|, 12, 13, |14|, 15, |21|
# |3|, 6, 7, 9, 12, |13|, 14, 15, 21
# 3, 6, 7, 9, 12, 13, 14, 15, 21

# 1. Chọn phần tử chốt ( pivot )
# 2. khai báo 2 biến con trỏ để duyệt 2 phía của phần tử chôt
# 3. Biến bên trái trỏ đến từng phần tử mảng con bên trái của phần tử chốt
# 4. Biến bên phải trỏ đến từng phần tử mảng con bên phải của phần tử chốt
# 5. Cho đến khi biến bên trái nhỏ hơn phần tử chốt thì nhảy sang bên phải
# 6. Cho đến khi biến bên phải nhỏ hơn phần tử chốt thì nhảy sang trái
# 7. Nếu 5,6 không xảy ra thì swap 2 giá trị trái phải
# 8. Nếu trái lớn hơn phải thì đây là giá trị chốt mới.


# Sắp xếp giảm dần
def quickSortDesc(numbers, left, right):

    if numbers is None:
        return
    
    # Duyệt đến khi còn 1 phần tử left = right
    if left >= right:
        return
    
    # Chọn phần tử chốt là phần tử đứng giữa từ left đến right    
    middle =   int( left + (right - left)/2)
    pivot = numbers[middle]

    # Khai báo con trỏ bên trái và bên phải 
    i, j = left, right

    # Tiếp tục duyệt cho đến khi index trái = index phải
    while( i <= j ):

        # duyệt vào mảng con bên trái, nếu giá trị của phần tử được duyệt > giá trị pivot thì break ra để tiến hành swap sang bên phải
        while (numbers[i] > pivot):
            i = i + 1

        # duyệt vào mảng con bên phải, nếu giá trị phần tử được duyệt < pivot thì break để tiến hành swap sang trái
        while (numbers[j] < pivot):
            j = j - 1

        # tiến hành swap
        if i <= j:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

            # duyệt đến phần tử tiếp theo bên trái
            i = i + 1

            # duyệt đến phần tử tiếp theo bên phải
            j = j - 1

    # Tiếp tục sắp xếp mảng bên trái từ vị trí left đến vị trí j mới            
    if left < j : 
        quickSortDesc(numbers, left, j)
    
    # Tiếp tục sắp xếp mảng bên phải từ vị trí i mới đến vị trí right
    if right > i:
        quickSortDesc(numbers, i, right)
                  
# pivot is middle of list
def quickSortAsc(numbers, left, right):
    
    if numbers is None:
        return
    
    if left >= right:
        return
    
    middle = int(left + ( right - left ) / 2 )        

    pivot = arr[middle]
    i, j = left, right
    
    while (i <= j) :
        
        print(f"before first loop : (i, j) = ({i}, {j}), pivot = {pivot}")            

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
                
    if left < j:
        print(f"( left, j ) = ({left},{j})")
        quickSortAsc(arr, left, j)

    if right > i:
        print(f"( i, right ) = ({i},{right})")
        quickSortAsc(arr, i, right)

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

def quickSort(numbers, left, right, typeOrder = None):

    # Nếu danh sách null thì ta return
    if numbers is None:
        return

    # Dừng lại nếu danh sách chỉ còn 1 phần tử
    if left >= right:
        return
    
    # Chọn phần tử chốt ( pivot )
    middle = int( left + (right - left)/ 2)
    pivot = numbers[middle]
    i, j = left, right

    # Partition
    while ( i <= j):


        if typeOrder is None:

            # Duyệt vào mảng bên trái partition        
            while (numbers[i] < pivot ) :
                i = i + 1
            
            # Duyệt vào phần tử mảng con bên phải partition
            while numbers[j] > pivot:
                j = j - 1
        elif typeOrder == 'Desc':

            while numbers[i] > pivot:
                i += 1

            while numbers[j] < pivot:
                j += -1 
        
        # Tiến hành swap
        if i <= j:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

            # duyệt vào các phần tử tiếp theo
            i += 1
            j += -1        
            

if __name__=="__main__":
    
    arr = [3, 6, 7, 9, 12, 13, 14, 15, 21]      
    left = 0
    right = len(arr) - 1
        
    quickSort(arr, left, right)    
    print(arr)

    arr = [3, 6, 7, 9, 12, 13, 14, 15, 21]      
    left = 0
    right = len(arr) - 1
        
    quickSort(arr, left, right, 'Desc')    
    print(arr)








