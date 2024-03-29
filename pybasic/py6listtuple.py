# list/ tuples
list_test = ["Thanh", 3261, True]
print(len(list_test))

# Add item
list_test.append(33)
print(list_test) # ['Thanh', 3261, True, 33]

# Extend list
list_test.extend(["123", 456, 789])
print(list_test) # ['Thanh', 3261, True, 33, '123', 456, 789]

# Day ra 1 phan tu: 
list_test.pop() # pop(index) default final
print(list_test) # ['Thanh', 3261, True, 33, '123', 456]


# Truy cap phan tu so 0
print(list_test[0]) # Thanh

# Thau doi gia tri cua phan tu dau tien
list_test[0] = "Thuan"
print(list_test[0]) # Thuan

# luu y: van de a = b, va b thay doi thi a cung thay doi theo vi no dang tham chieu lan nhau
# -----------------------------------------------------------------
list_test = ["Thanh", 3261, True]
x = list_test
list_test[0] = "Thuan"
print(x, list_test) # ['Thuan', 3261, True] ['Thuan', 3261, True]

# Neu khong muon no tham chieu thi
list_test = ["Thanh", 3261, True]
x = list_test[:]
list_test[0] = "Thuan"
print(x, list_test) # ['Thanh', 3261, True] ['Thuan', 3261, True]
# -----------------------------------------------------------------

# tuples :
    # khong dung duoc append, pop, extend 
    # khong the thay doi gia tri trong cac phan tu
tuple_test = ("Thanh", 3261, True)

 