# r , for reading
# w , for writing
# a , for appending
# r+ , for both reading and writing.

file = open('files/test.txt', 'r')

print(type(file)) # <class '_io.TextIOWrapper'>

# read() : khi đọc bằng file.read() : mặc định con trỏ nó sẽ trỏ đến cuối file, nên nếu chúng ta gọi lần 2 thì sẽ k lấy ra được gì
print(file.read())
# output
    # My name is Thuan
    # nice too meet you!!
print('in lan 2')
print(file.read()) # no more line to print

print('close file')
file.close()

print('reopen the file')
file = open('files/test.txt', 'r')

print('in lan 3')
print(file.read())
file.close()


print('----------------readline()-----------------------')
# đọc từng dòng và con trỏ đi đến hết dòng hiện hành
f = open('files/test.txt', 'r')
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

print('----------------readlines()-----------------------')
f = open('files/test.txt', 'r')
for idx, value in  enumerate(f.readlines()):
    print(f"index: {idx}, value : {value}")

f.close()

print('----------------mode write-----------------------')
f = open('files/test.txt', 'w')
f.write("i am 33 years old \n")
f.close()
f = open('files/test.txt', 'r')
print(f.read())
f.close()


print('----------------mode append-----------------------')
# khong cần close nếu dùng with
with open('files/test.txt', 'a') as f:
    f.write('how old are you?')

with open('files/test.txt', 'r') as f:
    print(f.read())














