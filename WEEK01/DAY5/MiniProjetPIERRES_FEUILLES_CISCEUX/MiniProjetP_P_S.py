#Mini_projet_1
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] 
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
    
    def display_board(self):
        """Affiche le plateau de jeu"""
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---|---|---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---|---|---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\n")
    
    def display_positions(self):
        """Affiche les positions disponibles"""
        print("Positions disponibles :")
        print(" 0 | 1 | 2 ")
        print("---|---|---")
        print(" 3 | 4 | 5 ")
        print("---|---|---")
        print(" 6 | 7 | 8 ")
        print()
    
    def is_valid_move(self, position):
        """Vérifie si un coup est valide"""
        if position < 0 or position > 8:
            return False
        if self.board[position] != ' ':
            return False
        return True
    
    def make_move(self, position):
        """Effectue un coup"""
        if self.is_valid_move(position):
            self.board[position] = self.current_player
            return True
        return False
    
    def check_winner(self):
        """Vérifie s'il y a un gagnant"""
        winning_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] 
                and self.board[combo[0]] != ' '):
                self.winner = self.board[combo[0]]
                self.game_over = True
                return True
        
        return False
    
    def check_board_full(self):
        """Vérifie si le plateau est plein (match nul)"""
        if ' ' not in self.board:
            self.game_over = True
            return True
        return False
    
    def switch_player(self):
        """Change le joueur actuel"""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def play(self):
        """Lance la boucle principale du jeu"""
        print("="*40)
        print("BIENVENUE AU MORPION!")
        print("="*40)
        print("Joueur 1 = X")
        print("Joueur 2 = O")
        print("="*40)
        
        self.display_positions()
        
        while not self.game_over:
            self.display_board()
            
            while True:
                try:
                    position = int(input(f"Joueur {self.current_player}, entrez votre coup (0-8): "))
                    if self.make_move(position):
                        break
                    else:
                        print("❌ Coup invalide! Cette case est occupée ou position invalide.")
                except ValueError:
                    print("❌ Veuillez entrer un nombre valide entre 0 et 8.")
            
            if self.check_winner():
                self.display_board()
                print(f"🎉 Joueur {self.winner} a gagné!")
                break
        
            if self.check_board_full():
                self.display_board()
                print("🤝 Match nul! Le plateau est plein.")
                break
           
            self.switch_player()
       
        self.ask_replay()
    
    def ask_replay(self):
        """Demande si les joueurs veulent rejouer"""
        while True:
            replay = input("Voulez-vous rejouer? (oui/non): ").lower()
            if replay in ['oui', 'o', 'yes', 'y']:
                self.__init__()  
                break
            elif replay in ['non', 'n', 'no']:
                print("Merci d'avoir joué! Au revoir! ")
                break
            else:
                print("Veuillez entrer 'oui' ou 'non'")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
    
    
#Mini_projet_2
import random
from enum import Enum

class Choice(Enum):
    """Énumération des choix possibles"""
    PIERRE = "pierre"
    FEUILLE = "feuille"
    CISEAUX = "ciseaux"


class Player:
    """Classe représentant un joueur"""
    def __init__(self, name, is_computer=False):
        self.name = name
        self.is_computer = is_computer
        self.score = 0
        self.choice = None
    
    def choose(self):
        """Le joueur fait un choix"""
        if self.is_computer:
            self.choice = random.choice(list(Choice))
            print(f"{self.name} a choisi... (secrètement)")
        else:
            while True:
                try:
                    print(f"\n{self.name}, faites votre choix:")
                    print("1. Pierre")
                    print("2. Feuille")
                    print("3. Ciseaux")
                    choice_num = int(input("Entrez 1, 2 ou 3: "))
                    
                    if choice_num == 1:
                        self.choice = Choice.PIERRE
                        print(f"{self.name} a choisi: Pierre 🪨")
                        break
                    elif choice_num == 2:
                        self.choice = Choice.FEUILLE
                        print(f"{self.name} a choisi: Feuille 📄")
                        break
                    elif choice_num == 3:
                        self.choice = Choice.CISEAUX
                        print(f"{self.name} a choisi: Ciseaux ✂️")
                        break
                    else:
                        print("❌ Choix invalide! Entrez 1, 2 ou 3.")
                except ValueError:
                    print("❌ Veuillez entrer un nombre valide.")
    
    def add_score(self):
        """Ajoute 1 point au joueur"""
        self.score += 1
    
    def reset_score(self):
        """Réinitialise le score"""
        self.score = 0
    
    def __str__(self):
        return f"{self.name} (Score: {self.score})"


