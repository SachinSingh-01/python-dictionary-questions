# Given a dictionary of items and prices, increase each price by 10 percent.
dic={
    "mobile":14999,
    "bicycle":4999,
    "pc":55000,
    "helmet":1880
}
for k,v in dic.items():
    dic[k]=v*1.10
print(dic)