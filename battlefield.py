from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self,):
        self.robot = Robot("Jericho")
        self.raptor = Dinosaur("Blue", 30)

    def run_game(self):
        self
    
    def display_welcome(self):
        pass
    
    def battle_phase(self):
        self.robot.attack(self.raptor) 
        self.raptor.attack(self.robot)
    def display_winner(self):
        pass
