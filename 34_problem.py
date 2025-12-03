# You are given:
# d = {"a": 1, "b": 5, "c": 1, "d": 10}
# Print all keys where the value is 1.
d = {"a": 1, "b": 5, "c": 1, "d": 10}
print(d)
for k,v in d.items():
    if v==1:
        print(k)