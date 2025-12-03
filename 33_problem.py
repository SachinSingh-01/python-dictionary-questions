# Write a program to check if a value exists in dictionary (not key).
dic={
    "name":"sachin singh",
    "class":12,
    "fav_sub":"maths",
    "school":"Delhi public school"
}
n=input("Enter the values:")
if n in dic.values():
    print("yes present")
else:
    print("not present")