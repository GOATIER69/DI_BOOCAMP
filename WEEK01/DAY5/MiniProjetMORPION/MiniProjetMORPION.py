#MiniProjet_MORPION
def display_board(board):
    """Affiche le plateau de Tic Tac Toe"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def display_positions():
    """Affiche les positions disponibles"""
    print("Positions disponibles :")
    print(" 0 | 1 | 2 ")
    print("---|---|---")
    print(" 3 | 4 | 5 ")
    print("---|---|---")
    print(" 6 | 7 | 8 ")
    print()


def player_input(board, player):
    """Obtient la position du joueur et effectue le coup"""
    while True:
        try:
            position = int(input(f"Joueur {player}, entrez votre coup (0-8): "))
            
            if position < 0 or position > 8:
                print("❌ Veuillez entrer un nombre entre 0 et 8.")
                continue
            
            if board[position] != ' ':
                print("❌ Cette case est déjà occupée!")
                continue
            
            board[position] = player
            break
        except ValueError:
            print("❌ Veuillez entrer un nombre valide.")


def check_win(board, player):
    """Vérifie si le joueur a gagné"""
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
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    
    return False


def is_board_full(board):
    """Vérifie si le plateau est plein"""
    return ' ' not in board


def switch_player(current_player):
    """Change le joueur actuel"""
    return 'O' if current_player == 'X' else 'X'


def play():
    """Fonction principale qui lance le jeu"""
    print("="*40)
    print("BIENVENUE AU TIC TAC TOE!")
    print("="*40)
    print("Joueur 1 = X")
    print("Joueur 2 = O")
    print("="*40)
    
    board = [' ' for _ in range(9)]
    current_player = 'X'
    game_over = False
    
    display_positions()
    
    while not game_over:
        display_board(board)
        
        player_input(board, current_player)
        
        if check_win(board, current_player):
            display_board(board)
            print(f"🎉 Joueur {current_player} a gagné!")
            game_over = True
            break
        
        if is_board_full(board):
            display_board(board)
            print("🤝 Match nul! Le plateau est plein.")
            game_over = True
            break
        
        current_player = switch_player(current_player)
    
    while True:
        replay = input("Voulez-vous rejouer? (oui/non): ").lower()
        if replay in ['oui', 'o', 'yes', 'y']:
            play()
            break
        elif replay in ['non', 'n', 'no']:
            print("Merci d'avoir joué! Au revoir! 👋")
            break
        else:
            print("Veuillez entrer 'oui' ou 'non'")


if __name__ == "__main__":
    play()