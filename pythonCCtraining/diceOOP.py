from random import randint

class Dice():
    """Represents a die that can be rolled"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

dice6= Dice()

results = []
for i in range(10):
    current_result = dice6.roll_die()
    results.append(current_result)

print(results)