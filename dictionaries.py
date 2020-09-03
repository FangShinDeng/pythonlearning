# dictionaries 跟API接口是密不可分, 要好好學習

Person = {
    "name": "John",
    "age": "36",
    "male": "Man"
}

print(type(Person))

# 用for迴圈打印左邊參數內容

for data in Person:
    print(data) # name, age, male
    pass

for data in Person:
    print(Person[data]) # John, 36, Man
    pass

for data in Person.values():
    print(data)
    pass

print(Person.values()) # dict_values(['John', '36', 'Man'])

# 打印參數跟內容 用item!
for key,value in Person.items():
    print(key, value)
    print(key + ':' + value)
    pass
