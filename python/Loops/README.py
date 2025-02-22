# Loops in Python Loops are used to repeat instructions.
# while Loops
count = 1
while count <= 5 :
    print("hello")
    count += 1
print(count) 


i = 1
while i <= 10:
    print("farnodes", i)
    i+=1

# print nummber from 1 to 5
# Iterator
i = 1
while i <= 5:
    print(i)
    i += 1
print("Loop ended")


i = 5    # initialization (start)
while i >= 1:
    print(i)
    i -= 1  
print("loop ended")
 

### let's practice
# print number from 1 to 100
i = 1
while i <=100: # stopping cond
    print(i)
    i += 1


# print number from 100 to 1    
i = 100    # initialization (start)
while i >= 1: # stopping condation
    print(i)
    i -= 1


# print the multiplication table of a number n.
i = 1      # initialization (start)
while i <= 10:
    print(i*4)
    i += 1

# n = int(input("enter number : "))
# i = 1
# while i <= 10:
#     print(i*n)
#     i += 1


# print the elements of the following list using a loop 

heroes = ["anuj", "swetank", "mohit", "bittu"]
i = 0
while i < len(heroes):
    print(heroes[i])
    i += 1


# Search for a number x in this tuple using loop:

num = (1, 4, 6, 7, 9, 11, 13, 15, 17)
i = 0       # initialization (start)
while i < len(num):
    print(num[i])
    i += 1 



num = (1, 4, 6, 7, 9, 11, 13, 15, 17, 13, 20)
x = 13
i = 0       # initialization (start)
while i < len(num):
    if(num[i] == x):
        print("FOUND at idx", i)
    else:
        print("finding")
    i += 1 


# Break & continue

i = 1
while i <= 7:
    print(i)
    if(i == 3):
        break
    i += 1
print("end of loop")

# print table 2*1 = 2, and so...

table = 1
while table <= 10:
    print(f"2 * {table} = {2*table}")
    table+=1

table = 1
while table <= 10:
    print(f"3 * {table} = {3*table}")
    table+=1


# Loops in python
# Loops are used for sequential traversal. for traversing list, string, tuple etc.
# range functions returns a sequence of number, staring from by default, and increments by 1 by default and steps before a specified number >> range (start? , stop, step?)

nums = [1, 2, 3, 4, 5, 6, 7]

for val in nums:
    print(val)

# seq number print 0 to 6
seq = range(7)

for i in seq:
    print(i)

# for i in range(10): # range(stop)
#     print(i)


# for i in range(2, 10): # range(stop, start)
#    print(i)

# for i in range(2, 10, 2): # range(stop, start, step)
#     print(i)

# for i in range(2, 100, 2): # range(stop, start, step)
#     print(i) 


#  let's practice
# using for & range()
# 1. print number from 1 to 100

# for i in range(1, 101):
#     print(i)


# 2. print number from 100 to 1
#for i in range(100, 0, -1):
#    print(i)

# print the multiplication table of a number

# number = int(input("enter number : "))

# for i in range(1, 11):
#     print(number * i)

### pass statment

# for i in range(5):
#     pass 
# print("some usefull work")

