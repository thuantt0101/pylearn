import time

# Decorator don gian la dung ham trong ham

def square(numbers):
    result = []
    start = time.time()
    for number in numbers:
        result.append(number* number)
    
    end = time.time()
    print(f"This func took {(end - start)*1000} ms")
    return result

def cube(numbers):
    result = []
    start = time.time()
    for i in numbers:
        result.append(i*i*i)
    
    end = time.time()
    print(f"this func took {(end - start)*1000} ms")
    return result

# numbers = [1, 3, 4, 5, 6, 7]
# square(numbers)
# cube(numbers)

# nhu vi du tren thi ro rang code cua chung ta bi lap lại ở đoạn tính thời gian
# Cai thien bang Decorator

def cal_time(func):
    def timer(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"{func.__name__} took {(end-start)*1000} ms")
        return result
    return timer
    # timer return result, ta return timer de return result

# muốn pass hàm này vào cal_time ==> dùng decorator
@cal_time
def square2(numbers):
    result = []
    for number in numbers:
        result.append(number*number)    
    return result

@cal_time
def cube2(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result


numbers = [1, 3, 4, 5, 6, 7]
square2(numbers) # square2 took 0.0 ms
cube2(numbers) # cube2 took 0.0 ms

# ==> như vậy chúng ta đã pass thành công 2 hàm cube2 và square2 vào hàm cal_time , ta viết code ngắn hơn rồi.
# ==> Vì các process chạy riêng nhau ==> không dùng được biến global, với thread thì có thể dùng chung các biến.