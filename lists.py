# Lists 基礎用法
fruits = ['apple','banana','mango','guava','papaya']
# fruit = fruits[0]
# print(fruit)
# fruit = fruits[-1]
# print(fruit)
# fruit = fruits[0:2]
# print(fruit)
# fruit = fruits[-3:-1]
# print(fruit)

# 打印list所有內容
for fruit in fruits:
    print(fruit)
    pass

# 檢查水果裡面有沒有木瓜
if 'papaya' in fruits:
    print('Yes')
    pass

# 取list長度
print(len(fruits))



# list常用函式, append, insert, remove, pop, del, clear, copy

fruits.append("tomato") # 加入
print(fruits)

fruits.insert(2, 'grape') # 特定位置插入
print(fruits)

fruits.remove("banana") # 移除特性項目
print(fruits)

fruits.pop(2) # 依照特定位置移除, 若沒有填入序數, 則從後方移除一項
fruits.pop()
print(fruits)

del fruits[1]
# del fruits # del 是python語句, 並非列表方法
print (fruits) # NameError 若用Del fruits直接將整個fruits會刪除

fruits.pop()
fruits.pop()
fruits.pop()
print(fruits) # 只是刪除所有的內容物,最後剩餘空集合

fruits = ['apple','banana','mango','guava','papaya']
fruits.clear() # 直接清空所有內容物,剩餘空集合
print(fruits)

x = ['a','b','c']
y = x.copy()
print(y)

# list 相加減,兩張表資料合併
x = ['a','b','c']
y = ['d','e']
z = x + y
print(z)

for i in y: 
    x.append(i)
    pass
print(x)

x.extend(y)
print(x)

