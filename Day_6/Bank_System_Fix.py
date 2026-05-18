#Flow of program:
#1)Load_database() creates a bank_data{}
#2)That Dict is sent to class BankDatabase. Bank Database has dict called accounts. That dict stores all the values that was input from class Accounts.
#3)Whenever we add new Account, we add it to accounts dict by creating a object. If we need to change or reference data, we check indivisual account in accounts dict.
#4)Save_database() has needs a parameter as dict. accounts dict is sent to Save_database which stores the values in .csv file.




import csv
from os import system


def load_database():
    bank_data = {}
    with open("bank_data.csv", "r",
              newline="") as file:  # Here without newline="", the .csv file contains a blank row after each row.
        reader = csv.DictReader(file)  # Converts each row into readable key value Dict

        for row in reader:
            userid = row["userid"]  # Key for nested dict so defined separate

            bank_data[userid] = {
                "username": row["username"],
                "password": row["password"],
                "balance": int(row["balance"])
            }
    return bank_data


def save_database(data):
    with open("bank_data.csv", "w", newline="") as file:
        fields = ["userid", "username", "password", "balance"]

        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()

        for userid, info in data.items():
            writer.writerow({
                "userid": userid,
                "username": info.username,
                "password": info.password,
                "balance": info.get_balance()
            })


class Account:
    def __init__(self, user_id: str, username:str, password:str, balance:int):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit_balance(self, amount: int):
        self.__balance += amount

    def withdraw_balance(self, amount: int):
        if amount < self.__balance:
            self.__balance -= amount
            return True
        else:
            return False


class BankDatabase:
    def __init__(self, user_database):
        self.accounts = {}

        for user_id, info in user_database.items():#count is used to count for enumerate. user_id and info is simply the data in user_databse
            self.accounts[user_id]= Account(user_id, info["username"], info["password"], info["balance"])

    def validate_login(self, username: str, password: str):
        for account in self.accounts.values():#Check single 'account' from dictionary of 'acounts'. Return the 'account' that matches
            if account.username == username and account.password == password:
                return account

    def add_user(self, username: str, password: str, balance: int):
        if not self.accounts:  # Checks if database is empty
            next_id = 0
        else:
            existing_id = {int(user_id.replace("user", ""))  # makes user0 to 0 only
                           for user_id in self.accounts.keys()}  # Loop through all id

            next_id = max(existing_id) + 1

        user_id = f"user{next_id}"
        self.accounts[user_id]= Account(user_id, username, password, balance)
        print("New user added successfully:")


class BankSystem(BankDatabase):
    def __init__(self, user_database):
        self.current_user = None#This is done in case user1 logged out and user2 wants to log in. If we don't do this, current_user would be user1 in case user2 fails to log in.
        super().__init__(user_database)

    def signup(self):
        new_user_name = input("Enter new username:").lower()
        if (any(user.username == new_user_name for user in self.accounts.values())):
            print("Username already taken")
        else:
            new_password = input("Enter new password:")
            confirm_new_password = input("Re-enter the password to confirm:")
            if confirm_new_password != new_password:
                print("Passwords do not match")
            else:
                try:
                    new_balance = int(input("Enter new balance:"))
                    self.add_user(new_user_name, new_password, new_balance)
                except ValueError:
                    print("Enter a valid number")

    def login(self):

        number_of_tries = 3
        while number_of_tries > 0:
            entered_user_name = input("Enter username:").lower()
            entered_password = input("Enter password:")
            confirmation = input("Are you sure you want to continue? (y/n)").upper()
            if confirmation == "N":
                continue
            elif confirmation != "Y" and confirmation != "N":
                print("Please enter either Y or N")
                continue

            user = self.validate_login(entered_user_name, entered_password)

            if user:
                self.current_user = user
                print(f"""Login Successful""")
                save_database(self.accounts)
                return True

            number_of_tries -= 1
            print(f"Login Unsuccessful. {number_of_tries} tries left")
        return False

    def check_balance(self):
        print(f"The current user balance is {self.current_user.get_balance()}")

    def deposit(self, amount: int):
        self.current_user.deposit_balance(amount)
        save_database(self.accounts)
        print(f"Rs {amount} was deposited. Current user balance is {self.current_user.get_balance()}")

    def withdraw(self, amount: int):
        check_balance = self.current_user.withdraw_balance(amount)
        if check_balance == True:
            save_database(self.accounts)
            print(f"Rs {amount} was withdrawn. Current user balance is {self.current_user.get_balance()}")
        else:
            print(f"Insufficient balance. Current user balance is {self.current_user.get_balance()}")

    def confirmation_choice(self, choice: str):
        if choice == "Y":
            return True
        elif choice == "N":
            return False
        else:
            print("Please enter either Y or N")
            return False

    def main_menu(self):
        while True:
            user_choice = input("""Welcome to Banking System. What do you want to do?:
            [1]Create New Account
            [2]Login
            [3]Exit
            [4]View All User Data
            [5]Clear Screen
            [6]Delete Account
            Enter your choice:""").upper()

            match user_choice:
                case "1" | "CREATE" | "CREATE NEW ACCOUNT":
                    self.signup()
                    save_database(self.accounts)
                case "2" | "LOGIN":
                    system("cls")
                    success = self.login()
                    if success:
                        self.menu()
                    else:
                        print("Too many failed attempts!")
                        exit()
                case "3" | "EXIT":
                    save_database(self.accounts)
                    exit()
                case "4" | "VIEW USER DATA":
                    print(self.__dict__)
                case "5" | "CLEAR SCREEN":
                    system("cls")
                case "6" | "DELETE ACCOUNT":
                    delete_user_id = input("Enter user ID of account you want to delete:")
                    del self.accounts[delete_user_id]
                    save_database(self.accounts)
                case _:
                    print("Enter a valid option")

    def menu(self):
        while True:
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
                        choice = input("Are you sure you want to continue? (y/n)").upper()
                        if self.confirmation_choice(choice):
                            self.deposit(amount)
                        else:
                            continue

                    except ValueError:
                        print("Enter a valid number")
                case "3" | "WITHDRAW MONEY":
                    try:
                        amount = int(input("Enter the amount to enter:"))
                        choice = input("Are you sure you want to continue? (y/n)").upper()
                        if self.confirmation_choice(choice):
                            self.withdraw(amount)
                        else:
                            continue

                    except ValueError:
                        print("Enter a valid number")
                case "4" | "LOG OUT":
                    save_database(self.accounts)
                    self.current_user = None
                    print("User Logged Out")
                    system("cls")
                    return
                case "5" | "CLEAR SCREEN":
                    system("cls")
                case "6" | "EXIT":
                    save_database(self.accounts)
                    exit()
                case _:
                    print("Enter a valid option")

    def run(self):
        self.main_menu()


bank_database = load_database()
bs = BankSystem(bank_database)
bs.run()


