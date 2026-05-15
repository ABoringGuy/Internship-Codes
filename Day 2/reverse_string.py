user_input = input("Enter a string: ")
i=0
j=len(user_input)-1

character=list(user_input)

option=input("Use for loop or while loop(for/while)").upper()
if(option=="WHILE"):
    while i<j:
        character[i], character[j]=character[j], character[i]
        i+=1
        j-=1
    reversed_string="".join(character)#Convert list to string
    print("The reversed string is:",reversed_string)

elif option=="FOR":
    for x in range (j):
        character[i], character[j] = character[j], character[i]
        i += 1
        j -= 1
    reversed_string="".join(character)#Convert list to string
    print("The reversed string is:", reversed_string)

else:
    print("Invalid option")

