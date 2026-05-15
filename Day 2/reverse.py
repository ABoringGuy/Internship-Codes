user_input=int(input("Enter any number:"))
reverse_num=0

while user_input>0:
    a=user_input%10
    reverse_num=reverse_num*10+a
    user_input=user_input//10

print(reverse_num)