class Animal:

    num_of_animals = 0

    def __init__(self, name):
        self.name =name
        self.is_alive = True
        Animal.num_of_animals +=1

    def eat(self):
        print(f"{self.name} is eating...")
    
    def sleep(self):
        print(f"{self.name} is sleeping...")
    

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} says Squeak!")

dog = Dog("Buddy")
cat = Cat("Whiskers")
mouse = Mouse("Jerry")

dog.eat()
dog.sleep()
dog.speak()

cat.eat()
cat.sleep()
cat.speak()

mouse.eat()
mouse.sleep()
mouse.speak()

print("Total number of animals:", Animal.num_of_animals)
