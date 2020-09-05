# 加減乘除
a = 10
b = 6
x = a + b
x = a - b
x = a * b
x = a / b

# 取餘數, 次方, 取整數位
x = a % b
x = a ** b
x = a // b

print(x)

# 縮寫
x = 2
x+=3
x-=3
x*=3
x/=3
x%=3
x**=3
x//=3

print(x)
# 邏輯運算, 2進制
# & AND閘
# | OR閘
# ^ XOR閘
# ~ NOT閘 可以用bin()顯示二進位答案
# << 左補 
x&=3 # x = x&3 
x|=3
x^=3
x>>=3
x<<=3
print(x)

bin(~0)
bin(~1)
bin(~2)
bin(~3)

x = 5
print(bin(x)) # 0b101
x >>= 1
print(bin(x)) # 0b10

# 基本邏輯判斷
print(10>0)
print(10<0)
print(10==10)
print(10>=0)
print(10<=0)
print(10!=0)


# is 判斷否為同一個東西
x = ['a','b']
y = ['a','b']
z = x
print(x is y) # False
print(z is x) # True

# in 包含內容
x = ['a','b','c']
y = 'a'
print(y in x) # True
