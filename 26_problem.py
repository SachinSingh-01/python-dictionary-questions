# Write a program to print only keys that have integer values.
student={
    "name":"Sachin Singh",
    "class":56,
    "roll no.":1,
    "School":"Delhi public school",
    "Total marks":55
}
for k,v in student.items():
    if isinstance(v,int):
        print(f"{k}:{v}")