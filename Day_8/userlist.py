from collections import UserList


# Creating a list where deletion is not allowed
class MyList(UserList):

    # Prevents using remove() on list
    def remove(self, s=None):
        print("Removing from list")

        # Prevents using pop() on list

    def pop(self, s=None):
        print("Removing from list")

    # Create an instance of MyList


L = MyList([1, 2, 3, 4])
print("Original List")

# Append 5 to the list
L.append(5)
print("After Insertion")
print(L)
# Attempt to remove an item (will raise error)
L.remove()