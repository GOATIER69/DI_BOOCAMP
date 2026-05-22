#Défi
from googletrans import Translator

def translate_french_to_english():
    """Traduit une liste de mots français en anglais"""
    french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
    
    # Créer un traducteur
    translator = Translator()
    
    # Créer un dictionnaire pour stocker les traductions
    translation_dict = {}
    
    # Traduire chaque mot
    for word in french_words:
        translation = translator.translate(word, src='fr', dest='en')
        translation_dict[word] = translation.text
    
    return translation_dict


def translate_french_to_english_compact():
    """Version compacte avec compréhension de dictionnaire"""
    french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
    translator = Translator()
    
    # Compréhension de dictionnaire
    return {word: translator.translate(word, src='fr', dest='en').text
            for word in french_words}


# ===== TESTS =====

if __name__ == "__main__":
    print("="*60)
    print("TRADUCTION FRANÇAIS → ANGLAIS")
    print("="*60)
    
    # Test 1 : Afficher la liste originale
    print("\n✅ Liste originale (français):")
    french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
    print(french_words)
    
    # Test 2 : Traduction simple
    print("\n✅ Traduction (Méthode 1):")
    try:
        result1 = translate_french_to_english()
        print(result1)
        
        # Vérifier le résultat
        expected = {
            "Bonjour": "Hello",
            "Au revoir": "Goodbye",
            "Bienvenue": "Welcome",
            "A bientôt": "See you soon"
        }
        print(f"\nRésultat attendu:")
        print(expected)
        
    except Exception as e:
        print(f"Erreur: {e}")
    
    # Test 3 : Traduction compacte
    print("\n✅ Traduction (Méthode 2 - Compacte):")
    try:
        result2 = translate_french_to_english_compact()
        print(result2)
    except Exception as e:
        print(f"Erreur: {e}")
    
    # Test 4 : Afficher les traductions de manière formatée
    print("\n✅ Format tableau:")
    try:
        translator = Translator()
        for word in french_words:
            translation = translator.translate(word, src='fr', dest='en')
            print(f"{word:20} → {translation.text}")
    except Exception as e:
        print(f"Erreur: {e}")
    
    print("\n" + "="*60)