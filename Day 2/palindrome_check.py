user_input = input("Enter a string: ").upper()
i=0
j=len(user_input)-1
is_palindrome=True
option=input("Use for loop or while loop(for/while)").upper()
if(option=="WHILE"):
    while i<j:
        if user_input[i]!=user_input[j]:
            is_palindrome=False
            print("The word is not a palindrome")
            break
        i+=1
        j-=1

    if is_palindrome==True:
        print("The word is a palindrome")

elif option=="FOR":
    for x in range (j):
        if user_input[i]!=user_input[j]:
            is_palindrome=False
            print("The word is not a palindrome")
            break
        i+=1
        j-=1

    if is_palindrome==True:
        print("The word is a palindrome")

else:
    print("Choose valid option")