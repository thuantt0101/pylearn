# Generator

def square_nums(list_num):
    return list(map(lambda x: x * x, list_num))

# list_nums = [1, 2, 3, 4]
# print(square_nums(list_nums))
# ---------------------------------------------

import random
import time

branches = ["BMW", "VinFast", "Toyota", "Mez", "Lexus", "Lambogini"]
engines = ["2.0", "1.6", "3.0", "v6", "v8"]

def car_list(num_people):
    
    result = []
    for i in range(num_people):
        car = {
            'id' : i,
            'name' : random.choice(branches),
            'engine': random.choice(engines)
        }
        result.append(car)

    return result

def car_generator(num_people):
    for i in range(num_people):
        car = {
            'id' : i,
            'name' : random.choice(branches),
            'engine': random.choice(engines)
        }
        yield car


t1 = time.time()
people = car_list(1000000)
t2 = time.time()
print(f'Took {t2-t1} Seconds') # Took 0.8072073459625244 Seconds

t1 = time.time()
people = car_generator(1000000)
t2 = time.time()
print(f'Took {t2-t1} Seconds') #  Took 0.05475926399230957 Seconds
print(next(people)) # {'id': 0, 'name': 'Toyota', 'engine': 'v6'}

# generator là một hàm trả về một đối tượng (iterator) mà chúng ta có thể lặp lại (một giá trị tại một thời điểm). 
# Chúng cũng tạo ra một đối tượng kiểu danh sách, nhưng bạn chỉ có thể duyệt qua các phần tử của generator một lần duy nhất vì generator không lưu dữ 
# liệu trong bộ nhớ mà cứ mỗi lần lặp thì chúng sẽ tạo phần tử tiếp theo trong dãy và trả về phần tử đó.
# ==> Nếu muốn dùng mà không cần lưu trữ dữ liệu ==> nên dùng generator nhanh chóng hơn