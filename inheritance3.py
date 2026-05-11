class Animal():
    def eat(self):
        return "This animal is eating..."

    def sleep(self):
        return "This animal is sleeping..."

class Prey(Animal):
    def flee(self):
        return "This animal is fleeing..."

class Predator(Animal):
    def hunt(self):
        return "This animal is hunting..."

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass
    

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

print("Rabbit:", rabbit.eat(), rabbit.sleep(), rabbit.flee())
print("Hawk:", hawk.eat(), hawk.sleep(), hawk.hunt())
print("Fish flee:", fish.eat(), fish.sleep(), fish.flee())
print("Fish hunt:", fish.eat(), fish.sleep(), fish.hunt()) 