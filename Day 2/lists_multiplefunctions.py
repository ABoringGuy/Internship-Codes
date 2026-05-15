# Create a list
colors=["red","green","blue"]

# Print the first item
print(colors[0])
# Change the second item to "yellow"
colors[1]="yellow"
print(colors)

# Add "purple" to the end
colors.append("purple")
print(colors)
# Remove "red"
colors.remove("red")
print(colors)

#Add "pink" at position 1
colors.insert(1,"pink")
print(colors)

#Reverse the order of list
colors.reverse()
print(colors)

#Sort the list in alphabetical order
colors.sort()
print(colors)

#Show the item on list at different positions
print(colors[0])
print(colors[-1])#Print Last item
print(colors[0:2])
print(colors[-2:])

#show number of items in a list
print("Number of items in list is", len(colors))

#search in list by name
if "red" in colors:
    print("Red is present in the list")
else:
    print("Red is not present in the list")

#show items in list by loop
for x in colors:
    print(x)

#Give the class type of list
print(type(colors))#Assumes the list color is object with data type 'list'

#pop out value in specified position from listcolors.pop(1)
print(colors)