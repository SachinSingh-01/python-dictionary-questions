# Swap keys and values of a dictionary (values will be unique).
d = {
    "name": "sachin",
    "age": 20,
    "city": "delhi"
}
swapped = {}
for k, v in d.items():
    swapped[v] = k
print(swapped)
