# Counter : đếm số lần xuất hiện
from collections import Counter
c =  Counter("Thanh dep trai")
print(c)

c2 = Counter(coca = 5, pepsi = 2)
print(list(c2.elements())) # ['coca', 'coca', 'coca', 'coca', 'coca', 'pepsi', 'pepsi']

c3 = Counter(a = 4, b = 5, c =7, d = -2)
d = ['a', 'c', 'a', 'd']
c3.subtract(d) 
print(c3) # Counter({'c': 6, 'b': 5, 'a': 2, 'd': -3})
c3.update(d) # chính là toán cộng
print(c3) # Counter({'c': 7, 'b': 5, 'a': 4, 'd': -2})
