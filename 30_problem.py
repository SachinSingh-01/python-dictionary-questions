# Create a dictionary with student data and update marks using input().
student_data={
    "name":"Moni Singh",
    "class":9,
    "roll no.":9,
    "marks":465
}
mark_update=input("Enter the update marks:")
student_data.update({"marks":mark_update})
print(student_data)