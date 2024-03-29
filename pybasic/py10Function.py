# python basic - function

def func1():
    print('hello world, this is my first function')

func1() # hello world, this is my first function
print('----------------------------------------')


def func2(x, y ):
    print(x, y)

func2(10, 20) # 10 20
print('----------------------------------------')

def func3(x, y):
    return x + y

print(func3(1, 2)) # 3

def func4(x, y):
    return x + y, x * y
print('----------------------------------------')

x, y = func4(2, 4)
print(x, y) # 6 8
print('----------------------------------------')


#--------------------Tham số mặc định và tham số bắt buộc--------------------------
def func5(x, y, z = None):
    print(x, y, z)
    return x + y

print(func5(2, 3 , 'first call')) 
# out:
    # 2 3 first call
    # 5

