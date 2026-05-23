import random

class Game:
    def __init__(self):
        # Liste des choix valides en français pour l'utilisateur
        self.valid_choices = ["pierre", "feuille", "ciseaux"]

    def get_user_item(self):
        """Demande à l'utilisateur de choisir un élément avec validation."""
        while True:
            user_choice = input("Choisissez (pierre, feuille, ciseaux) : ").strip().lower()
            if user_choice in self.valid_choices:
                return user_choice
            print("Choix invalide. Veuillez réessayer.")

    def get_computer_item(self):
        """Sélectionne aléatoirement un élément pour l'ordinateur."""
        return random.choice(self.valid_choices)

    def get_game_result(self, user_item, computer_item):
        """
        Détermine le résultat du match.
        Renvoie STRICTEMENT 'win', 'draw' ou 'loss' en anglais.
        """
        if user_item == computer_item:
            return "draw"
        
        # Logique des victoires
        win_conditions = {
            "pierre": "ciseaux",
            "feuille": "pierre",
            "ciseaux": "feuille"
        }
        
        if win_conditions[user_item] == computer_item:
            return "win"
        else:
            return "loss"

    def play(self):
        """Exécute une manche et renvoie le résultat en anglais."""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        
        # Affichage textuel pour l'utilisateur (en français pour l'expérience client)
        print(f"\nVous avez choisi : {user_item}.")
        print(f"L'ordinateur a choisi : {computer_item}.")
        
        if result == "win":
            print("👉 Vous avez gagné ! 🎉")
        elif result == "loss":
            print("👉 Vous avez perdu. 😢")
        else:
            print("👉 Match nul ! 🤝")
        print("-" * 30)
        
        # Renvoie impérativement 'win', 'loss' ou 'draw'
        return result