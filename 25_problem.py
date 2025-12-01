# Write a program to add a new key only if the key does NOT already exist.
dic={
    "name":"Sachin Singh",
    "class":"VII",
    "subject":"Mathematics"
}
if "marks" not in dic:
    dic["marks"]=85
    print(dic)
