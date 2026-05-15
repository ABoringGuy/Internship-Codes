while(True):
    a = int(input("Enter the 1st number:"))
    b = int(input("Enter the 2nd number:"))

    command = input("User can perform addition, substraction, multiplication or division\nWhat do you want to do?:").upper()
    match command:
        case "ADDITION":
            print("Sum is:", a+b)
        case "SUBSTRACTION":
            print("Difference is:", a-b)
        case "MULTIPLICATION":
            print("Product is:", a*b)
        case "DIVISION":
            print("Division is:", a/b)
        case _:
            print("Invalid command")
            continue
    follow_up=input("Do you want to continue up?(y/n)").upper()

    if follow_up=="N":
        break