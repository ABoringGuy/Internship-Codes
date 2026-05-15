class shape:
    def display(self):
        print("Shape")

class circle(shape):
    def display(self):
        print("Circle")

class square(shape):
    def display(self):
        print("Square")

class cylinder(circle, square):#Inheritance order
        pass

obj= cylinder()
obj.display()

print(cylinder.mro())#displays the order of inheritance