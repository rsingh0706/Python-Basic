## file input/output in python
## python can be used to perfrom operations on a file (read & write data)
## type of all file
## 1. Text file - .txt, .docx, .log, etc.
## 2. Binary file - .mp4, .mov, .png, .jpeg, etc
## https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function

## Open, read & close file
## we have to a open a file before reading or writing
## f = open("file_name", "mode")
## simpe.txt (file name)   r: read mode 
## demo.docx  (file name)  W: write mode
## data = f.read()
## f.close()

# f = open("farnodes.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

## Reading a file 
## data = f.read()  # reads entire file
## data = f. readline() # reads one line at a time


## read in charter

# f = open("farnodes.txt", "r")
# data = f.read(8)
# print(data)

## read in readline 
# f = open("farnodes.txt", "r")
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# # writing to a file
# f = open("farnodes.txt", "w")

# f.write("I went to learn devOps") # overwrite the entire file
# f.close()

# f = open("farnodes.txt", "a")
# f.write("then i will move to python Application")
# f.close()


# f = open("farnodes.txt", "a")
# f.write("\n after that devOps tools")
# f.close()


## create a new file python write mode
# f = open("sample.txt", "w")
# f.close()

# create a new file python using by append mode
# f = open("python.txt", "a")
# f.write("this is new file")
# f.close()

## file read and write mode open start file overwrite 
# f = open("sample.txt", "r+")
# f.write("abc")
# f.close()


## with syntax
# with open("demo.txt", "a")as f: as alias
# data = f.read()
# with open("python.txt", "r")as f:
#     data = f.read()
#     print(data)



## deleting a file using the os module 
## import os
## os.remove(filename)

# import os
# os.remove("python.txt")


## Let's practice

# create a new file "practice.txt" using python.add the folling data in it:
# with open("practice.txt", "w")as f:
#     f.write("Hi everone\nwe are learning file I/o\n")
#     f.write("using python.\nI like programming in python")


## WAF that replace all occurrences of python with devOps in above file name "practice.txt"
# with open("practice.txt", "r")as f:
#     data = f.read()

# new_data = data.replace("python", "java")
# print(new_data)

##  search if the word "learning" exists in the file or not
# word = "learning"
# with open("practice.txt", "r")as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")

## From a file containing number separted by comma, print the count of even number
with open("practice.txt", "r")as f:
    data = f.read()
    print(data)