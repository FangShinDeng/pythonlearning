# 自定義函數

def my_function(word = '1'):
    print("This is the word: " + word)   
    pass

my_function('a')

# 若不知道需要傳遞多少個函數給word,可以使用"*"來讓參數接收一整個位元組
# 当函数的参数不确定时，可以使用*args 和**kwargs，*args 没有key值，**kwargs有key值。
# * => Tuple
# ** => Dict
def my_function2(*name):
    print("This is the Name: " + name[2])
    pass

my_function2('John', 'Adam', 'Sam')

def my_function3(farg,**kwarg):
    print("farg", farg)
    for key in kwarg:
        print("content %s:%s" % (key, kwarg[key])) # 帶變數中間用%
        pass
    pass

data = {
    "name": "John",
    "age": 36,
    "male": "Man"
}

my_function3('first')

my_function3('first', **data) # 帶入值時,**也務必要加入

# Recursion 函式帶入自己函式
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)