
# student grade

```bash
marks = int(input("enter student marks : "))
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "c"
else:
    grade = "D"
print("grade of the student ->", grade)
```



# Nesting 

```bash
age = int(input("enter age : "))
if (age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")
```


# even odd number

```bash
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```



# greatest od 4 number entered by user

```bash
a = int(input("enter first number: "))
b = int(input("enter secand number: "))
c = int(input("enter third number: "))
d = int(input("enter fourth number: "))
 
if a >= b and a >= c and a >= d :
    print("frist number is largest", a)
elif b >= c and b >= d :
    print("secand number is largest", b)
elif c >= d :
    print("third number is largest", c)
else:
    print("forth number is largest", d)
```


# check the number is a multiple number or not 

```bash
x = int(input("Enter number: "))

if(x % 7  == 0  ):
    print("multiple of 7")
else:
    print("Not a multiple")
```

