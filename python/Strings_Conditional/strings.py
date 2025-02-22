# concatenation  two words add
```bash
str1 = "jaipur is the city inside jaipur"
str2 = "rajasthan"
print(str1 + str2)
```


# Add new line & space add
```bash
str3 = "hello jaipur.\t love jaipur"
print(str3)
str4 = "hello rajasthon.\nlove rajaasthon"
print(str4)
str5 = "hello india.\n love india"
print(str5)
```


# lenth count

```bash
len1 = len(str1)
print(len1)
len2 = len(str2)
print(len2)
last_str = str1 + "     " + str2
print(last_str)
print(len(last_str))
```


# indexing number print (0,1,2,.....)

```bash
name = "jaipur rajasthan"
ch = name[6]
print(ch)
```

# Slicing  use Accessing parts of start number # [10:17] + kherli +ve....

```bash
value = "rajasthan kherli"
print(value[2:5])
print(value[10:17])
print(value[10:len(value)])
print(value[10:])
print(value[:9])
```

# Slicing negative index [not done]

```bash
mango = "Apple"
print(mango[-2:])
print(mango[-5:-1])
```


# string Functions , endswith("er.")  returns True  and False

```bash
value1 = "I am studying python from youtube"
print(value1.endswith("tube"))
print(value1.endswith("ybe"))
```


# string Functions, capitalize  1 st charater capital 

```bash
value2 = "i am jaipur"
print(value2.capitalize())
```


# String orignal no change , new string create and changs

```bash
value3 = "i am from kherli"
value3 = value3.capitalize()
print(value3)
```


# String replace (old, new )

```bash
value4 = "I am studing python from collage"
print(value4.replace("o", "r"))
```


# String find (word) returns 1 st number of 1 st occurrer

```bash
name3 = " i live in jaipur"
print(name3.find("n"))
print(name3[0])
```


# String (cont)  counts the occurrence

```bash
name4 = "i live in jaipur & i live in kherli"
print(name4.count("i"))
```
