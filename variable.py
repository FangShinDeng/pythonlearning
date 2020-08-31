x = 'John'

def name():
    global x #全局變數
    x = 'fantastic'
    pass

name()
print('Name is '+ x)