# HÀM ENUMERATE LÀ GÌ ? - REVERSE LIST!
# Cho phep nhap lan luot qua cac thanh phan cua 1 collection, trong khi no van giu index cua item hien tai
fruits = ["banana", "orange", "lemon", "watermelon", "apple"]

for idx, value  in enumerate(fruits):
    print(f"{idx} : {value}")
# 0 : banana
# 1 : orange    
# 2 : lemon     
# 3 : watermelon
# 4 : apple   
    
my_list = [1, 3, 4, 6, 10, 15]
reversed_my_list = list(reversed(my_list))
print(my_list) # [1, 3, 4, 6, 10, 15]
print(reversed_my_list) # [15, 10, 6, 4, 3, 1]

# hoac
print(my_list[::-1]) # [15, 10, 6, 4, 3, 1]

# sort nhung khong lam thay doi list ban dau
my_list = [1, 4, 3, 6, 10, 15]
sorted_my_list = sorted(my_list)
print(my_list) # [1, 4, 3, 6, 10, 15]
print(sorted_my_list) # [1, 3, 4, 6, 10, 15]