# Create a class
class Person:
     def __init__(self, name, age):
            self.name=name
            self.age=age

     def greet(self):
          print("Hello, my name is", self.name)

     def __str__(self):
         return f"{self.name}{self.age}"

#Create a child class
class Child(Person):
    def __init__(self, fname, fage, gradyear):
        # Person.__init__(self, fname, fage) So that we can still inherit from Parent __init__. We are using super() instead for this example
        super().__init__(fname, fage)
        self.fname=fname
        self.fage=fage
        self.graduationyear=gradyear

    def greet(self):
        print("Hello Student here, my name is", self.name)


# Create an object
p1=Person("John", 36)

# Call the greet method
p1.greet()

del p1.name
# p1.greet() This causes a error

p2=Person("Johnny", 36)
del p2.age
p2.greet()#No error as age is not referenced in greet

p1.name="Shaw"
print(p1.name)
p1.greet()

print(p1)

c1=Child("String", 30, 2022)
c1.greet()#Greet() from student overwrites Person() despite inheritance occuring

for x in p1, c1:
    x.greet()#Print Greet() from both Person and Student

class Animal:
    def __init__(self, name, age):
        self.name=name
        self.__age=age#This causes age to be private data

    def get_age(self):
        return self.__age#Making a function to return private value is the only way to access the private value

    def __changeage(self, new_age):
        new_age=self.__age+1
        print(new_age)

    def get_new_age(self, user_age):
        self.__changeage(user_age)



animal=Animal("Animal", 18)
print(animal.name)
#print(animal.age) This gives error as Age is private
print(animal.get_age())#This works as we are calling a function to get age rather than the age itself

#animal.__changeage() This gives error as method is private

animal.get_new_age(18)

print(animal._Animal__age)#This is a method to access private class directly called Name Mangling. This is directly calling the attribute the way python calls it. Not recommend to use this.

class Car:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year

    class engine:#Inner class is class inside class. It does not inherit outer class property directly
        def __init__(self, c):#Getting object as parameter lets inner class inherit from outer class
            self.c=c

        def print_model(self):
            print(f"{self.c.model} says VROOOOOM!")


c=Car(make="Mercedes", model="Mercedes", year=2020)
c_inner=c.engine(c)

c_inner.print_model()