# Create a dictionary and print all items where value is a string.
student={
    "name":"Sachin Singh",
    "class":56,
    "roll no.":1,
    "School":"Delhi public school",
    "Total marks":55,
    "Gender":"Male"
}
for k,v in student.items():
    if isinstance(v,str):
        print(v)
  