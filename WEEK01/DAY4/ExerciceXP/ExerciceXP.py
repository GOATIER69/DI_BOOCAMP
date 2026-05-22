#Exercice 1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
bengal_obj = Bengal("Rajah", 4)
chartreux_obj = Chartreux("Gris", 3)
siamese_obj = Siamese("Luna", 2)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]
sara_pets = Pets(all_cats)
sara_pets.walk()

#Exercice 2
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} aboie"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        
        if self_power > other_power:
            return f"{self.name} a gagné le combat!"
        elif other_power > self_power:
            return f"{other_dog.name} a gagné le combat!"
        else:
            return "C'est un match nul!"

dog1 = Dog("Rex", 5, 30)
dog2 = Dog("Bella", 3, 25)
dog3 = Dog("Max", 4, 35)

print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(f"\nVitesse de {dog1.name} : {dog1.run_speed():.2f}")
print(f"Vitesse de {dog2.name} : {dog2.run_speed():.2f}")
print(f"Vitesse de {dog3.name} : {dog3.run_speed():.2f}")

print(f"\n{dog1.fight(dog2)}")
print(f"{dog2.fight(dog3)}")
print(f"{dog1.fight(dog3)}")

#Exercice 4
class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        person = Person(first_name, age, self.last_name)
        self.members += [person]

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"You are over 18, your parents accept that you will go out with your friends")
                else:
                    print(f"Sorry, you are not allowed to go out with your friends.")
                return
        print(f"{first_name} n'existe pas dans la famille.")

    def family_presentation(self):
        print(f"Famille {self.last_name}:")
        for member in self.members:
            print(f"  {member.first_name} - {member.age} ans")

family = Family("Dupont")

family.born("Alice", 25)
family.born("Bob", 15)
family.born("Charlie", 18)
family.born("Diana", 10)

print("--- Présentation de la famille ---")
family.family_presentation()

print("\n--- Vérification de majorité ---")
family.check_majority("Alice")
family.check_majority("Bob")
family.check_majority("Charlie")
family.check_majority("Diana")
