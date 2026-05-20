from collections import namedtuple

account= namedtuple('account',['userid', 'username', 'password', 'balance'])

"""class account(namedtuple('account',['userid', 'username', 'password', 'balance'])):            
            def __new__(cls, userid, username, password, balance):
                return super().__new__(cls, userid, username, password, balance)
                
writing above is equivalent to making account. We use __new__ instead of __init__ as class made by namedtuple is
already immutable(value cannot change).

"""
username=input("Enter Username")
password=input("Enter Password")
balance=int(input("Enter Balance"))


a=account("user0", username, password, balance)
"""When we do this:
        def __new__(cls, userid, username, password, balance):
             return super().__new__(cls, userid, username, password, balance)
             
        is being run"""

print("User details are:",a)

print(f"Username of {a.userid} is {a.username} and balance is {a.balance}")

list=['user1', 'abc', '1234', '1234']
dict={'userid':'user2', 'username':'xyz', 'password':'1234' , 'balance':1234}
list_to_nametuple=a._make(list)
wrong_dict_to_nametuple=a._make(dict)
dict_to_nametuple=account(**dict)
print("User details are:",list_to_nametuple)
print("User details are:",wrong_dict_to_nametuple)#Note this only gives fieldnames for dict
print("User details as dict are:", dict_to_nametuple)#Use this to actually print dictionary

'''Convert list/dict to named tuple and dict to named tuple'''

print("User details are:", a._asdict())

"""._asdict() is used to convert named_tuple to dict"""

print(a._fields)
print(list_to_nametuple._fields)
print(dict_to_nametuple._fields)

"""._fields is used to print the keynames of declared namespace"""

replace_name=list_to_nametuple._replace(username="aboringguy")
print(replace_name)
print(list_to_nametuple)
"""Notice how ._replace() simply makes a new nametuple with replaced name.
It does not actually change the nametuple but makes a identical copy"""

b=account(userid="user0", username="abc", password="", balance=1234)
c=account.__new__(account,'user0' ,'ainterestingguy', '123', 100)
print(b)
print(c)

""".__new__() is same as creating a new object. When we create a new object(in b), python internally uses __new__.
We can use .__new__() directly as c(the same thing python does internally) but it is not recommended simply to make 
code cleaner and easier to understand"""

print(a.__getnewargs__())

"Returns a plain tuple from named tuple"

a=a._replace(username="aboringguy")

"""While not idea;, we can use above method to "change value" of tuple.
Basically replaces the whole object 'a' with new 'a'"""
print(a)