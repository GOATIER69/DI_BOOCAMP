#Mini_projet_Pierre_Feuille_Ciseaux
from Game import Game

def get_user_menu_choice():
    """Affiche le menu et récupère le choix de l'utilisateur."""
    print("\n--- MENU PRINCIPAL ---")
    print("1. Jouer une nouvelle partie")
    print("2. Afficher les scores actuels")
    print("q. Quitter le jeu")
    
    choice = input("Votre choix : ").strip().lower()
    return choice

def print_results(results):
    """Affiche le récapitulatif final des scores au format demandé {win: X, loss: Y, draw: Z}."""
    print("\n=================================");
    print("📊 RÉCAPITULATIF DES SCORES 📊")
    print("=================================")
    print(f"🏆 Victoires (wins)  : {results['win']}")
    print(f"❌ Défaites (losses) : {results['loss']}")
    print(f"🤝 Matchs nuls (draws): {results['draw']}")
    print("=================================")
    print("Merci d'avoir joué avec nous ! À bientôt ! 👋\n")

def main():
    # Initialisation du dictionnaire respectant exactement le format requis
    scores = {"win": 0, "loss": 0, "draw": 0}
    
    print("Bienvenue dans le jeu Pierre, Feuille, Ciseaux ! 🪨 📄 ✂️")
    
    while True:
        choice = get_user_menu_choice()
        
        if choice == "1":
            # Création de l'objet et appel de la méthode play()
            match = Game()
            game_result = match.play()
            
            # CORRECTION : On vérifie maintenant les clés anglaises renvoyées par play()
            if game_result == "win":
                scores["win"] += 1
            elif game_result == "loss":
                scores["loss"] += 1
            elif game_result == "draw":
                scores["draw"] += 1
                
        elif choice == "2":
            # Visualisation rapide des scores sans quitter
            print(f"\nScores actuels -> Victoires: {scores['win']} | Défaites: {scores['loss']} | Nuls: {scores['draw']}")
            
        elif choice in ["q", "x"]:
            # Appel de la fonction d'affichage final avant de couper le programme
            print_results(scores)
            break
            
        else:
            print("Option indisponible. Veuillez choisir 1, 2 ou q.")

if __name__ == "__main__":
    main()