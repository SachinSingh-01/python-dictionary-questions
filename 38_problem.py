# Remove a key only if its value is a string.
dict={
    "name":"Sachin",
    "class":"XII",
    "year":2023,
    "language":"python",
    "topic":"dictionary",
    "price":34342
}
to_remove=[]
for k,v in dict.items():
    if isinstance(v,str):
        to_remove.append(k)
for k in to_remove:
    dict.pop(k)
print(dict)