# BẾN TOÀN CỤC VÀ CỤC BỘ!
x = 100 # biến toàn cục
def example():
    x = 10 # cục bộ
    print(x)

print(x) # 100
example() # 10

#-----------------------global
y = 100
def example2():
    global y # cho phép biến toàn cục được thay đổi giá trị trong hàm cục bộ này.
    y = 10
    print(y)

example2() # 10
print(y)   # 10


#-----------------------
list_sample = [8]
def example3():
    global list_sample
    list_sample.append(9)
    print(list_sample)

print(list_sample)
example3()
