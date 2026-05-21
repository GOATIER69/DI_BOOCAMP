#Exercice 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
cat1 = Cat("Milo", 3)
cat2 = Cat("Luna", 7)
cat3 = Cat("Simba", 5)
def find_oldest_cat(cat1, cat2, cat3):
    return max(cat1, cat2, cat3, key=lambda cat: cat.age)
oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"Le chat le plus âgé est {oldest.name}, et a {oldest.age} ans.")

#Exercice 2
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} fait ouaf !")

    def jump(self):
        print(f"{self.name} saute {self.height * 2} cm de haut !")
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 35)
print(f"Chien de David : {davids_dog.name}, {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()
print(f"\nChien de Sarah : {sarahs_dog.name}, {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()
print()
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} est le plus grand chien.")
elif sarahs_dog.height > davids_dog.height:
    print(f"{sarahs_dog.name} est le plus grand chien.")
else:
    print("Les deux chiens ont la même taille.")
    
#Exercice 3
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
stairway = Song([
    "There's a lady who's sure",
    "all that glitters is gold",
    "and she's buying a stairway to heaven"
])
stairway.sing_me_a_song()

#Exercice 4
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, *new_animals):
        for animal in new_animals:
            if animal not in self.animals:
                self.animals += [animal]
                print(f"{animal} ajouté au zoo.")
            else:
                print(f"{animal} est déjà dans le zoo.")

    def get_animals(self):
        print(f"\nAnimaux dans {self.zoo_name} : {self.animals}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} a été vendu.")
        else:
            print(f"{animal_sold} n'est pas dans le zoo.")

    def sort_animals(self):
        grouped = {}
        for animal in sorted(self.animals):
            key = animal[0].upper()
            if key in grouped:
                grouped[key] += [animal]
            else:
                grouped[key] = [animal]
        return grouped

    def get_groups(self):
        groups = self.sort_animals()
        print()
        for key, animals in groups.items():
            print(f"{key}: {animals}")
brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Giraffe", "Bear", "Baboon", "Lion", "Cat", "Cougar", "Zebra")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.get_groups()


