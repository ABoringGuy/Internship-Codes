import numpy as np

from Numpy.numpy_basics import two_dimension_array

array1=np.array([1,2,3])
array2=np.array([4,5,6])

add_array=np.add(array1,array2)
#add_array=array1+array2
print("\nAdd two arrays\n",add_array)

sum_array=np.sum([array1,array2])
print("\nSum of two arrays\n",sum_array)

cumulative_sum=np.cumsum([array1,array2])
print("\nCumulative sum of two arrays\n",cumulative_sum)

product = np.multiply(array1,array2)
print("\nProduct of two arrays\n",product)

product_over_axis=np.prod([array1,array2], axis=1)
print("\nProduct of 2 array over axis\n",product_over_axis)

cumulative_product=np.cumprod([array1,array2])
print("\nCumulative product of 2 array over axis\n",cumulative_product)

power=np.power(array1,array2)
print("\nArray1 to Power Array2 is:\n",power)

lcm=np.lcm(array1,array2)
print("\nLCM is:\n",lcm)

lcm_of_array1=np.lcm.reduce(array1)
print("\nLCM of array 1 is:\n",lcm_of_array1)

gcd=np.gcd(array1,array2)
print("\nGCD is:\n",gcd)

union_array=np.union1d(array1,array2)
print("\nUnion of two arrays\n",union_array)

intersection_array=np.intersect1d(array1,array2)
print("\nIntersection of two arrays\n",intersection_array)

new_array=np.array([1,2,3,2,3,4,5,6,6])
unique_elements_only_array=np.unique(new_array)
print("\nUnique elements only array\n",unique_elements_only_array)