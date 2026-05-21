#Exercice 1
birthdays = {
    "Alice": "1990/03/15",
    "Bob": "1985/07/22",
    "Charlie": "2000/11/08",
    "Diana": "1995/01/30",
    "Eve": "1988/09/12"
}

print("Bienvenue !")
print("Vous pouvez consulter les dates d'anniversaire des personnes dans la liste !")

name = input("\nEntrez le nom : ")

if name in birthdays:
    print(f"L'anniversaire de {name} est le : {birthdays[name]}")
else:
    print(f"{name} n'est pas dans la liste.")
    
#Exercice 2
birthdays = {
    "Alice": "1990/03/15",
    "Bob": "1985/07/22",
    "Charlie": "2000/11/08",
    "Diana": "1995/01/30",
    "Eve": "1988/09/12"
}

print("Bienvenue !")
print("Vous pouvez consulter les dates d'anniversaire des personnes dans la liste !\n")

print("Personnes disponibles :")
for name in birthdays:
    print(f"  - {name}")

name = input("\nEntrez le nom : ")

if name in birthdays:
    print(f"L'anniversaire de {name} est le : {birthdays[name]}")
else:
    print(f"Désolé, nous ne disposons pas des informations concernant la date de naissance de {name}.")

#Exercice 3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

name = input("Entrez un nom : ")

if name in names:
    print(names.index(name))
else:
    print(f"{name} n'est pas dans la liste.")
    
#Exercice 4
import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    throws = 0
    while True:
        dice1 = throw_dice()
        dice2 = throw_dice()
        throws += 1
        if dice1 == dice2:
            return throws

def main():
    results = []
    
    for _ in range(100):
        results += [throw_until_doubles()]
    
    total = sum(results)
    moyenne = round(total / len(results), 2)
    
    print(f"Total throws: {total}")
    print(f"Average throws to reach doubles: {moyenne}.")

main()