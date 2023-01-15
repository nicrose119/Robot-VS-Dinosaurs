from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot = Robot('Robo')
        self.dinosaur = Dinosaur('Dino',20)
        
    def run_game(self):
       self.display_welcome()
       self.battle_phase()
       self.display_winner()

    def display_welcome(self):
        self.greeting = "Welcome to Robot V Dinosaur 2022"
    
    def battle_phase(self):
        while self.robot.is_alive() and self.dinosaur.is_alive():
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)

    def display_winner(self):
        if self.robot.is_alive():
            print("The Robot is the Winner")
        else: 
            print("The Dinosaur is the Winner!")