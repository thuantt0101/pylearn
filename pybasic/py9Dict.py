# Dictionary vài ngôn ngữ khác thì nó có tên là hash table hoặc là hash map

# syntax :
    # {}, {'key': value}
x = {}
print(type(x)) # <class 'dict'>

x = {'key': 1}
print(x) # {'key': 1}
print(x['key']) # 1

# add item
x[2] = 8
x['key2'] = 9
print(x) # {'key': 1, 2: 8, 'key2': 9}

# check key in x
print('key' in x) # True
print('key3' in x) # False

print(x.keys()) # dict_keys(['key', 2, 'key2'])
print(type(x.keys())) # <class 'dict_keys'>
print( list(x.keys())) # ['key', 2, 'key2']

print(x.values()) # dict_values([1, 8, 9]) 
print(list(x.values())) # [1, 8, 9]

# loop in a list
print('loop in a list')

for key,value in x.items():
    print(key, ':' , value) 
        # key : 1
        # 2 : 8
        # key2 : 9

for key in x.keys():
    print(key, ': ' , x[key] )
        # key :  1
        # 2 :  8
        # key2 :  9    

