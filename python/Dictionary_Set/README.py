# Dictionary in python 
# Dictionary are uesd to store data value in key:value pairs
# They are unordered, mutable(changeable) & don't allow duplicate keys
info = {
    "name" : "rahul",
    "subjects" : ["python", "html", "java"],
    "topic" : ("dict", "set"),
    "age" : 25,
    "marks" : 25.99
}
print(type(info))
print(info)

print(info["name"])
print(info["subjects"])
print(info["topic"])
print(info["age"])
print(info["marks"])
print(info.keys())
print(info.values())
print(info. items())

# value change 
info["name"] = "Anuj"
print(info)

# value add 
info["chauhan"] = "rahul"
print(info)


# Nested Dictionaries
student = {
    "name" : "vikalp soni",
    "subjects" : {
        "math" : 97,
        "hindi" : 85,
        "english" : 90

    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["english"])
print(student.keys())


# Dictionary Methods
