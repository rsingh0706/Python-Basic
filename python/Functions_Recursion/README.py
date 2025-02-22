# Built in functions > progammer , user defined functions
# Functions in Python > Block of statments that perfrom a specific Task
def calc_sum(a, b): # (a, b) parameters 
    sum = a+b
    print(sum)
    return sum 

calc_sum(5, 10)
calc_sum(15, 10)
calc_sum(25, 10)

# function definition
def calc_sum(a, b): # (a, b) parameters
    return a + b

sum = calc_sum(1, 3)  # (calc_sum) function call; (1, 3) arguments parameters ke under pass kiye jate h
print(sum)


def print_hello():
    print("hello")

print_hello()
print_hello()

def print_hello():
    print("hello")

output = print_hello()
print(output)  # output none


# average of 3 number
def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

calc_avg(97, 98, 99)


# functions of python
print("farnode", end=" ")  # sep = " "
print("devOps") # end = "\n"


# User defined functios

# let's practice
# WAF to print the lenth of a list (list is the parmeter)
cities = ["Delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["thor", "ironman", "captain", "rahul"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)


# print the elements of a list in a single line (list is the parameter)

cities = ["Delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["thor", "ironman", "captain", "rahul"]

print(cities[0], end= "\n")
print(cities[1], end= "\n")

def print_len(list):
    print_len(list)


# Convert USD to INR
# converter = input("Enter indian Value :")
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")
converter(3)


### Recursion
# when a function calls itself repeatedly

def show(n):
    if(n== 0):
        return
    print(n)
    show(n-1)
    print("END")
show(7)
# show(5)
# print(show)

# fact
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
print(fact(4))


# Let's Practice
# write a recursive function to calculate the sum of frist n natural number
# number calculate 1*1 = 1, 2*1 = 2, 
def cal_sum(n):
    if(n == 0):
        return
    print(n)
    cal_sum(n-1)
cal_sum(5)



# Total number of sum
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n
sum = calc_sum(10)
print(sum)