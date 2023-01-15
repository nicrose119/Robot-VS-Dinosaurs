from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Laser Sword", 10)

    def attack(self, dinosaur):
       dinosaur.health -= self.active_weapon.attack_power
       print(f'{dinosaur.name} now has {dinosaur.health} remaining')

    def is_alive(self):
        return self.health > 0