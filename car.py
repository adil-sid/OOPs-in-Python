class Car:
    num_cars = 0

    def __init__(self, year, color, for_sale):
        self.year = year 
        self.color = color
        self.for_sale = for_sale
        Car.num_cars += 1

    def drive(self):
        print(f"You drive the {self.color} car.")
    
    def stop(self):
        print(f"You stop the {self.color} car.")

    def describe(self):
        print(f"The car is {self.year} {self.color} and is for sale {self.for_sale}")
    
