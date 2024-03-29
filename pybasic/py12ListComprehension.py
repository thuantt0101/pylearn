# LIST COMPREHENSION   ( COMPREHENSION = bao quát dễ hiểu)
# new_list[<action> for <item> in  <iterator> if <some condittion> ]
hello = "hello world"

# Bình thường ta sẽ loop vào hello để in ra 1 list như sau
for i in hello:
    print(i)
        # h
        # e
        # l
        # l
        # o

        # w
        # o
        # r
        # l
        # d    
    
# nhưng nếu chúng ta muốn đưa nó vào 1 cái list từng phần tử thì làm như sau
# đây chính là comprehension
print( [char for char in hello] )  # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

# In ra danh sách sô chẵn từ 0 đến 10
print( [ i for i in range(0, 10) if i % 2 == 0 ]) # [0, 2, 4, 6, 8]

# in ra list số lẽ từ  0 đến 10
print([i for i in range(0, 10) if i % 2 != 0]) # [1, 3, 5, 7, 9]


# Tính giá của sản phẩm
list_price_product = [100, 120, 200, 300]
VAT = 0.08

def price_product(price):
    return price* (1 + VAT)

print([ price_product(price) for price in list_price_product ] ) # [108.0, 129.60000000000002, 216.0, 324.0]
