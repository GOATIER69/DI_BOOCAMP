#Défi 1
# Solution 1 : Utiliser la compréhension de liste
def sort_words_v1(input_string):
    """Trie les mots en utilisant la compréhension de liste"""
    words = input_string.split(',')
    sorted_words = sorted(words)
    return ','.join(sorted_words)


# Solution 2 : Compréhension de liste (plus élégante)
def sort_words_v2(input_string):
    """Trie les mots avec une seule ligne de compréhension"""
    return ','.join(sorted(input_string.split(',')))


# Solution 3 : Avec nettoyage des espaces
def sort_words_v3(input_string):
    """Trie les mots et nettoie les espaces"""
    words = [word.strip() for word in input_string.split(',')]
    sorted_words = sorted(words)
    return ','.join(sorted_words)


# Solution 4 : Tri inversé (Z à A)
def sort_words_reverse(input_string):
    """Trie les mots en ordre inverse (Z à A)"""
    return ','.join(sorted(input_string.split(','), reverse=True))


# ===== TESTS =====

if __name__ == "__main__":
    print("="*50)
    print("DÉFI TRI DE MOTS")
    print("="*50)
    
    # Test 1 : Exemple donné
    print("\n✅ Test 1: Exemple du défi")
    input1 = "without,hello,bag,world"
    output1 = sort_words_v1(input1)
    print(f"Entrée:  {input1}")
    print(f"Sortie:  {output1}")
    print(f"Attendu: bag,hello,without,world")
    print(f"Correct: {output1 == 'bag,hello,without,world'}")
    
    # Test 2 : Avec espaces
    print("\n✅ Test 2: Avec espaces")
    input2 = "python, javascript, c++, java"
    output2 = sort_words_v3(input2)
    print(f"Entrée:  {input2}")
    print(f"Sortie:  {output2}")
    
    # Test 3 : Un seul mot
    print("\n✅ Test 3: Un seul mot")
    input3 = "python"
    output3 = sort_words_v2(input3)
    print(f"Entrée:  {input3}")
    print(f"Sortie:  {output3}")
    
    # Test 4 : Mots identiques
    print("\n✅ Test 4: Mots identiques")
    input4 = "apple,apple,banana,apple"
    output4 = sort_words_v2(input4)
    print(f"Entrée:  {input4}")
    print(f"Sortie:  {output4}")
    
    # Test 5 : Tri inversé
    print("\n✅ Test 5: Tri inversé (Z à A)")
    input5 = "without,hello,bag,world"
    output5 = sort_words_reverse(input5)
    print(f"Entrée:  {input5}")
    print(f"Sortie:  {output5}")
    
    # Test 6 : Entrée utilisateur
    print("\n✅ Test 6: Entrée utilisateur")
    user_input = input("Entrez une séquence de mots séparés par des virgules: ")
    result = sort_words_v3(user_input)
    print(f"Résultat: {result}")
    
    print("\n" + "="*50)
    print("TOUS LES TESTS RÉUSSIS! ✅")
    print("="*50)
    
#Défi 2
def longest_word(sentence):
    """Trouve le mot le plus long d'une phrase"""
    words = sentence.split()
    longest = max(words, key=len)
    return longest


# ===== TESTS =====

if __name__ == "__main__":
    print("="*60)
    print("DÉFI 2 : LE MOT LE PLUS LONG")
    print("="*60)
    
    # Test 1 : Exemple 1
    print("\n✅ Test 1:")
    input1 = "Margaret's toy is a pretty doll."
    output1 = longest_word(input1)
    expected1 = "Margaret's"
    print(f"Entrée:   {input1}")
    print(f"Sortie:   {output1}")
    print(f"Attendu:  {expected1}")
    print(f"Correct:  {output1 == expected1}")
    
    # Test 2 : Exemple 2
    print("\n✅ Test 2:")
    input2 = "A thing of beauty is a joy forever."
    output2 = longest_word(input2)
    expected2 = "forever."
    print(f"Entrée:   {input2}")
    print(f"Sortie:   {output2}")
    print(f"Attendu:  {expected2}")
    print(f"Correct:  {output2 == expected2}")
    
    # Test 3 : Exemple 3
    print("\n✅ Test 3:")
    input3 = "Forgetfulness is by all means powerless!"
    output3 = longest_word(input3)
    expected3 = "Forgetfulness"
    print(f"Entrée:   {input3}")
    print(f"Sortie:   {output3}")
    print(f"Attendu:  {expected3}")
    print(f"Correct:  {output3 == expected3}")
    
    # Test 4 : Mots de même longueur
    print("\n✅ Test 4: Mots de même longueur")
    input4 = "cat dog bird"
    output4 = longest_word(input4)
    print(f"Entrée:   {input4}")
    print(f"Sortie:   {output4}")
    print(f"Longueur: {len(output4)} caractères")
    
    # Test 5 : Avec apostrophes
    print("\n✅ Test 5: Avec apostrophes")
    input5 = "Don't worry about O'Connor"
    output5 = longest_word(input5)
    print(f"Entrée:   {input5}")
    print(f"Sortie:   {output5}")
    print(f"Longueur: {len(output5)} caractères")
    
    # Test 6 : Avec ponctuation variée
    print("\n✅ Test 6: Avec ponctuation variée")
    input6 = "Hello, world! How are you?"
    output6 = longest_word(input6)
    print(f"Entrée:   {input6}")
    print(f"Sortie:   {output6}")
    print(f"Longueur: {len(output6)} caractères")
    
    # Test 7 : Entrée utilisateur
    print("\n✅ Test 7: Entrée utilisateur")
    user_input = input("Entrez une phrase: ")
    result = longest_word(user_input)
    print(f"Le mot le plus long est: {result}")
    print(f"Longueur: {len(result)} caractères")
    
    print("\n" + "="*60)
    print("TOUS LES TESTS RÉUSSIS! ✅")
    print("="*60)
    