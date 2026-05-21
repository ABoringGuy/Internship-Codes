def age_filter(num):
    if num>10:
        return num

num_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

filtered_list=filter(age_filter,num_list)
print(list(filtered_list))


even_filter=filter(lambda n: n%2==0, num_list)
print(list(even_filter))

dictfruit={"apple":1, "banana":2, "orange":3, "mango":4}

filtered_fruits=filter(lambda count: 1< count[1]<4, dictfruit.items())
"""Note count[0] is key and count[1] is value
dictfruit.items() returns each key& value as tuple so tuple index was used in count[]"""
print(list(filtered_fruits))
