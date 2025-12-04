'''You have:
students = {
    "s1": {"name": "Amit", "marks": 70},
    "s2": {"name": "Rahul", "marks": 85},
    "s3": {"name": "Neha", "marks": 90}
}
Print names of all students who scored more than 80.'''
students = {
    "s1": {"name": "Amit", "marks": 70},
    "s2": {"name": "Rahul", "marks": 85},
    "s3": {"name": "Neha", "marks": 90}
}
for k,v in students.items():
    if v["marks"]>80:
        print(v["name"])