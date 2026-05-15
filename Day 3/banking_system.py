from os import system,name #To help clear terminal, this does not work in pycharm so run in Windows
import sys
sudyumna={"username":"aboringguy",
          "password":"ABoringPassword",
          "balance":1200
          }
pramish={"username":"ainterestingguy",
          "password":"AInterestingPassword",
         "balance":9999912399
          }
rudyumna={"username":"abc",
          "password":"1234",
          "balance":12053500
          }
pramisha={"username":"xyz",
          "password":"4567",
         "balance":99955359999
          }
gudyumna={"username":"gsboringguy",
          "password":"ABfsforingPassword",
          "balance":120343240
          }



bank_database={"user-1":sudyumna,
               "user-2":pramish,
               "user-3":rudyumna,
               "user-4":pramish,
               "user-5":gudyumna
               }

correct_credentials= False
correct_count=3



while(True):
    found=False
    print("Welcome to Banking System")
    while correct_credentials==False and correct_count!=0:

        username=input("Please enter your username: ").lower()
        password = input("Please enter your password: ")
        confirmation=input("Are you sure this is correct?(Y/N) ").upper()
        if confirmation=="N":
            system("cls")
            continue
        elif confirmation!="Y" and confirmation!="N":
            print("Please enter either Y or N")
            continue
        else:
            for x, obj in bank_database.items():
                if obj["username"]==username and obj["password"]==password:
                    balance=obj["balance"]
                    print("Correct! You have successfully logged in!")
                    correct_count=-1
                    correct_credentials=True
                    break
            if correct_credentials==False:
                correct_count-=1
                print(f"Wrong Credentials. {correct_count} tries left!")
                if correct_count==0:
                    exit()

    log_out=False

    while log_out==False:
        if (log_out == True):
            print("This should work")
            break
        change_amount=0


        options=input("""Do you want to?:
         [1]Check Balance
         [2]Deposit Money
         [3]Withdraw Money
         [4]Log-Out
         [5]Clear Screen
         [6]Exit
         
         Option:""").upper()


        match options:
            case "CHECK BALANCE" | "1":
                print("Your Balance is:", balance)

            case "DEPOSIT MONEY" | "2":
                try:
                    change_amount=int(input("Enter Amount you want to deposit: :"))
                except ValueError:
                    print("Input must be an integer!")
                    continue
                confirmation=input(f"Are you sure you want to deposit Rs.{change_amount}?(Y/N)").upper()
                if confirmation=="Y":
                    balance+=change_amount
                    print("Your New Balance is:", balance)
                    obj["balance"]=balance
                elif confirmation!="N" and confirmation!="Y":
                    print("Invalid Option. Transaction Failed!")
                else:
                    pass

            case "WITHDRAW MONEY" | "3":
                try:
                    change_amount = int(input("Enter Amount you want to withdraw:"))
                except ValueError:
                    print("Input must be an integer!")
                    continue
                confirmation = input(f"Are you sure you want to withdraw Rs.{change_amount}?(Y/N)").upper()
                if confirmation == "Y" and balance>change_amount:
                    balance -= change_amount
                    obj["balance"] = balance
                    print(f"Your Deposit Money is {change_amount} and your new Balance is {balance}")

                elif confirmation != "N" and confirmation != "Y":
                    print("Invalid Option. Transaction Failed!")
                elif confirmation =="Y" and balance<change_amount:
                    print(f"Not Enough Balance. Your current Balance is {balance}!")
                else:
                    pass

            case "LOG OUT" | "4":
                log_out=True
                correct_credentials = False
                correct_count = 3

            case "Clear Screen" | "5":
                system("cls")

            case "Exit" | "6":
                exit()

            case _:
                print("Please Enter Valid Option")

