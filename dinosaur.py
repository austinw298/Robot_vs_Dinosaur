class Raptor:
    def __init__(self, name, attack_power):
        self.health = 100
        self.name = name
        self.attack_power = attack_power

    def attack(self, robot):
        self.bite = robot

