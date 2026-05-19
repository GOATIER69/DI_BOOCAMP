#Exercice1
mois = int(input("Entrez un mois (1-12) : "))

if 3 <= mois <= 5:
    print("Spring")
elif 6 <= mois <= 8:
    print("Summer")
elif 9 <= mois <= 11:
    print("Autumn")
elif mois == 12 or 1 <= mois <= 2:
    print("Winter")
else:
    print("Mois invalide, entrez un nombre entre 1 et 12.")

#Exercice 2
for i in range(1, 21):
    print(i)

nombres = list(range(1, 21))
for i in range(0, len(nombres), 2):
    print(nombres[i])
    
#Exercice 3
while True:
    nom = input("Entrez votre nom : ")
    if nom == "Kouame":
        print("Bienvenue, Kouame !")
        break
    
#Exercice 4
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

name = input("Entrez un nom : ")

if name in names:
    print(names.index(name))
else:
    print(f"{name} n'est pas dans la liste.")
    
#Exercice 5
n1 = int(input("Input the 1st number: "))
n2 = int(input("Input the 2nd number: "))
n3 = int(input("Input the 3rd number: "))

print(f"The greatest number is: {max(n1, n2, n3)}")

#Exercice 6
import random

gagne = 0
perdu = 0

while True:
    essai = int(input("Devinez un nombre entre 1 et 9 : "))
    nombre_aleatoire = random.randint(1, 9)
    
    print(f"Le nombre était : {nombre_aleatoire}")
    
    if essai == nombre_aleatoire:
        print("Gagnant ! 🎉")
        gagne += 1
    else:
        print("Meilleure chance la prochaine fois !")
        perdu += 1
    
    rejouer = input("Voulez-vous rejouer ? (oui/non) : ")
    if rejouer.lower() != "oui":
        break

print(f"\n--- Résultats finaux ---")
print(f"Parties gagnées : {gagne}")
print(f"Parties perdues : {perdu}")
print(f"Total de parties : {gagne + perdu}")