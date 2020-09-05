mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(type(myit)) # <class 'tuple_iterator'>
print(myit)
print(next(myit)) # apple 
print(next(myit)) # banana
print(next(myit)) # cherry

mytuple = "abc"
myit = iter(mytuple) #字串也可以
print(myit)
print(next(myit)) # a
print(next(myit)) # b
print(next(myit)) # c
# print(next(myit)) # StopIteration

for x in myit:
    print(x)
    pass

# 創建迭代器
class Mynumbers():
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = Mynumbers()
myit = iter(myclass)

print(myclass)
print(myit)
print(next(myit))
print(next(myit))
print(next(myit))

# StopIteration
class testInteration():
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a < 20:
            x = self.a
            self.a += 1
            return x
        else: 
            raise StopIteration

test = testInteration()
myit = iter(test)

for i in myit:
    print(i)
    