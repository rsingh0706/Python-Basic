# List  marks[0], marks[1] it can store elements type (integer, float, string, etc..)
marks = [94.4, 87.5, 95.2, 66.4
         
         ]

print(marks)
print(type(marks))
print(marks[0])
print(marks[1])

# list mutable (change) and immutable (no change)
student = ["karan", 94.6, 17, "Delhi"]
print(student[0])
student[0] = "rahul"
print(student)

# list slicing Similar to String Slicing ending idx is not included
number = [87, 74, 85, 67, 77]
print(number[1:4])
print(number[1:])
print(number[:4])
print(number[-4:-1])
print(number[:-4])
print(number[-3:])
print(number[:-3])
print(number[:-2])


# ##List Methods 
# List append adds one element at the end
number = [2, 4, 6]
number.append(7)
print(number)


# list sorts in ascending order (1, 2, 3, ... )

number = [2, 1, 3]
print(number.append(7))
print(number.sort())
print(number)

# list sorts in ascending order (a, c, p, q, t, b, d)
word = ['a', 'c', 'p', 'q', 't', 'b', 'd']
print(word.sort())
print(word)


# list sorts in descending order (3, 2, 1)
list = [2, 1, 3]
print(list.append(4))
print(list.sort(reverse=True))
print(list)


# list reverses 
word = ['a', 'c', 'p', 'q', 't', 'b', 'd']
word.reverse()
print(word)



# insert element at index
list = [2, 1, 3]
list.insert(1, 5)
print(list)


# remove first occurrence of element 






# remove element at idx
list = [2, 1, 3, 1]
list.pop(2)
print(list)



### Tuples in python
# A built-in data type that lets us create immutable sequences of values.
tup = (2, 4, 6, 8, 9)
print(type(tup))
print(tup[3])
print(tup[0])
print(tup[1])

# list mutable data
tup = [2, 4, 6, 8, 9]
tup[3] = 7
print(tup)

# Tuple methods 
# Tuple returns index of frist occurrence index number 0 to 1....
# tup.index(el)
tup = (1, 2, 3, 4, 5, 6)
print(tup.index(3))

# tup.count(el) counts total occurrence
num = (1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 2)
print(num.count(2))