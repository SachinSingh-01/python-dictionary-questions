# Use popitem() and show which item is removed.
car={
    "brand":"Toyota",
    "model":"Toyota hilux",
    "year":1989
}
print(car)
# car.pop("model")
# print(car)
car.popitem()
print(car)
