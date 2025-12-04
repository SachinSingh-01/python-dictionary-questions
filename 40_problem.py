'''Create a dictionary from a string showing character counts.
Example: "apple" → {'a':1, 'p':2, 'l':1, 'e':1}'''
char="apple"
d={}
for c in char:
    if c in d:
        d[c]+=1
    else:
        d[c]=1
print(d)