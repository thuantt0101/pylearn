# STRING FORMARTTING ( TRUYỀN BIẾN VÀO STRING)

# %, format(), f -string
my_string = "Toi la Thuan"
age = 18
money = 280.86
# %
hello = "Xin chao cac ban ! %s nam nay toi %i, toi co %.2f $" %( my_string, age, money)
print(hello) # Xin chao cac ban ! Toi la Thuan  nam nay toi 18 tuoi, toi dang co 280.860000 $


# format
hello = "Xin chao cac ban ! {} nam nay toi {}, toi co {:.2f} $".format(my_string, age, money) 
print(hello) # Xin chao cac ban ! Toi la Thuan nam nay toi 18, toi co 280.86 $

# f-string
hello = f"Xin chao cac ban ! {my_string} nam nay toi {age}, toi co {money:.2f} $"
print(hello)