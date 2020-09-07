# create a file
f = open("demo.txt", "w+")
f2 = open("test.xls", "w+")    
doc = f.write("Hello world \n")

# for loop write content to file
for i in range(10):
    f.write("This is the number: %s \r" % i)
    pass

# Close file
f.close() 


# Rewrite file
f=open("demo.txt", "a+") # a+, append

for i in range(2):
    f.write("Append line: %d \r" % i)
    pass


# Read file
f = open("demo.txt", "r")

if f.mode == 'r':
    contents = f.read()
    print(contents)

f.close()

# Delete
import os
# os.remove("demo.txt")

if os.path.exists("demo.txt"):
    os.remove("demo.txt")
else:
    print("File is not exist")
