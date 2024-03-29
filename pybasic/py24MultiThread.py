#  MULTI THREADING (ĐA LUỒNG) LÀ GÌ ?
# Ví dụ :
    # |_Nấu ắn là main thread
    #   |_ xuất hiện thêm Take care of baby
    #   |_ Phone call


import time

def square(numbers):
    print("Calculate square of numbers")
    for x in numbers:
        time.sleep(1)
        print(f"square: {x * x}")
    
def cube(numbers):
    print("Calculate cube of numbers")
    for x in numbers:
        time.sleep(1)
        print(f"square: {x * x * x}")

# start = time.time()
# arr = [1, 3, 5, 7, 9]
# square(arr)
# cube(arr)
# end = time.time()
# print(f"It took : {end - start}") # It took : 10.087596893310547
# ==> nếu chạy tuần tự thì nó tốn chúng ta hết 10s

import threading

start = time.time()
arr = [1, 3, 5, 7, 9]
thread1 = threading.Thread(target = square, args=(arr,))

thread2 = threading.Thread(target = cube, args= (arr, ))
# thread1 và thread 2 chạy hầu như là cùng lúc với nhau.
thread1.start()
thread2.start()

# join dùng để kết thúc ở thread chính, nếu không thì nó sẽ chạy luôn không cần đợi thread1 và thread2 kết thúc.
thread1.join()
thread2.join()

end = time.time()
print(f"It took : {end - start}")  # It took : 5.048942565917969

# ứng dụng thực tế : gõ văn bản là 1 thread, in văn bản là 1 thread trong microsoft word, word chính là process




