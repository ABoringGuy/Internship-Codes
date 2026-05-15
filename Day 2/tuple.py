# Create the tuple
fruits=("apple", "banana", "cherry")
# Print the second item
print(fruits[1])
# Print the number of items
print(len(fruits))
# Unpack the tuple
a,b,c=fruits
print(a,b,c)
#Unpack the tuple but don't put 2nd value
x,_,z=fruits
print(x,z)
#Seperate it in 2 tuples
q,*w=fruits
print(q,w)
print(type(q),type(w))
#Join tuple
price=(20,30,40)
joined_tuple=fruits+price
print(joined_tuple)
#Repeat tuple
twice=fruits*2
thrice=fruits*3
print(twice)
print(thrice)

#count in tuple
print(twice.count("apple"))

#search in tuple
print(thrice.index("banana"))

#As Tuple can't be changed, we convert to list and apply changes
fruits_list=list(fruits)
fruits_list.remove("cherry")
fruits=tuple(fruits_list)
print(fruits)