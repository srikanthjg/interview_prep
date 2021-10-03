## OOPS
# Python program to illustrate destructor
class Employee:

    # Initializing ==> Constuctor
    def __init__(self):
        print('Employee created.')

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')

obj = Employee()
del obj


##INPUT
"""
num = input ("Enter number :")
print(num)
name1 = input("Enter name : ")
print(name1)
"""

##File
"""
# a file named "geek", will be opened with the reading mode.
file = open('geek.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print (each)

# Python code to create a file
file = open('geek.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()
"""


# Python code to illustrate split() function
"""
with open("file.text", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print word
"""


## REGEX




## TRY CATCH
try:
  t=1/0
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")




###### MAP,FILTER,REDUCE


##MAP

arr=[1,2,3]
print "map", map(sum,[[1,2,3],[3,4,5],[1,1,1]])
## [6, 12, 3]



## 10
