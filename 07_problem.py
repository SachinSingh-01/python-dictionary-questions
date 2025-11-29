# Create a dictionary, store keys() in a variable, add a new key, and print the keys to show update.
student={
    "name":"Sachin Singh",
    "Class":12,
    "Roll no.":1,
    "School":"Army public school"
}
print(student)
x=student.keys()
print(x)
student["gender"]="male"
print(student)
print(x)