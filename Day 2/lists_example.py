n=int(input("Enter the number of items to enter:"))
a=[]

for i in range(n):
    item=input(f"Item number {i} is ")
    a.append(item)

print("List is: ",a)


while(True):
    option = input("Do you want to change list(Y/N)?").upper()
    if option=="Y":
        change_list=input("Do you want to Add Item, Remove Item or Change Item?(A, R, C)").upper()
        match change_list:
            case "A":
                n = int(input("Enter the number of items to enter:"))
                for i in range(n):
                    added_item = input(f"Item number {i} is ")
                    a.append(added_item)

            case "R":
                removed_item = input("Enter the item to remove")
                a.remove(removed_item)
                print("New List is:", a)

            case "C":
                position=int(input("Enter the position of item you want to change:"))
                changed_item=input("Enter the new item that replaces the old item:")
                a[position]=changed_item

            case _:
                continue
    else:
        break

print("Final List is: ", a)
