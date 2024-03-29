# 1. for loop

for i in range(10):
    print(i)

print('------------------------------')

# range(start, stop, step)
for i in range(2, 10, 2):
    print(i) # 2 4 6 8

print('------------------------------')

for i in range(10, 0, -2):
    print(i) # 10 8 6 4 2

print('------------------------------')

list_sample = ["Thanh", 1233, 9.0, True]
for i in list_sample:
    print(i) # Thanh 1233 9.0 True


print('------------------------------')
for i in range(len(list_sample)):
    print(i, list_sample[i]) # 0 Thanh 1 1233 2 9.0 3 True

print('---------------while---------------')
# 2. while loop
i = 0
while i < 6:
    print(i)
    i += 1
 
i = 0
while True:
    if i > 7:
        print('the first number > 7 : ', i)        
        break
    else: 
        i += 1


print('---------------while continue---------------')
i = 0
while i < 5:        
    i += 1
    if i == 3:
        continue # ngay lap tuc bo qua dong o duoi va quay ve vong lap while
    print(i)