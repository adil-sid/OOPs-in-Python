from car import Car

car1 = Car(2020, "Black", False)
car2 = Car(2021, "white", True)
car3 = Car(2022, "Blue", False)
# car4 = Car(2023, "Red", True)
# car5 = Car(2024, "Green", False)

print("\n--- Testing car1 ---")
car1.describe()
car1.drive()
car1.stop()

print("\n--- Testing car2 ---")
car2.describe()
car2.drive()
car2.stop()

print("\n--- Testing car3 ---")
car3.describe()
car3.drive()
car3.stop()

# print("\n--- Testing car4 ---")
# car4.describe()
# car4.drive()
# car4.stop()

# print("\n--- Testing car5 ---")
# car5.describe()
# car5.drive()
# car5.stop()

print("Total number of cars:", Car.num_cars)
