# SWITCH - CASE (CẤU TRÚC RẼ NHÁNH)


# switch case : thiet ke bang dict
def week(i):
    switcher  = {
        2 : "Monday",
        3 : "Tuesday",
        4 : "Webnesday",
        5 : "Thurday",
        6 : "Friday",
        7 : "Saturday",
        8 : "Sunday"
    }
    return switcher.get(i , "Invalid day")

print(week(2)) # Monday
print(week(9)) # Invalid day



