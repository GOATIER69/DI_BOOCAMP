matrix = """7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!"""

lignes = matrix.split('\n')
grille = [list(ligne) for ligne in lignes]

texte_brut = ""
for col in range(len(grille[0])):
    for row in range(len(grille)):
        texte_brut += grille[row][col]

message = ""
for char in texte_brut:
    if char.isalpha():
        message += char
    else:
        if message and not message.endswith(" "):
            message += " "

print(message.strip())