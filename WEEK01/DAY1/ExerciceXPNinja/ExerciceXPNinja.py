#Exercice 1
3 <= 3 < 9
True

3 == 3 == 3
True

bool(0)
False

bool(5 == "5")
False

bool(4 == 4) == bool("4" == "4")
True

bool(bool(None))
False

x is True
y is False
a: 5

#Exercice 2
record = 0

while True:
    phrase = input("Entrez la phrase la plus longue possible sans le caractère 'A' : ")
    
    if 'A' in phrase or 'a' in phrase:
        print("❌ Votre phrase contient la lettre 'A' !")
    else:
        longueur = len(phrase)
        if longueur > record:
            record = longueur
            print(f"🎉 Félicitations ! Nouveau record : {record} caractères !")
        else:
            print(f"Longueur : {longueur} caractères. Record actuel : {record} caractères.")
            
#Exercice 3
paragraphe = """
The Python programming language was created by Guido van Rossum and first released in 1991. 
Python is designed to be easy to read and simple to implement. 
It is open source, which means it is free to use. 
Python is a general-purpose language, meaning it can be used to create many different types of programs. 
It is not specialized for any specific type of problem. 
This versatility, along with its beginner-friendly nature, makes Python one of the most popular programming languages in the world today.
"""

nb_caracteres = len(paragraphe)

phrases = [p.strip() for p in paragraphe.replace('!', '.').replace('?', '.').split('.') if p.strip()]
nb_phrases = len(phrases)

mots = paragraphe.split()
nb_mots = len(mots)

mots_minuscules = [m.strip('.,!?;:').lower() for m in mots]
nb_mots_uniques = len(set(mots_minuscules))

nb_caracteres_non_blancs = len(paragraphe.replace(' ', '').replace('\n', ''))
moyenne_mots_par_phrase = round(nb_mots / nb_phrases, 2)
nb_mots_non_uniques = nb_mots - nb_mots_uniques

print(f"""
========== Analyse du paragraphe ==========
📝 Nombre de caractères         : {nb_caracteres}
🔤 Nombre de caractères non blancs : {nb_caracteres_non_blancs}
📖 Nombre de phrases            : {nb_phrases}
💬 Nombre de mots               : {nb_mots}
✨ Nombre de mots uniques       : {nb_mots_uniques}
🔁 Nombre de mots non uniques   : {nb_mots_non_uniques}
📊 Moyenne de mots par phrase   : {moyenne_mots_par_phrase}
============================================
""")