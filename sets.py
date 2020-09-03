# set 特別用法
x = {'a','b','c'}
y = ['d','e','f']
print(type(x))
# z = x + y  # Set跟List是不能直接相加的

# 若想要補內容到set裡面, 需要用update()

x.update(y)
print(x)

# 當要刪除set裡面的內容物時, 若東西不存在則會error, 要使用discard就不會error
# x.remove('g') # error
x.discard('g')

print(x)

# 結合set要使用union
x = {'a','b'}
y = {'c','d'}
# z = x + y # error set無法相加
# print(z)

z = x.union(y)
print(z)