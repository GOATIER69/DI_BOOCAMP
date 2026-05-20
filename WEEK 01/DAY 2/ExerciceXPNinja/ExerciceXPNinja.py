#Exercice 1
chaine = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
cars = chaine.split(", ")
print(f"Nombre de fabricants : {len(cars)}")
print(f"Ordre décroissant : {sorted(cars, reverse=True)}")
avec_o = len([car for car in cars if 'o' in car.lower()])
print(f"Fabricants contenant 'o' : {avec_o}")
sans_i = len([car for car in cars if 'i' not in car.lower()])
print(f"Fabricants ne contenant pas 'i' : {sans_i}")

cars_doublons = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
cars_unique = list(set(cars_doublons))
print(f"\n{', '.join(sorted(cars_unique))}")
print(f"Nombre d'entreprises sans doublons : {len(cars_unique)}")

cars_inversees = sorted([car[::-1] for car in cars])
print(f"\nFabricants triés (A-Z) avec lettres inversées : {cars_inversees}")

#Exercice 2
def get_full_name(first_name, last_name, middle_name=None):
    if middle_name:
        return f"{first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}"
    else:
        return f"{first_name.capitalize()} {last_name.capitalize()}"

print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
print(get_full_name(first_name="bruce", last_name="lee"))

#Exercice 3
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

# Dictionnaire inversé pour morse -> anglais
morse_inverse = {v: k for k, v in morse_code.items()}

def english_to_morse(text):
    result = []
    for word in text.upper().split():
        result += [' '.join(morse_code[letter] for letter in word if letter in morse_code)]
    return ' / '.join(result)

def morse_to_english(morse):
    result = []
    for word in morse.split(' / '):
        result += [''.join(morse_inverse[code] for code in word.split())]
    return ' '.join(result)


texte = "Hello World"
en_morse = english_to_morse(texte)
print(f"Anglais → Morse : {en_morse}")

en_anglais = morse_to_english(en_morse)
print(f"Morse → Anglais : {en_anglais}")