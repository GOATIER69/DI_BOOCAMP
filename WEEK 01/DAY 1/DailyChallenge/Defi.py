#Défi 1
number = int(input("Entrez un nombre : "))
length = int(input("Entrez une longueur : "))

multiples = [number * i for i in range(1, length + 1)]
print(multiples)

#Défi 2
mot = input("Entrez un mot : ")

resultat = ""
for lettre in mot:
    if resultat == "" or lettre != resultat[-1]:
        resultat += lettre

print(resultat)