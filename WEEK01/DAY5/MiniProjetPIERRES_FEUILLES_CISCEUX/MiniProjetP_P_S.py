#Mini_projet_Pierre_Feuille_Ciseaux
from Game import Game

def get_user_menu_choice():
    """Affiche le menu et récupère le choix de l'utilisateur sans boucle interne."""
    print("\n--- MENU PRINCIPAL ---")
    print("1. Jouer une nouvelle partie")
    print("2. Afficher les scores actuels")
    print("q. Quitter le jeu")
    
    choice = input("Votre choix : ").strip().lower()
    return choice

def print_results(results):
    """Affiche le récapitulatif final des scores de manière conviviale."""
    print("\n=================================");
    print("📊 RÉCAPITULATIF DES SCORES 📊")
    print("=================================")
    print(f"🏆 Victoires : {results['win']}")
    print(f"❌ Défaites  : {results['loss']}")
    print(f"🤝 Matchs nuls: {results['draw']}")
    print("=================================")
    print("Merci d'avoir joué avec nous ! À bientôt ! 👋\n")

def main():
    # Initialisation du dictionnaire des scores selon le format demandé
    scores = {"win": 0, "loss": 0, "draw": 0}
    
    print("Bienvenue dans le jeu Pierre, Feuille, Ciseaux ! 🪨 📄 ✂️")
    
    while True:
        choice = get_user_menu_choice()
        
        if choice == "1":
            # Création d'une instance de la classe Game et lancement de la partie
            match = Game()
            game_result = match.play()
            
            # Mise à jour du dictionnaire des scores en fonction du retour de play()
            if game_result == "victoire":
                scores["win"] += 1
            elif game_result == "défaite":
                scores["loss"] += 1
            elif game_result == "match nul":
                scores["draw"] += 1
                
        elif choice == "2":
            # Option bonus pour voir les scores sans quitter
            print(f"\nScores actuels -> Victoires: {scores['win']} | Défaites: {scores['loss']} | Nuls: {scores['draw']}")
            
        elif choice in ["q", "x"]:
            # Fin du programme et affichage des résultats
            print_results(scores)
            break
            
        else:
            print("Option indisponible. Veuillez choisir 1, 2 ou q.")

if __name__ == "__main__":
    main()