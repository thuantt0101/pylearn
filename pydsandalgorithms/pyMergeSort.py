def mergeSort(arr):

    if len(arr) > 1:

        # finding the middle index of the array
        middle_index = len(arr)//2

        # Left haft of the array
        l = arr[:middle_index]
        
        # Right haft of the array
        r = arr[middle_index:]

        # Sorting the first haft of the array
        mergeSort(l)

        # Sorting the second haft of the array
        mergeSort(r)

        # Initial index of left subarray
        i = 0

        # Initial index of the right subarray
        j = 0

        # Initial index of merged subarray
        k = 0

        # copy data to temp arrays l[] and r[]
        while i < len(l) and j < len(r):
            
            if l[i] < r[j]:
                arr[k] = l[i]
                i = i + 1
            else:
                arr[k] = r[j]
                j = j + 1
            
            k = k + 1
        
        # checking if there're some remaining elements
        while i < len(l):
            arr[k] = l[i]
            i = i + 1
            k = k + 1
        
        while j < len(r):
            arr[k] = r[j]
            j = j + 1
            k = k + 1

def mergeSort2(arr):

    if len(arr) > 1:

        middle = len(arr)//2

        left_array = arr[:middle]
        right_array = arr[middle:]

        mergeSort2(left_array)
        mergeSort2(right_array)

        # Initial index of left subarray
        i = 0

        # Initial index of the right subarray
        j = 0

        # Initial index of merged subarray
        k = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1

            k += 1

        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1
            k += 1
        
        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1
        
        






# Thuật toán merge sort hoạt động trên nguyên tắc chia để trị.
# Merge Sort chia nhỏ nhiều lần 1 mảng ( array ) thành 2 mảng con bằng nhau cho đến khi mỗi mảng con (subarray) 
# bao gồm 1 phần tử duy nhất, Cuối cùng tất cả các mảng con được hợp nhất để sắp xếp mảng kết quả

# ===========================================
 
# 16    12  15  13  19  17  11  18
# 16 12 15 13    |       19 17 11 18
# 16 12 | 15 13          19 17 | 11 18
# 12 16 | 13 15          17 19 | 11 18
# 12 13 15 16     | 11 17 18 19
# 11 12 13 15 16 17 18 19
if __name__ == "__main__":

    arr = [16, 12, 15, 13, 19, 17 ,11, 18, 10]
    mergeSort(arr)
    print(arr)

    print('--------------------')
    arr = [16, 12, 15, 13, 19, 17 ,11, 18, 10]
    mergeSort2(arr)
    print(arr)


