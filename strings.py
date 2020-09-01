x = 'hello world'
print(x)

# 多行字串, 透過三個單引號或雙引號
x = """
1. 內容1,
2. 內容2,
3. 內容3,
"""
print(x)

# Slice 取出特定字串內的內容
x = 'Hello world'
print(x[0]) # 'H'
print(x[3:6]) # 'lo '
print(x[6:3]) # 'NULL'
# Nagative Slice
print(x[-3]) # 'r'
print(x[-2:-5]) # 'NULL'
print(x[-5:-2]) # 'wor'

# String Length 取長度
x = len('hello world')
print(x)

# Strip 去除頭尾空格
x = ' A B C D EEE FG    '
print(x.strip())

# 將字體變成大寫小寫
x = 'Hello world'
print(x.upper())
print(x.lower())

# 取代 
G = x.replace('H','G')
print(G)

# 分割 split
x = 'Hello, world'
G = x.split(',')
print(G)
print(type(G)) # <class 'list'>

# 檢查字串
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x) # True
y = "an" in txt
print(y) # False

# 字串跟數字不能一起用, 能用format來進行
x = 10
y = 'John'
# print(x+y) # error

# format 基礎用法
age = 10
txt = "My name is John and age is {}"
print(txt.format(age)) 

# format 進階用法
name = 'John'
age = 30
male = True
txt = "My name is {} and age is {}. ({}), I'm a man"
txt = txt.format(name, age, male)
print(txt)

# 當遇到字串裡面有單引號或雙引號時, 在雙引號貨單引號前加上\
txt = "My job is \"Engineer\""
print(txt)

# 還有很多其他內建用法 具體請參考https://www.w3schools.com/python/python_strings.asp的下方內容