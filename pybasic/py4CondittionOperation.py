# Conditonal Operator
    # == 
    # != 
    # >=
    # <=
    # >
    # <

# Testing 1
print('a' > 'z')
print(ord('a'))
print(ord('z'))

# Testing 2
check = 8 == 9
print(check)

# Testing 3
a = 7 
b = 9
c = 15
res1 = a > b 
res2 = b < c 
res3 = a + b > c 
res = res1 or res2
print(res)
res = res1 and res2
print(res) #  False

res = not res
print(res) # True