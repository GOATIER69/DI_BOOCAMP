#Exercice 3
from ExerciceXP import Dog
import random
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = f"{self.name}, " + ", ".join(args)
        print(f"{dog_names} tous jouent ensemble")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} n'est pas dressé!")
my_dog = PetDog("Fido", 2, 10)

print("--- Entraînement ---")
my_dog.train()

print("\n--- Jeu ---")
my_dog.play("Buddy", "Max")

print("\n--- Tours ---")
my_dog.do_a_trick()
my_dog.do_a_trick()
my_dog.do_a_trick()