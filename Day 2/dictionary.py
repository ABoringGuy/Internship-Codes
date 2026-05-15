# Create the dictionary
car={"brand":"Ford", "model":"Mustang", "year":2024}
# Print the model
print(car["model"])
# Add a color key
car.update({"color":"red"})
# Remove the brand key
car.pop("brand")
# Print the dictionary
car.update({"brand":"Ford"})
print(car)
#display only keys
print(car.keys())
#display only items
print(car.values())
#copy items from dictionary to other
backup_car=car.copy()
print(backup_car)
#Assign same value to all keys. Also create a dict from tuple
key=("key1","key2","key3")
value=0
new_dict=dict.fromkeys(key, value)
#Get value from specified key
print(car.get("brand"))
#Remove last inserted key-value
new_dict.popitem()
print(new_dict)
#Set a default value for specified key
car.setdefault("color","white")
print(car)#Condition if color exists
car={"brand":"Ford", "model":"Mustang", "year":2024}
car.setdefault("color","white")#Condition if color doesn't exist
print(car)
#Nested dictionary
family={
    "father":{"name":"Devraj","Profession":"Business"},
    "mother":{"name":"Devika","Profession":"Business"},
    "son":{"name":"Sudyumna","Profession":"Engineer"}
        }
print(family)

#Alternative method to Nested Dictionary
father={"name":"Devraj","Profession":"Business"}
mother={"name":"Devika","Profession":"Business"}
son={"name":"Sudyumna","Profession":"Engineer"}

family={'father':father,'mother':mother,'son':son}

print(family)

#Access data in nested dict
print(family["son"]["name"])
print(family["son"])