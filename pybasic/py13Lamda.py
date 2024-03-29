# Lamda function: small (one line) anonymous function : hàm ẩn danh
# Lamda arguments : expression

# lambda voi 1 argument
test_lambda = lambda x : x + 48
print(test_lambda(69))


# sắp xếp list
list_sample = [-1, -5, -6, 0, 1, 2, 3, 4]
    
# theo cách thông thường
print(sorted(list_sample)) # [-6, -5, -1, 0, 1, 2, 3, 4]

# sắp xếp theo đối trọng - sắp xếp khác biệt hơn 1 xíu
print(sorted(list_sample, key= lambda x: abs(x))) # [0, -1, 1, 2, 3, 4, -5, -6]


list_coor = [(0, 4), (-5, 6) , (7, 10), (1, 5)]
print(sorted(list_coor)) # [(-5, 6), (0, 4), (1, 5), (7, 10)] ==> lấy phần tử đầu tiên để sắp xếp
print(sorted(list_coor, key = lambda x: x[1])) # [(0, 4), (1, 5), (-5, 6), (7, 10)] sắp xếp theo phần tử thứ 2 của list



