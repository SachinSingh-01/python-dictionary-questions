# Add "pass" or "fail" status to each student based on marks.
students = {
    "s1": {"name": "Amit", "marks": 70},
    "s2": {"name": "Rahul", "marks": 85},
    "s3": {"name": "Neha", "marks": 90},
    "s4": {"name": "priya", "marks": 36},
    "s5": {"name": "anurag", "marks": 39},
    "s6": {"name": "adarsh", "marks": 31},
}
for k,v in students.items():
    if v["marks"]>40:
        v["status"] = "pass"
    else:
        v["status"] = "fail"
print(students)