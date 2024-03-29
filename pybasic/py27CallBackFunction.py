# Call Back Function :
    # Là 1 hàm
    # Được gọi bởi 1 hàm khác

def get_value(param, value):
    call_back(value)

def call_back(value):
    print(f'My Value is: {value}')

get_value(param=call_back, value="Thanh") # My Value is: Thanh

# Các hàm bản chất nó chính là hàm call back : map, reduce, filter