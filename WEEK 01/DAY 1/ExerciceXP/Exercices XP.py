#Exercice 1
print("hello world !") * 4

#Exercice 2
resultat_puissance = 99**3
resultat_puissance
resultat_final = resultat_puissance * 8
print(resultat_final)

#Exercice 3
5 < 3 #False
3 == 3 #True
3 == "3" #False
"3" > 3 #False
"Hello" == "hello" #False

#Exercice 4
computer_brand = "Dell"
print(f"I have a {computer_brand} computer.")

#Exercice 5
name = "KOUAME"
age = 25
shoe_size = 42
info = f"Mon nom est {name}, j'ai {age}, ma taille de chaussure est {shoe_size}."
print(info)

#Exercice 6
a = 10
b = 5
if a > b:
    print("hello world")
    
#Exercice 7
#verifier_si_un_nombre_est_pair_ou_impair
nombre_str = input("Veuillez entrer un nombre entier : ")
try:
    nombre = int(nombre_str)
    if nombre % 2 == 0:
        print(f"{nombre} est un nombre pair essaie encore.")
    else:
        print(f"{nombre} est un nombre impair essaie encore.")
except ValueError:
    print("Entrée invalide : veuillez entrer un nombre entier.")
    
#Exercice 8
my_name = "KOUAME"
nom_utilisateur = input("Quel est votre nom d'utilisateur ? ")
if nom_utilisateur.lower() == my_name.lower():
    print("jumeaux !")
else:   print("pas des jumeaux !")

#Exercice 9
taille_str = input("Veuillez entrer votre taille en centimètres : ")
try:
    taille = float(taille_str)
    if taille >= 175:
        print("Vous êtes assez grand pour faire les montagnes russes !")
    else
        print("Désolé, vous n'êtes pas assez grand pour faire les montagnes russes.")