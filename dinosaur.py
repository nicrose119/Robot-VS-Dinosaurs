class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power(10)
        self.health = 100

    def attack(self, robot):
      self.attack = robot.attack
      self.health -= robot.attack_power

    def alive(self):
        if self.health == 0:
            self.alive = False
            return self.alive
