class Dinosaur:
    def __init__(self, name, attack_power):
        self.dinosaur = name()
        self.attack_power = attack_power(10)
        self.dino_health = 100

    def attack(self, robot):
        if self.dino_health >0:
            print(f"{self.name} attacks {robot.name}")
       
    def dino_health(self):
        return self.dino_health >= 0
    



