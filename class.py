# 類別

class Myclass(object):
    x = 5
    pass

Myclass1 = Myclass()
print(Myclass1.x) # 5

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        pass
    
    def nickname(self):
        print("My nickname is " + self.name + " and I'm " + format(self.age) + "years old")
        pass


John = Person('John',36)
print(John.name, John.age)
John.nickname()


class Student(Person): # 創建子類別 Child class
    def __init__(self, firstname, lastname): 
        self.firstname = firstname
        self.lastname = lastname
    pass

# Sam = Student("Mike", 28)
# Sam.nickname()
Sam = Student('Sam','Smith')
print(Sam)

