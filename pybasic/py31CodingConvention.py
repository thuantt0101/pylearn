# CODING CONVENTION (PEP 8) - CÁCH ĐỂ CODE DỄ ĐỌC HƠN

# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbDhGNTJBNDNuSWZ4MGxObXhIU0hoSUJZR0Vud3xBQ3Jtc0tuUTBZU0pvdGdBR3RNRUlQYTZjR1ZaNWRjQ1hMY01xdmJUbTktR3ZwbVJPSWhseXJoemR2ZGkxbFJ2S2UtU0FxcEFuRW9YRUVNT016SXZfQ0tSVE03bnZQZU1VWG5WMEFDTDE0ckpIM2h5RlIwRER1NA&q=https%3A%2F%2Fwww.python.org%2Fdev%2Fpeps%2Fpep-0008%2F&v=L3EMzXKpI-w


# PEP 8
# Naming conventions

# Nếu tên biến có từ 2 từ trở lên thì ta nên cách nhau bởi underscore "_"
my_variable = "My name is Thuan"

# Nếu tên hàm có từ 2 từ trở lên thì ta cũng cách nhau bởi dấu underscore "_"
def my_func():
    pass

# Nếu là constant thì upper case
PI = 3.14

# Nếu tên class  có từ 2 từ trở lên thì viết liền nhau  và chỉ cần viết "upper case" chữ cái đầu tiên
class CoolBoy():
    pass

# Đặt tên có ý nghĩa
full_name = "Thuan Tran"
first_name, last_name = full_name.split()
print(f"my first name is {first_name}\n and my last name is {last_name}")


# Cách import thư viện, nếu như khác thư viện thì tách thành 2 dòng
import os
import flask

# Cách import module thuộc cùng 1 thư viện
from os  import environ, path

# Quy ước đặt tên file : không đặt tiếng việt có dấu, không dùng dấu cách 

# Có thể đặt tên có underscore nếu tên file có 2 từ trỏ lên và viết thương
# my_file.py

# Cũng có thể đặt tên file viết liền và viết " upper case" chữ cái đầu tiên
# Recommended this way.
# MyFile.py 

# tên số ít hoặc số nhiều
car ="Vinfast"
cars = ["Vinfast", "BMW"] # tên số nhiều có thể là 1 list


# Cài Extension để format code : Prettier - code format 
# control + f => format code 

def my_function_two(v_a,v_b):
    pass

# 1. Select the text you want to Prettify
# 2. CMD + Shift + P -> Format Selection