from dinosaur import Dinosaur
from robot import Robot

class Battlefield:

    def __init__(self):
        self.robot = Robot("robot1")
        self.dinosaur = Dinosaur("dinosaur1", 10)
        
    def run_game(self):
        print(self.greeting)
        if self.robot.alive and self.dinosaur.alive == True:
            self.dinosaur.attack(self.robot)
            print(self.robot.name, self.robot.health)
            self.robot.attack(self.dinosaur)
            print(self.dinosaur.name, self.dinosaur.health)
        elif self.robot.alive or self.robot.alive == False:
            return self.winner
        print(self.display_winner)

    def display_welcome(self):
        self.greeting = "Welcome to Robot V Dinosaur 2022"
    
    def battle_phase(self):
        if self.robot.alive == True and self.dinosaur.alive == False:
            self.winner = self.robot.name
        elif self.robot.alive == False and self.dinosaur.alive == True:
            self.winner = self.dinosaur.name

    def display_winner(self):
        if self.winner == self.robot.name:
           self.display_winner = "The Robot is the Winner"
        elif self.winner == self.dinosaur.name:
            self.display_winner = "The Dinosaur is the Winner!"