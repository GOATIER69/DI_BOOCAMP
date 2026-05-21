#Exercice 1
import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def definition(self):
        print("Un cercle est une figure géométrique plane constituée de tous les points équidistants d'un point central appelé centre.")
circle1 = Circle()
print(f"Cercle avec rayon par défaut : {circle1.radius}")
print(f"Périmètre : {circle1.perimeter():.2f}")
print(f"Aire : {circle1.area():.2f}")
circle1.definition()

print()
circle2 = Circle(5)
print(f"Cercle avec rayon 5 : {circle2.radius}")
print(f"Périmètre : {circle2.perimeter():.2f}")
print(f"Aire : {circle2.area():.2f}")
circle2.definition()

#Exercice 2
import random

class MyList:
    def __init__(self, letters):
        self.letters = letters

    def reverse(self):
        return self.letters[::-1]

    def sort(self):
        return sorted(self.letters)

    def random_list(self):
        return [random.randint(1, 100) for _ in range(len(self.letters))]
mylist = MyList(['z', 'a', 'm', 'b', 'x'])

print(f"Liste originale : {mylist.letters}")
print(f"Liste inversée : {mylist.reverse()}")
print(f"Liste triée : {mylist.sort()}")
print(f"Liste de nombres aléatoires : {mylist.random_list()}")

#Exercice 3
class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]

    def add_item(self, name, price, spice, gluten):
        self.menu += [{"name": name, "price": price, "spice": spice, "gluten": gluten}]
        print(f"{name} a été ajouté au menu.")

    def update_item(self, name, price, spice, gluten):
        for item in self.menu:
            if item["name"] == name:
                item["price"] = price
                item["spice"] = spice
                item["gluten"] = gluten
                print(f"{name} a été mis à jour.")
                return
        print(f"{name} n'est pas au menu.")

    def remove_item(self, name):
        for item in self.menu:
            if item["name"] == name:
                self.menu.remove(item)
                print(f"{name} a été supprimé du menu.")
                print(f"Menu actuel : {self.menu}")
                return
        print(f"{name} n'est pas au menu.")

    def display_menu(self):
        print("\n=== Menu du Restaurant ===")
        for item in self.menu:
            print(f"{item['name']} - ${item['price']} - Épice: {item['spice']} - Gluten: {item['gluten']}")

manager = MenuManager()
manager.display_menu()

manager.add_item("Pizza", 12, "A", True)
manager.display_menu()

manager.update_item("Soup", 12, "C", False)
manager.display_menu()

manager.remove_item("French Fries")

manager.remove_item("Pasta")