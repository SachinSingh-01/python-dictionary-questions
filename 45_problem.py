# Count how many students have marks above 75.
students = {
    "s1": {"name": "Amit", "marks": 70},
    "s2": {"name": "Rahul", "marks": 85},
    "s3": {"name": "Neha", "marks": 50},
    "s4": {"name": "priya", "marks": 86},
    "s5": {"name": "anurag", "marks": 79},
    "s6": {"name": "adarsh", "marks": 41},
}
count=0
for k,v in students.items():
    if v["marks"]>75:
        count+=1
print("No. of student have marks greater than 75:",count)