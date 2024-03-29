# Object Oriented Grogramming
# Tính trừu tượng : từ 1 vật thể trong đời thực, chúng ta trừu tượng hóa nó lên và đưa nó vào trong 1 class, như Nhân viên ( Employee)
# Tính đóng gói : đưa hết tất cả các thuộc tính và phương thức vào trong class và bảo vệ chúng, thông thường bảo vệ bằng public, protected, private
    # protected thêm tiền tố "_" trước 
    # private thêm  tiền tố "__" trước
# Tính đa hình : cùng 1 tên hàm nhưng thằng con này nó lại cho ra kết quả khác, thằng con khác lại cho ra kết quả khác, chúng thực thi theo 1 cách khác

class Employee:
    __co_salary = 1.04
    _level  = "staff"

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{}{}'.format(self.first, self.last)
    
    def apply_co_salary(self):
        self.pay = int(self.pay * self.__co_salary)
        return self.pay
    
    def get_co_salary(self):
        return self.__co_salary


class Developer(Employee):
    def __init__(self, first, last, pay, pro_lang):
        super().__init__(first, last, pay)
        self.pro_lang = pro_lang
    
    # Tính đa hình
    def apply_co_salary(self):
        # return super().apply_co_salary()
        self.pay = int(self.pay * 1.2)
        return self.pay
    
emp1 = Employee("Thanh", "La", 400)


# Testing 1 : Tính đóng gói
# print(emp1.__co_salary) # Có thể lấy trực tiếp
print(emp1.get_co_salary()) # Lấy thông qua hàm ==> che giấu dữ liệu, kể cả các thằng kế thừa cũng sẽ k truy cập được
print(emp1._level) # Nếu protected thì thằng kế thừa có thể truy cập được, và cũng có thể truy cập trực tiếp như này

dev1 = Developer("Thanh",  "la", 400, "Python")
print(dev1.apply_co_salary())