class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        pass
    
    def nickname(self):
        print("My nickname is " + self.name + " and I'm " + format(self.age) + " years old")
        pass

class Student(Person): # 創建子類別 Child class
    def __init__(self, firstname, lastname): #當今天子類別有__init__時，將不繼承父類別
        self.firstname = firstname
        self.lastname = lastname
    
    def printname(self):
        print(self.firstname, self.lastname)
        pass
    pass

class Child(Person): # 繼承父類別
    pass

Sam = Child("Dennis",5)
Sam.nickname()

Sandy = Student("Sandy", "Huang")
Sandy.printname()

# super, 當子類別要繼承父類別時
class Clothing(Person):
    def __init__(self, name, age, clothing):
        super().__init__(name, age)
        self.clothing = clothing
        pass
    def pclothing(self):
        print(self.name, self.age, self.clothing)
        pass
    pass

Nike = Clothing("Nike", "1995", "Nike-s")
Nike.pclothing()