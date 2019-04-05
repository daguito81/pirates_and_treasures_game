
from random import randint
import re


class Player:
    def __init__(self, kingdom):
        self.kingdom = kingdom
        self.location = 0
        self.energy = 10
        self.food = 10

    def eat(self, food):
        self.food = self.food - food
        self.energy = self.energy + food

        if self.food < 0:
            print("No food, you died.")
            exit()

        else:
            print("eating", food, "food")
            print("Location:", self.location)
            print("Energy:", self.energy)
            print("Food:", self.food)
        print(" ")

    def walk(self, steps):

        if steps == 1:
            energy_loss = 1
        else:
            energy_loss = int(steps / 2)

        self.location = steps + self.location
        self.energy = self.energy - energy_loss
        bear = randint(1, 50)
        pirates = randint(1, 5)
        found_food = randint(1, 5)

        print(" ")
        print("walking", steps, "steps")

        if player1.location >= 50:
            print("YOU FOUND THE TREASURE AND WON!")
            exit()

        elif self.location % pirates == 0:
            print("YOU FOUND PIRATES! They stole your food")
            self.food = self.food - randint(1, 3)
            print("Location:", self.location)
            print("Energy:", self.energy)
            print("Food:", self.food)

        elif self.location == 19:
            print("YOU WAKE UP!!! It was all a dream...")
            exit()

        elif self.location == bear:
            print("YOU FOUND A BEAR! He killed you.")
            exit()

        elif self.energy == 0:
            print("EAT OR DIE!")
            print("Location:", self.location)
            print("Energy:", self.energy)
            print("Food:", self.food)

        elif self.energy < 0:
            print("Out energy, you died.")
            exit()

        elif self.food < 0:
            print("No food, you died.")
            exit()

        elif self.location % found_food == 0:
            self.food = self.food + randint(1, 3)
            print("FOUND FOOD!")
            print("Location:", self.location)
            print("Energy:", self.energy)
            print("Food:", self.food)

        else:
            print("Location:", self.location)
            print("Energy:", self.energy)
            print("Food:", self.food)
        print(" ")


# GAME
player1 = Player('Blue')

print("""
You are a young traveller searching for a TREASURE. Your   \n
goal is to WALK around the island, but be careful! There \n
are pirates and bears roaming around. \n
\n
HOW TO PLAY THE GAME: type 'walk #' or 'eat #'. Replace # \n
with a number of your choice. TIP: start with small STEPS. \n
The more you WALK the more ENERGY you will lose. If your \n
ENERGY is down, EAT something!!! \n
\n
GOOD LUCK """)
print('   ')

for i in range(1000):
    print('Enter your action:')
    action = input()
    print('   ')

    if "eat " in action:
        number = int(re.findall(r'\d+', action)[0])  # Fixed strings with r''
        player1.eat(number)
    elif "walk " in action:
        number = int(re.findall(r'\d+', action)[0])
        player1.walk(number)
    else:
        print("Error, try again!")
        print('   ')
