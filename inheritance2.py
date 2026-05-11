class Prey:
    def flee(self):
        return "This animal is fleeing..."

class Predator:
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

print("Rabbit:", rabbit.flee())
print("Hawk:", hawk.hunt())
print("Fish flee:", fish.flee())
print("Fish hunt:", fish.hunt()) 