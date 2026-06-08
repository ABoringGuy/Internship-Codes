import numpy as np
import matplotlib.pyplot as plt

array=np.array([1, 2, 3, 4, 5])
"""Print Mean for Array above"""
print(np.mean(array))
"""Print Standard Deviation for Array above"""
print(np.std(array))
"""Print Median for Array above"""
print(np.median(array))

"""Plotting a linear graph.
.plot(x,y)"""
plt.plot(array,[10,1,4,6,2])
plt.show()

print("Array of certain range:",np.arange(-11, 12))

two_dimension_array=np.array(
    [
        [1,2,3],
        [4,5,6]
    ]
)
three_dimension_array=np.array(
    [
        [
            [1,2,3],
            [1,2,3]
        ],

        [
            [4,5,6],
            [1,2,3]
        ],
    ]
)



print("Dimension for two_dimension_array:",two_dimension_array.ndim)
print("Dimension for three_dimension_array:",three_dimension_array.ndim)
print("Shape for two_dimensional_array",two_dimension_array.shape)
print("Shape for three_dimensional_array",three_dimension_array.shape)
print("Data type is:",two_dimension_array.dtype)
print("Data Type after Conversion is:",np.array(three_dimension_array,dtype="S").dtype)

one_dimensional_array=np.array([1,2,3,4,5,6])
"""Here reshape, converted 1d to 2d array. It caused 2 arrays in higher dimension
and each array consists of 3 elements.
.reshape(no of arrays in higher(2d), no of elements in lower(1D))"""
one_dimension_to_two_dimension=one_dimensional_array.reshape(2,3)
print("Converted from 1d to 2d",one_dimension_to_two_dimension)

"""Here reshape converted 1d to 3d. It caused 3 arrays for 3d array, each nest
inside only has 1 array and lowest dimension array has 2 elements each"""
one_dimension_to_three_dimension_array=one_dimensional_array.reshape(3,1,2)
print("Converted from 1d to 3d",one_dimension_to_three_dimension_array)

"""We used -1 if we want to flatten to Array(reduce dimensions)"""
three_to_one_dimension=three_dimension_array.reshape(-1)
print("Converted to 1d from 3d:", three_to_one_dimension)

"""Slicing for 1D is done as:
array_name[starting index:(ending index-1)"""
sliced_data_for_1d=array[1:4]
print("Slicing for 1d array is:",sliced_data_for_1d)

"""Slicing for 2D is done as:
array_name[array position for higher nest, starting index:(ending index-1)]
Here we used [0, 1:2]. 0 denotes 1st array inside nest. If we used 1 then 2nd array would be selected"""
sliced_data_for_2d=two_dimension_array[0,1:2]
print("Slicing for 2d array is:",sliced_data_for_2d)

sliced_data_for_3d=three_dimension_array[0,1,1:2]
print("Slicing for 3d array is:",sliced_data_for_3d)

"""nditer is used to iterate through high dimension array.
Alternatively, for x in three_dimension_array:
                      for y in x:
                           for z in y:
                                print(z)
                                
Also does the same job"""
for x in np.nditer(three_dimension_array):
    print("Iterating by each element for 3d:", x)

"""Iterating with giving ID based on index of each element in array"""
for id,x in np.ndenumerate(three_dimension_array):
    print("Iterating by each element for 3d:",id, x)