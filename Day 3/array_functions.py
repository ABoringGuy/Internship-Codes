from functools import reduce

name_list=["Sudyumna","Pramish","Raunak"]
age=[12,22,21]
name_and_age=zip(name_list,age)
print(name_and_age)
print(list(name_and_age))#List creates a iterator. This prints the actual list but printing this again gives no value as iterator is exhausted
print(list(name_and_age))#Observe in output that the same function as above gives No value


name_with_number=enumerate(name_list)
print(list(name_with_number))

name_and_age_with_number=enumerate(name_and_age)
print(list(name_and_age_with_number))

for index,(name, age) in enumerate(name_and_age):#This gives blank as Iterator is already exhauseted from print(name_and_age)
    print(index,name,age)

new_name_and_age_zip=zip(name_list,age)

for index,(name, age) in enumerate(new_name_and_age_zip):#This works as we made a new zipped list instead
    print(index,name,age)

print(age)#Gives no value is it exhausted

def double_age(age):
    return age*2

age=[12,22,21]#We need to redefine list of age becasue it is exhausted. age

mapped_age=list(map(double_age,age))
print(list(mapped_age))

def age_filter(age):
    return age>15

age=[12,22,21]

filtered_age=list(filter(age_filter,age))#Gives a list that only satisfies condition of age_filter function
print(list(filtered_age))


age=[12,22,21]

reduced_age=reduce(lambda first_element,next_element : first_element+next_element, age)#Here reduce goes through all element of age() and performs specified task to give single output.
print(reduced_age)

mapped_age_lamda=list(map(lambda x: x*2, age))
print(list(mapped_age_lamda))