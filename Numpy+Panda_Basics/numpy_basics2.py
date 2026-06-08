import numpy as np

array1=np.array([1,2,3,4,5,6])
array2=np.array([7,8,9,10,11,12])

joined_array_by_concatenate=np.concatenate((array1,array2))
print("\nUsed to concatenate two arrays\n",joined_array_by_concatenate)

"""Stacking is same as concatenate but we can join array based on specified axis"""
"""Following program is equivalent to column stacking:"""
#stacking_array_by_column=np.stack((array1,array2), axis=0)
stacking_array_by_column=np.hstack((array1,array2))
print("\nStacking by column\n",stacking_array_by_column)

"""Following program is equivalent to row stacking:"""
#stacking_array_by_row=np.stack((array1,array2), axis=1)
stacking_array_by_row=np.vstack((array1,array2))
print("\nStacking by row\n",stacking_array_by_row)

stacking_array_by_depth=np.dstack((array1,array2))
print("\nStacking by depth\n",stacking_array_by_depth)

new_array=np.array([1,2,3,4,5,6,7,8,9,10])
""".split(array_name, number of splits to do)"""
split_array=np.split(new_array, 5)
print(split_array)

uneven_array=np.array([1,2,3,4,5,6,7,8,9,10,11])
"""If we simply use split() we get error,
We use array_split() to split uneven array.
It tries to split array as evenly as possible for specified indices."""
split_uneven_array=np.array_split(uneven_array, 5)
print(split_uneven_array)


two_dimension_array=np.array([[1,2,3,4,5,11],[6,7,8,9,10,12]])
"""We can use vsplit and dsplit for vertical and depth splitting. Similarly a alterantive code for same program is:"""
#np.split(two_dimension_array, 6, axis=0)
split_array_two_dimension=np.hsplit(two_dimension_array, 6)
print(two_dimension_array)
print(split_array_two_dimension)

age=np.array([2,3,18,56,33,12,45,3,75,43,21,13,14,2])
"""Seaching single value"""
print(np.where(age==2))
"""Searching multiple values"""
print(np.where((age==3) | (age==56) | (age==75)))
"""This gives boolean based on whether value is present or not"""
print(np.isin(age, [3,56,75] ))

sorted_array=np.array([2,4,5,6,7,10,11])
"""Below code gives the best position to insert provided values on sorted list.
It can also be used to find position of elements although that is not its original
intent"""
print(np.searchsorted(sorted_array,[3,56,75]))

"""Sorts array. Same code for higher dimensions"""
print(np.sort(age))

"""Filtering array. Below code is equivalent"""
# filtered_array=[]
# for individual_age in age:
#     if individual_age>18:
#         filtered_array.append(individual_age)
filtered_array=age[age>18]
print(np.sort(filtered_array))



