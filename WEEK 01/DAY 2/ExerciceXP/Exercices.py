#Exercice 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionnaire = dict(zip(keys, values))
print(dictionnaire)

#Exercice 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total = 0

for membre, age in family.items():
    if age < 3:
        prix = 0
    elif 3 <= age <= 12:
        prix = 10
    else:
        prix = 15

    total += prix
    print(f"{membre.capitalize()} ({age} ans) : {prix} $")

print(f"\nCoût total : {total} $")


family = {}
n = int(input("Combien de membres dans la famille ? "))

for _ in range(n):
    nom = input("Nom : ")
    age = int(input(f"Âge de {nom} : "))
    family[nom] = age

total = 0
print()

for membre, age in family.items():
    if age < 3:
        prix = 0
    elif 3 <= age <= 12:
        prix = 10
    else:
        prix = 15

    total += prix
    print(f"{membre.capitalize()} ({age} ans) : {prix} $")

print(f"\nCoût total : {total} $")

#Exercice 3
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2
print(f"Zara sells clothes for : {', '.join(brand['type_of_clothes'])}.")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
brand.pop("creation_date")
print(f"Last competitor : {brand['international_competitors'][-1]}")
print(f"Major colors in the US : {', '.join(brand['major_color']['US'])}")
print(f"Number of keys : {len(brand)}")
print(f"All keys : {list(brand.keys())}")

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 7000
}
brand.update(more_on_zara)
print(f"\nDictionnaire fusionné :\n{brand}")

#Exercice 4
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")

#Exercice 5
import random

def compare_numbers(number):
    random_number = random.randint(1,100)
    
    if number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {number}, Random number: {random_number}")

compare_numbers(50)

#Exercice 6
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

make_shirt()
make_shirt(size="medium")
make_shirt(size="small", text="Custom message")

#Exercice 7
import random

def get_random_temp(saison=None):
    if saison == "winter":
        return round(random.uniform(-10, 5), 1)
    elif saison == "spring":
        return round(random.uniform(10, 20), 1)
    elif saison == "summer":
        return round(random.uniform(25, 40), 1)
    elif saison == "autumn":
        return round(random.uniform(5, 15), 1)
    else:
        return round(random.uniform(-10, 40), 1)

def get_saison(mois):
    if mois in [12, 1, 2]:
        return "winter"
    elif mois in [3, 4, 5]:
        return "spring"
    elif mois in [6, 7, 8]:
        return "summer"
    else:
        return "autumn"

def main():
    mois = int(input("Entrez un mois (1-12) : "))
    saison = get_saison(mois)
    print(f"Saison : {saison.capitalize()}")

    temp = get_random_temp(saison)
    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp < 0:
        print("Brrr, il fait un froid de canard ! Mets des vêtements supplémentaires aujourd'hui.")
    elif temp <= 16:
        print("Il fait assez froid ! N'oublie pas ton manteau.")
    elif temp <= 23:
        print("Beau temps !")
    elif temp <= 32:
        print("Il fait un peu chaud, pensez à bien vous hydrater.")
    else:
        print("Il fait vraiment chaud ! Reste au frais.")

main()

#Exercice 8
toppings = []
prix_base = 10
prix_topping = 2.50

while True:
    topping = input("Entrez une garniture (ou 'quit' pour terminer) : ")
    
    if topping == "quit":
        break
    
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

print(f"\nYour pizza toppings : {', '.join(toppings)}")
print(f"Total price : ${prix_base + len(toppings) * prix_topping:.2f}")

