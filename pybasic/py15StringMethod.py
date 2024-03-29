# backslash \ : Dùng trước các ký tự đặc biệt
temp = 'I \'am Thuan I Study at \"UEH\" '
print(temp) # I 'am Thuan I Study at "UEH" 

# substring [start_idx, end_idx]  ==> [)
my_string = "Toi la Thuan depzai"
print(my_string[7: 12]) # Thuan
print(my_string[:12]) # Toi la Thuan

# strip() :  Return a copy of the string with leading and trailing whitespace removed.
my_string = " Toi la Thuan depzai "
print(my_string.strip())

# Loại bỏ T ở đầu
print(my_string.strip('T')) #  Toi la Thuan depzai

# split(): 
my_string = "Toi la Thuan depzai"
print(my_string.split()) # ['Toi', 'la', 'Thuan', 'depzai']

# uperp():
my_string = "Toi la Thuan depzai"
print(my_string.upper()) # TOI LA THUAN DEPZAI

# lower()
print(my_string.lower()) # toi la thuan depzai

# capitallize() : in hoa chu cai dau tien cua chuoi
print(my_string.capitalize()) # Toi la thuan depzai

# replace():
print(my_string.replace('depzai', 'Dep trai')) # Toi la Thuan Dep trai

# find() : find the position of given char
# nothing find: return -1
print(my_string.find('T')) # 0
print(my_string.find("Haha")) # -1

