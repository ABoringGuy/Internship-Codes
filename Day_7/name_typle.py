from collections import namedtuple

account= namedtuple('account',['userid', 'username', 'password', 'balance'])

username=input("Enter Username")
password=input("Enter Password")
balance=int(input("Enter Balance"))


a=account("user0", username, password, balance)
print("User details are:",a)

print(f"Username of {a.userid} is {a.username} and balance is {a.balance}")

list=['user1', 'abc', '1234', '1234']
dict={'userid':'user2', 'username':'xyz', 'password':'1234' , 'balance':1234}

print("User details are:",a._make(list))
'''Convert list to named tuple and dict to named tuple'''
print("User details are:",a._make(dict))