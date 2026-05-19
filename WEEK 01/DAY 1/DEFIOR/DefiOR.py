#Défi
from datetime import date

# Saisie de la date de naissance
naissance = input("Entrez votre date de naissance (JJ/MM/AAAA) : ")
jour, mois, annee = map(int, naissance.split('/'))

# Calcul de l'âge
aujourd_hui = date.today()
age = aujourd_hui.year - annee
if (aujourd_hui.month, aujourd_hui.day) < (mois, jour):
    age -= 1

# Nombre de bougies = dernier chiffre de l'âge
nb_bougies = age % 10
if nb_bougies == 0:
    nb_bougies = 1

# Année bissextile ?
bissextile = (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

# Génération du gâteau
def gateau(nb_bougies):
    bougies = "i" * nb_bougies
    espace_haut = " " * ((17 - len(bougies)) // 2)
    print(f"       ___{bougies}___")
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~")

# Affichage
print(f"\n🎂 Vous avez {age} ans — {nb_bougies} bougie(s) !\n")
gateau(nb_bougies)

if bissextile:
    print(f"\n🎉 Vous êtes né(e) une année bissextile ! Voici un deuxième gâteau !\n")
    gateau(nb_bougies)