"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
"""

x = 'John'
print(type(x))

# Numeric Types
x = 5
print(type(x))

x = 5.4
print(type(x))

x = 5j #虛數
print(type(x))

# Sequence Types
x = ['a','b','c'] # 小筆記好寄用法List, 第一個字L為直的, 因此為[]
print(type(x))

x = ('a','b','c') 
print(type(x)) 

# List vs Tuple
# List 為串列, 可以被修改, 但tuple不行

numbers = range(1,10,2) #range(起始,終點,間距)

for number in numbers:
    print(number)
    pass

print(type(x))

x = {"name": 'John', "age":"20", "Male":"Man"} # Mapping Type
print(x["name"])
print(type(x))

# Set Types
    # set() 函式是python內建函式的其中一個，屬於比較基礎的函式。建立一個無序不重複元素集，可進行關係測試，刪除重複資料，還可以計算交集、差集、並集等。
    # set无序排序且不重复，是可变的，有add（），remove（）等方法。
    # frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。

x = {"apple", "banana", "cherry"} # Set
print(type(x))

a = set(('apple','banana'))
print(a)
a.add('z')
print(a)

b = frozenset('apple')
print(b)
# b.add('z') forzenest會凍結, 不能再被添加或刪除
# print(b)

# Boolean Type
x = bool(5)
print(x)
x = True
print(type(x))

# Binary Types
x = bytes(5)
print(x)
x = b"Hello"
print(x)
print(type(x))

x = bytearray(5)
print(x)
print(type(x))

x = memoryview(bytes(5))
print(x)

