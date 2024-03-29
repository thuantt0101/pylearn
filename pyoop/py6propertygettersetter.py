
# Object Oriented Programming
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # muốn biến func => property thì thêm decorator @property, đây như 1  dạng getter
        
    def fullname_func(self):
        return f'{self.brand} {self.model}'
    @property
    def fullname(self):
        return f'{self.brand} {self.model}'
    
    @fullname.setter
    def fullname(self, full_name):
        brand, model = full_name.split("-")
        self.brand = brand
        self.model = model

    @fullname.deleter
    def fullname(self):
        self.model = None
        self.brand = None
        print("fullname deleted!")
    

# Cách gọi theo hàm
car = Car("Vinfast", "luxa 2.0")
print(car.fullname_func())

# Cách gọi theo property
print(car.fullname)

# setter
car.fullname = "Vinfast-luxa 3.0"
print(car.brand)
print(car.model)

# delete
del car.fullname
print(car.brand, car.model)    
