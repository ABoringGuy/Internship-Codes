from collections import namedtuple

Account= namedtuple('Account', ['userid','username','password','balance'])


username=input("Enter your username:")
password=input("Enter your password:")
balance=int(input("Enter your balance:"))

acc=Account(username,username,password,balance)

def check_balance(acc):
    print(f"Your balance is {acc.balance}")

def deposit(acc,amount:int):
    balance=acc.balance+amount
    return balance

def withdraw(acc,amount:int):
    balance=acc.balance-amount
    return balance


def menu(a):
    while True:
        choice=int(input("""Enter your choice:
        [1] Check balance
        [2] Deposit
        [3] Withdraw
        [4] Exit"""))

        if choice==1:
            check_balance(a)
        elif choice==2:
            amount=int(input("Enter your amount:"))
            a=a._replace(balance=deposit(a,amount))
            print(a)
        elif choice==3:
            amount=int(input("Enter your amount:"))
            a=a._replace(balance=withdraw(a,amount))
            print(a)
        else:
            break
    return a

acc=menu(acc)
print(acc)

