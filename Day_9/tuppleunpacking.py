"""This is one of the most common use of Tuple unpacking. When we return multiple value from function,
it is returned as tuple which we unpack to get individual value"""

def get_user():
    return "xyz", 22, "Kathmandu"

name, age, city = get_user()
print(name, age, city)


atuple=("Kathmandu", "Nepal")
city, country = atuple
print(city)
print(country)