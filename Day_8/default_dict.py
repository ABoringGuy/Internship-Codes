"""Default Dict helps assign default values for missing keys"""

from collections import defaultdict

"""Using List as Default Factory:"""
d={"a":["apple"], "b":["bada apple"]}

d=defaultdict(list, d)

li = ["apple", "ant" ,"cat", "drunk"]

for value in li:
    d[value[0]].append(value)#We can use list modules, append(), for dict here

print("Dictionary with values as list:")
print(d)
"""Here we assigned the list as value for dict. We made the 1st letter of each element in list as key"""



"""Using int as Default Factory:"""
sales = {"apple": 5, "banana": 2}

sales = defaultdict(int, sales)

new_sales = ["apple", "orange", "apple", "mango", "banana", "apple"]

for item in new_sales:
    sales[item] += 1#Using arithmetic operation to set values in dict
print(dict(sales))
"""Here, we assigned int values as values for missing keys. We can use float as well"""

"""Using string as Default Factory:"""
sd={}
sd = defaultdict(str,sd)
sd['animal'] = 'dog'
print(sd)
"""We assigned value "dog" to "animal" despite that key not existing"""