from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Laser Sword", 10)

    def attack(self, dinosaur):
        self.active_weapon = dinosaur.attack
        self.health -= dinosaur.attack_power

    def alive(self):
        if self.health == 0:
            self.alive = False
            return self.alive