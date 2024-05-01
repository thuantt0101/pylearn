from  enum import Enum, unique, Flag, auto

# Enum viết tắt của từ enumeration có nghĩa là phép liệt kê
#  tính năng này xác định một tập hợp các tên được liên kết với các hằng số như số, chuỗi, v.v. 
# Enum rất hữu ích để biểu diễn dữ liệu đại diện cho một tập hợp hữu hạn các trạng thái ví dụ như ngày trong tuần, tháng
# trong năm, …
# Thêm chỉ dẫn @unique vào trước định nghĩa lớp, đảm bảo rằng các phần tử trùng lặp không tồn tại trong enum.
# __members__ là thuộc tính chỉ đọc của lớp cung cấp ánh xạ từ tên đến các phần tử. Nó có thể sử dụng để lặp.

@unique
class Months(Enum):
    JANUARY = 1    
    FEBRUARY=2
    MARCH = 3
    APRIL=4
    MAY=5
    JUNE=6
    JULY=7
    AUGUST=8
    SEPTEMBER=9
    OCTOBER=10
    NOVEMBER=11
    DECEMBER=12


# Giá trị tự động
class Quarter(Enum):
  
    # overdrive method to convert number to string
    def _generate_next_value_(name, start, count, last_values):
      return "[" + name + "]"
     
    Q1 = auto()
    Q2 = auto()
    Q3 = auto()
    Q4 = auto()    

if __name__=="__main__":
    # In ra cac thanh vien cua emum

    # Su dung index
    print(Months(7))

    # Chi so bang ten
    print(Months['JULY'])

    # Thong qua ten
    print(Months.JULY)

    # Thong qua ten
    print(Months.JULY.name)

    # Thong qua value
    print(Months.JULY.value)

    # Cach 2 de tao 1 enum
    quanter1 = Enum('Q1', [ ('January', 1), ('February', 2), ('March', 3)] )
    print(quanter1)
    print(quanter1.February)
    print(quanter1.February.name)
    print(quanter1.February.value)

    print('-------------')
    # Su dung for voi enum
    for month in (Months):
        print(month)

    print('-------------------------')
    # Thuoc tinh  __members__
    for name, member in Months.__members__.items():
        print(name, member)
     

    print('-------------auto--------------')
    for qtr in Quarter:
        print(qtr.value)



