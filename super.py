class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    
    def area(self):
        area_value = 3.14*((self.radius)**2)
        print(f"Area of circle is {area_value}")

class Square(Shape):
   
    def area(self, length):
        area_val = length*2
        print(f"The area of {self.color} sqaure is {area_val}")

class Reactangle(Shape):
    def __init__(self, color, is_filled, length, width):
        super().__init__(color, is_filled)
        self.length = length
        self.width = width
    

circle = Circle("Blue", False, 3)

circle.area()

square = Square(color="Red", is_filled=True)

square.area(4)