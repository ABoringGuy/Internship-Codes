# Create the set
colors={"red","green","blue"}
# Print the set
print(colors)
# Add "yellow"
colors.add("yellow")
# Remove "green"(if green not present shows error)
colors.remove("green")
#Remove "green"(if green not present doesn't show error)
colors.discard("green")
# Print the number of items
print(len(colors))
#union of 2 sets with 3rd set
object={"apple","banana","berry"}
color_and_object=colors.union(object)

alt_color_and_object=object | colors
print(alt_color_and_object)
print(color_and_object)
#Make Frozenset. Frozenset are similar to set but value cannot be added or removeed
frozen_object=frozenset(object)
print("frozen_object is of class ", type(frozen_object))
print("object is of class ", type(object))

#check if red is present in colors
print("red" in colors)

#check if red is not present in colors
print("red" not in colors)

#make a new set with common values of 2 sets
common_set_color=color_and_object.intersection(colors)
print(common_set_color)

common_set_object=color_and_object & object
print(common_set_object)

#make a new set with values of only in 1st set but not in 2nd set
new_color_set={"red"}
first_set_values_only=colors - new_color_set
print(first_set_values_only)