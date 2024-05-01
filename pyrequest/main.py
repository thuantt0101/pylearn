import requests

# syntax : requests.methodname(params)

# https://requests.readthedocs.io/en/latest/

x = requests.get('https://w3schools.com/python/demopage.htm')
print(type(x))
print(x.text)




