'''Given:
nums = [1, 2, 3, 4]
Create a dictionary like:
{1: 1, 2: 4, 3: 9, 4: 16}
(key = number, value = square)'''
nums = [1, 2, 3, 4]
d={}
for n in nums:
    d[n]=n*n
print(d)