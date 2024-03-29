import multiprocessing 
import time

# Đa tiến trình
def cal_time(func):        
    def timer(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"{func.__name__} took {(end - start) * 1000} ms")
        return result
    return timer

def square(numbers):
    time.sleep(10)
    result = []
    for number in numbers:
        result.append(number * number)
    return result

def cube(numbers):
    time.sleep(10)
    result = []
    for number in numbers:
        result.append(number * number * number)    
    return result

if __name__=="__main__":
    arr = [1, 3, 5, 7, 9]
    process1 = multiprocessing.Process(target=square, args= (arr,) )
    process2 = multiprocessing.Process(target=cube, args =(arr,) )

    process1.start()
    process2.start()

    process1.join()
    process2.join()
    
    print("Done process !")

# mở [ task manager để xem process ]  vào task detail để xem các process xuất hiện.
# lưu ý : nếu dùng đa tiến trình thì không thể dùng decorator được.


