from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name()
        self.robot_health = 100
        self.active_weapon = Weapon("Laser Sword", 10)

    def attack(self, dinosaur):
        if self.robot_health >0:
            print(f"{self.name} attacks {dinosaur.name}")
       
    def robot_health (self):
        return self.health >= 0   
