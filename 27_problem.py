# Create a dictionary of 3 items. Then ask user to input a key and print value.
car_name={
    "car1":"Mustang",
    "car2":"McLaren",
    "car3":"Buggati"
}
key=(input("Enter the key here:"))
if key in car_name:
        print(car_name[key])
else:
    print("Incorrect key")
