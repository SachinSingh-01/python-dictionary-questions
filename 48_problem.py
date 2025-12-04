'''For this dictionary:
d = {"a": [1, 2, 3], "b": [4, 5]}
Print sum of all numbers present in all lists.'''
d = {"a": [1, 2, 3], "b": [4, 5]}
total = 0
for lst in d.values():
    for num in lst:
        total += num
print(total)
