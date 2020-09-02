# print(bool(1))
# print(bool('Hello'))
# print(bool(('a','b','c')))
# print(bool(['a','b']))


# print(bool(0))
# print(bool({}))
# print(bool([]))
# print(bool(""))
# print(bool(None))

# 假設有一個__len__的從類函數, 只要回傳0, 就會是false
class Person():
    def __len__(self): # __len__ 前後加雙底線的主要用意在於不能被更改, 有些參數當不想被修改時,就能透過這種方式
        return 0
    pass

John = Person()
print(bool(John))

# 自定義函數當然可以
def add(a,b):
    Total = a+b
    return Total
    # pass

print(bool(add(1,2)))

def truefunction():
    return True
    # pass

print(bool(truefunction()))

# 其他的內建函數 isinstance(x,int) 檢查是否為整數
x = 4.99
isinstance(x, int) # 直接返回False


