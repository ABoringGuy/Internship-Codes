class shape:
    def display(self):
        print("Shape")

class circle(shape):
    def display(self):
        super().display()
        print("Circle")

class square(shape):
    def display(self):
        super().display()
        print("Square")

class cylinder(circle, square):
    def display(self):
        super().display()
        print("Cylinder")

obj= cylinder()
obj.display()