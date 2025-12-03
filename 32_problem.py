# Print all keys whose values are of type list.
dic={
    "car":"Mustang",
    "year":[2023,2034,2056,6734],
    "name":["sachin","moni","kumod","soni"],
    "bike":["splender","KTM","Hero","Ninja"]
}
for k,v in dic.items():
    if type(v)==list:
        print(k)