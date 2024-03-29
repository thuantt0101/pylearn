# Map, Filter, Reduce

# map(func, *iterables) : tranform object with function
list_temp = [ 7, 8, 9, 12]

def sum(x):
    return x + 2

res = map(sum, list_temp) 
print(type(res)) # <class 'map'>
print(list(res)) # [9, 10, 11, 14]

res2 = map(lambda x: x + 3, list_temp)
print(list(res2)) # [10, 11, 12, 15]


# filter(func, *iterables): filter object which you want
res3 = filter( lambda x: x%2==0, list_temp)
print(type(res3)) # <class 'filter'>
print(list(res3)) # [8, 12]
print([x for x in list_temp if x%2==0]) # [8, 12] cùng kết quả mong muốn nếu dung "list comprehension"


# reduce(func, object): return single value, func get 2 arg
list_temp.append(15)
list_temp.append(21)
list_temp.append(42)
print(list_temp) # [7, 8, 9, 12, 15, 21, 42

from functools import reduce

# lấy ra phần tử bé nhất
print(reduce(lambda x, y: x if x < y else y, list_temp )) # 7
# lấy phần tử lớn nhất
print(reduce(lambda x, y: x if x > y else y, list_temp))



