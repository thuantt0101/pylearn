# POSITIONAL , KEYWORDS ARGUMENT, *ARGS, **KWARGS LÀ GÌ ?

# Hàm có tham số bắt buộc
def add_func(x, y ):
    return x + y

print(add_func(1, 2)) # 3

# Hàm có tham số không bắt buộc
def add_func_3(x, y , z = None):
    add_num = None
    if z is None:
        add_num = x + y
    else:
        add_num = x + y + z
    
    return add_num

# Positional arguments
print(add_func_3(1, 2)) # 3
print(add_func_3(1, 2, 3)) # 6

# Keyword Arguments
print(add_func_3(x=5, z=10, y=2)) # 17


# *args: you can pass any number of positional arguments to your function
# args có thể truyền vào từ khác cũng được không vấn đề
def func_star_args(x, y , *args):
    print(x, y) 
    print(type(args)) # <class 'tuple'>
    for i in args:
        print(i)

func_star_args(10, 20, 88, "Hello")
func_star_args(10, 20) 
print('-----------------------')
# **kwargs : you can pass any number of keyword arguments to your function
def func_2star_args(x, y, **kwargs):
    print(x, y)
    print(type(kwargs)) # <class 'dict'>
    for i in kwargs:
        print(i, kwargs[i]) 

func_2star_args(10, 20, add_one = 20) # add_one 20


        
