# Error handling.

# Nếu file không tồn tại --> gây chết chương trình
# f = open('files/abc.txt')
# print(f.read())

a = [1, 2, 3]
try:
    print(a[3])
except IndexError:
    print("an error occurred!")

try:
    print(9/0)
except ZeroDivisionError:
    print("Can not divide for zero")
finally :
    print("This line always run")

