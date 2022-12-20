from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.health = 100
        self.name = name
        self.weapon = Weapon("Lightsaber", 100)

    def attack(self, dinosaur):
        self.roboattack = dinosaur 
