# Count how many times each word appears in this list:
# ["apple", "banana", "apple", "mango", "banana", "apple"]
lst=["apple", "banana", "apple", "mango", "banana", "apple"]
count={}
for i in lst:
    if i in count:
        count[i]+=1
    else:
        count[i]=1  
for i,cnt in count.items():
    print(f"{i}:{cnt}")
