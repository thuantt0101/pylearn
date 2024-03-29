# Set
# Khai bao set : syntax : set([iterable]), iterable (không bắt buộc): đối tượng có thể là string, tuple, set, list, dictionary... hoặc đối tượng lặp iterator.
    # set()
    # {} phai co phan tu , neu khong co phan tu thi no chinh la dict

# Giá trị trả về từ set
# Nếu không truyền tham số, set() sẽ tạo ra một tập hợp trống.
# Nếu iterable được truyền dưới dạng tham số, nó sẽ tạo một tập hợp các phần tử trong iterable.

# ưu điểm của set, add và remove rất là nhanh, vì nó sử dụng hashtable ( ngâm cứu sau )
# ==> ưu điểm của set là tìm kiếm, remove, add nhanh 1 giá trị nào đó.


# Set print cac phan tu khong trung nhau
s = set( (8, 10, 7, 9, 10, 7) )
print(s) # {8, 9, 10, 7}
print(type(s)) 

# cách thứ 2 để khai báo 1 set
s2 = {4, 5, 6, 8, 8}
print(s2) # {8, 4, 5, 6} 
print(type(s2)) 


# set method
s.add(1)
print(s) # {1, 7, 8, 9, 10}

s.remove(8)
print(s) # {1, 7, 9, 10} 
print('union s1 & s2')
print(s.union(s2)) # {1, 4, 5, 6, 7, 8, 9, 10}

print('s differrent s2')
s = set( (8, 10, 7, 9, 10, 7) )
s2 = {4, 5, 6, 8, 8}
print(s.difference(s2)) # {9, 10, 7}

print('s intersection s2')
s = set( (8, 10, 7, 9, 10, 7) )
s2 = {4, 5, 6, 8, 8}
print(s.intersection(s2)) # {8}

print(0 in s) # False
print(9 in s) # True

s.clear()
print(s) # set()






