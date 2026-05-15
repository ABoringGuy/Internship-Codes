import json
from os import system


with open("Bank_database.json", "r") as file:
    bank_database = json.load(file)

def save_database(data):
    with open("bank_database.json", "w") as file:
        json.dump(data, file, indent=4)

class Account:
    def __init__(self,user_id:str, user_data,user_database):
        self.user_id=user_id
        self.user_database=user_database

        self.username=user_data["username"]
        self.password=user_data["password"]
        self.__balance=user_data["balance"]

    def get_balance(self):
        return self.__balance

    def deposit_balance(self,amount:int):
        self.__balance+=amount
        self.user_database[self.user_id]["balance"]=self.__balance

    def withdraw_balance(self,amount:int):
        if(amount<self.__balance):
            self.__balance -= amount
            self.user_database[self.user_id]["balance"]=self.__balance
            return True
        else:
            return False



class BankDatabase:
    def __init__(self,user_database):
        self.user_database=bank_database
        self.accounts=[]

        for count, (user_id, info) in enumerate(user_database.items()):
            self.accounts.append(Account(user_id, info, self.user_database))#make a object self.accounts for class Account. Sends the dictionary values to Account.

    def __str__(self, user_databse):
        for all_names in user_databse.values():
            print(all_names["username"])

    def validate_login(self, username:str, password:str):
        for account in self.accounts:
            if account.username == username and account.password == password:
                return account

    def add_user(self,username:str,password:str, balance:int):
        user_id=f"user{(len(self.user_database))}"
        info={"username":username,"password":password,"balance":balance}
        new_account=Account(user_id,info,self.user_database)
        self.user_database[user_id]=info
        self.accounts.append(new_account)
        print("New user added successfully:")



class BankSystem(BankDatabase):
    def __init__(self,user_database):
        super().__init__(user_database)

    def signup(self):
        new_user_name= input("Enter new username:").lower()
        if(any(user["username"]==new_user_name for user in self.user_database.values())):###LEFT HERE .values IS GIVING ERROR
            print("Username already taken")
        else:
            new_password= input("Enter new password:")
            confirm_new_password=input("Re-enter the password to confirm:")
            if (confirm_new_password!=new_password):
                print("Passwords do not match")
            else:
                try:
                    new_balance=int(input("Enter new balance:"))
                    self.add_user(new_user_name,new_password,new_balance)
                except ValueError:
                    print("Enter a valid number")


    def login(self):
        self.current_user=None
        number_of_tries = 3
        while(number_of_tries>0):
            entered_user_name = input("Enter username:").lower()
            entered_password = input("Enter password:")
            confirmation=input("Are you sure you want to continue? (y/n)").upper()
            if(confirmation=="N"):
                continue
            elif(confirmation!="Y" and confirmation!="N"):
                print("Please enter either Y or N")
                continue

            user = self.validate_login(entered_user_name, entered_password)

            if user:
                self.current_user=user
                print(f"""Login Successful""")
                return True

            number_of_tries -= 1
            print(f"Login Unsuccessful. {number_of_tries} tries left")
        return False

    def check_balance(self):
        print(f"The current user balance is {self.current_user.get_balance()}")

    def deposit(self, amount:int):
        self.current_user.deposit_balance(amount)
        print(f"Rs {amount} was deposited. Current user balance is {self.current_user.get_balance()}")

    def withdraw(self, amount:int):
        check_balance=self.current_user.withdraw_balance(amount)
        if(check_balance==True):
            print(f"Rs {amount} was withdrawn. Current user balance is {self.current_user.get_balance()}")
        else:
            print(f"Insufficient balance. Current user balance is {self.current_user.get_balance()}")

    def confirmation_choice(self, choice:str):
        if choice=="Y":
            return True
        elif choice=="N":
            return False
        else:
            print("Please enter either Y or N")
            return False

    def main_menu(self):
        while True:
            user_choice=input("""Welcome to Banking System. What do you want to do?:
            [1]Create New Account
            [2]Login
            [3]Exit
            [4]View All User Data
            [5]Clear Screen
            Enter your choice:""").upper()

            match user_choice:
                case "1" | "CREATE" | "CREATE NEW ACCOUNT":
                    self.signup()
                case "2" | "LOGIN":
                    system("cls")
                    success=self.login()
                    if(success):
                        self.menu()
                    else:
                        print("Too many failed attempts!")
                        exit()
                case "3" | "EXIT":
                    save_database(self.user_database)
                    exit()
                case "4" | "VIEW USER DATA":
                    print(self.__dict__)
                case "5" | "CLEAR SCREEN":
                    system("cls")
                case _:
                    print("Enter a valid option")


    def menu(self):
        while (True):
            user_choice = input(f"""Welcome {self.current_user.username.upper()}! What do you want to do?:
         [1]Check Balance
         [2]Deposit Money
         [3]Withdraw Money
         [4]Log-Out
         [5]Clear Screen
         [6]Exit
         
         Option:""").upper()

            match user_choice:
                case "1" | "CHECK BALANCE":
                    self.check_balance()
                case "2" | "DEPOSIT MONEY":
                    try:
                        amount = int(input("Enter the amount to enter:"))
                        choice=input("Are you sure you want to continue? (y/n)").upper()
                        if self.confirmation_choice(choice):
                            self.deposit(amount)
                        else:
                            continue

                    except ValueError:
                        print("Enter a valid number")
                case "3" | "WITHDRAW MONEY":
                    try:
                        amount = int(input("Enter the amount to enter:"))
                        choice=input("Are you sure you want to continue? (y/n)").upper()
                        if self.confirmation_choice(choice):
                            self.withdraw(amount)
                        else:
                            continue

                    except ValueError:
                        print("Enter a valid number")
                case "4" | "LOG OUT":
                    save_database(self.user_database)
                    self.current_user=None
                    print("User Logged Out")
                    system("cls")
                    return
                case "5" | "CLEAR SCREEN":
                    system("cls")
                case "6" | "EXIT":
                    save_database(self.user_database)
                    exit()
                case _:
                    print("Enter a valid option")

    def run(self):
        while True:
            self.main_menu()

bs=BankSystem(bank_database)
bs.__str__(bank_database)
bs.run()


