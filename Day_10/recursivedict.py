dictionary={
    "a1":1,
    "a2":{"a3":2},
    "a4":{"a5":5, "a6":{"a7":9}}
}



def conversion(current_processing_dictionary, parent_key="" , new_dictionary=None):
    if new_dictionary is None:
        new_dictionary = {}

    for old_key, old_values in current_processing_dictionary.items():
        if parent_key:
            new_key=f'{parent_key}.{old_key}'#Try replacing new_key with parent_key in each line and see what happens
        else:
            new_key=old_key
        """Note that isinstance(data, datatype) checks if data is of certain type.
        In this case it checks if values is a dictionary by itself."""

        if isinstance(old_values, dict):
            conversion(old_values,new_key, new_dictionary)
        else:
            new_dictionary[new_key]=old_values

    return new_dictionary

"""Below program is almost same as above. The main difference is that it does not preserve the old keys.
Useful to understand basic flow of recursion."""

# def conversion(current_processing_dictionary , new_dictionary=None):
#     if new_dictionary is None:
#         new_dictionary = {}
#
#     for old_key, old_values in current_processing_dictionary.items():
#         """Note that isinstance(data, datatype) checks if data is of certain type.
#         In this case it checks if values is a dictionary by itself."""
#
#         if isinstance(old_values, dict):
#             conversion(old_values, new_dictionary)
#         else:
#             new_dictionary[old_key]=old_values
#
#     return new_dictionary

dictionary = conversion(dictionary)

for key, value in dictionary.items():
    print(f"{key}:{value}")


"""Pramish version, no need to create new dict. Print directly from function itself"""

# def conversion(current_processing_dictionary, parent_key="" ):
#     for old_key, old_values in current_processing_dictionary.items():
#         if parent_key:
#             new_key=f'{parent_key}.{old_key}'#Try replacing new_key with parent_key in each line and see what happens
#         else:
#             new_key=old_key
#         """Note that isinstance(data, datatype) checks if data is of certain type.
#         In this case it checks if values is a dictionary by itself."""
#
#         if isinstance(old_values, dict):
#             conversion(old_values,new_key)
#         else:
#             print(f"{new_key}:{old_values}")
#
#
# conversion(dictionary)
