'''Store student names and marks in dictionary.Then print the student with the highest marks.'''
students = {
    "s1": {"name": "Amit", "marks": 70},
    "s2": {"name": "Rahul", "marks": 85},
    "s3": {"name": "Neha", "marks": 50},
    "s4": {"name": "priya", "marks": 86},
    "s5": {"name": "anurag", "marks": 79},
    "s6": {"name": "adarsh", "marks": 41},
}
top_name = ""
top_marks = 0
for k, v in students.items():
    if v["marks"] > top_marks:
        top_marks = v["marks"]
        top_name = v["name"]
print(top_name, top_marks)