class Game:
    """Classe principale du jeu Pierre-Feuille-Ciseaux"""
    def __init__(self, player1_name="Joueur 1", play_vs_computer=True):
        self.player1 = Player(player1_name, is_computer=False)
        self.player2 = Player("Ordinateur", is_computer=True) if play_vs_computer else Player("Joueur 2", is_computer=False)
        self.round_number = 0
    
    def determine_winner(self):
        """Détermine le gagnant du round"""
        choice1 = self.player1.choice
        choice2 = self.player2.choice
        
        if choice1 == choice2:
            return None
       
        if (choice1 == Choice.PIERRE and choice2 == Choice.CISEAUX) or \
           (choice1 == Choice.FEUILLE and choice2 == Choice.PIERRE) or \
           (choice1 == Choice.CISEAUX and choice2 == Choice.FEUILLE):
            return self.player1
        
        return self.player2
    
    def display_round_result(self):
        """Affiche le résultat du round"""
        print("\n" + "="*50)

        choice1_str = self.player1.choice.value if self.player1.choice is not None else "Aucun"
        choice2_str = self.player2.choice.value if self.player2.choice is not None else "Aucun"
        print(f"{self.player1.name}: {choice1_str} 🆚 {self.player2.name}: {choice2_str}")
        
        winner = self.determine_winner()
        if winner is None:
            print("✋ Match nul!")
        else:
            print(f"🎉 {winner.name} gagne ce round!")
            winner.add_score()
        print("="*50)
    
    def play_round(self):
        """Joue un round"""
        self.round_number += 1
        print(f"\n🎮 ROUND {self.round_number}")
        
        self.player1.choose()
        self.player2.choose()
        
        self.display_round_result()
    
    def display_scores(self):
        """Affiche les scores actuels"""
        print("\n📊 SCORES:")
        print(f"{self.player1}: {self.player1.score}")
        print(f"{self.player2}: {self.player2.score}")
    
    def play_series(self, num_rounds=3):
        """Joue une série de rounds"""
        print("="*50)
        print("BIENVENUE AU PIERRE-FEUILLE-CISEAUX!")
        print("="*50)
        
        for _ in range(num_rounds):
            self.play_round()
            self.display_scores()
        
        self.display_final_result()
    
    def display_final_result(self):
        """Affiche le résultat final"""
        print("\n" + "="*50)
        print("RÉSULTAT FINAL")
        print("="*50)
        self.display_scores()
        
        if self.player1.score > self.player2.score:
            print(f"\n🏆 {self.player1.name} remporte la série!")
        elif self.player2.score > self.player1.score:
            print(f"\n🏆 {self.player2.name} remporte la série!")
        else:
            print("\n🤝 Égalité parfaite!")
        print("="*50)
    
    def play_until_quit(self):
        """Joue des rounds jusqu'à ce que l'utilisateur quitte"""
        print("="*50)
        print("BIENVENUE AU PIERRE-FEUILLE-CISEAUX!")
        print("="*50)
        
        while True:
            self.play_round()
            self.display_scores()
            
            continue_game = input("\nVoulez-vous jouer un autre round? (oui/non): ").lower()
            if continue_game not in ['oui', 'o', 'yes', 'y']:
                self.display_final_result()
                break

if __name__ == "__main__":
    print("Choisissez le mode de jeu:")
    print("1. Jouer contre l'ordinateur (série de 3 rounds)")
    print("2. Jouer contre l'ordinateur (rounds illimités)")
    print("3. Jouer contre un autre joueur (série de 3 rounds)")
    
    choice = input("Entrez 1, 2 ou 3: ")
    
    if choice == "1":
        player_name = input("Entrez votre nom: ")
        game = Game(player_name, play_vs_computer=True)
        game.play_series(3)
    elif choice == "2":
        player_name = input("Entrez votre nom: ")
        game = Game(player_name, play_vs_computer=True)
        game.play_until_quit()
    elif choice == "3":
        player1_name = input("Nom du Joueur 1: ")
        player2_name = input("Nom du Joueur 2: ")
        game = Game(player1_name, play_vs_computer=False)
        game.player2.name = player2_name
        game.player2.is_computer = False
        game.play_series(3)
    else:
        print("Choix invalide!")