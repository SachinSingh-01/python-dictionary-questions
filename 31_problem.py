# Given a dictionary, print all keys whose values are greater than 50.
dic={
    "Social":78,
    "class":6,
    "maths":68,
    "English":34,
    "science":67
}
for k,v in dic.items():
    if v>50:
        print(k)