# object oriented programing

class Employee:
    co_salary = 1.04
    def __init__(self, first, last, pay) :
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{}{}'.format(self.first, self.last)
    
    def apply_co_salary(self):
        self.pay = int(self.pay * self.co_salary)
    
    # special method : representation, hàm mặc định trong class ==> dùng cho dev
    # Khi print ra thì nó sẽ đại diện bởi cấu trúc bên dưới thay vì print ra 1 object
    def __repr__(self):
        return f"Employee( {self.first}, {self.last}, {self.pay} )"
    
    # special method : Mặc định nếu có khai báo __str__ thì python sẽ sử dụng __str__ ==> dùng cho user 
    def __str__(self):
        return f"{self.fullname()} - {self.email}"
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp1 = Employee("Tran", "Thuan", 1000)
print(emp1) # Employee( Tran, Thuan, 1000 )

import datetime 

today = datetime.datetime.now()

# print readble format for date-time object
print(str(today)) 

# print the official format ò date-time object
print(repr(today))

emp2 = Employee("Tran", "Tu", 500)
print(emp1 + emp2)


# Ví dụ 3:
print(1+2) # 3 bản chất nó sẽ gọi int.__add__ được xây dựng sẵn
print(int.__add__(1,2)) 

# Ví dụ 4 __len__
print(len(emp1))