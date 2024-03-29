# default dict
from collections import defaultdict

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : "1964"
 }

# Nếu ta print 1 thuộc tính mà không có trong dict thì sẽ báo lỗi
# print(thisdict["color"])

def define_value():
    return "not init"
thisdict = defaultdict(define_value)
thisdict ["brand"] = "Ford"
thisdict["model"] = "Mustang"
thisdict["year"] = 1964
print(thisdict["color"]) # not init

# Khai báo dict kiểu int : mặc định nếu k có thuộc tính nó trả về 0
thisdict = defaultdict(int)
print(thisdict[0]) # 0
print(thisdict["brand"]) # 0


