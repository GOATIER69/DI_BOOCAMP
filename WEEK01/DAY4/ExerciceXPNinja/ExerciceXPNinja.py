#Exercice
import time
import os

class Cell:
    def __init__(self, alive=False):
        self.alive = alive
    
    def __str__(self):
        return "█" if self.alive else "░"


class Grid:
    def __init__(self, width, height, initial_state=None):
        self.width = width
        self.height = height
        self.generation = 0
        
        if initial_state:
            self.cells = initial_state
        else:
            self.cells = [[Cell(False) for _ in range(width)] for _ in range(height)]
    
    def count_alive_neighbors(self, row, col):
        """Compte les cellules vivantes voisines"""
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                
                new_row = row + i
                new_col = col + j
                
                if 0 <= new_row < self.height and 0 <= new_col < self.width:
                    if self.cells[new_row][new_col].alive:
                        count += 1
        
        return count
    
    def next_generation(self):
        """Applique les règles du Jeu de la Vie"""
        new_cells = [[Cell(False) for _ in range(self.width)] for _ in range(self.height)]
        
        for row in range(self.height):
            for col in range(self.width):
                alive_neighbors = self.count_alive_neighbors(row, col)
                is_alive = self.cells[row][col].alive
                
                if is_alive:
    
                    if alive_neighbors in [2, 3]:
                        new_cells[row][col].alive = True
                else:
                    
                    if alive_neighbors == 3:
                        new_cells[row][col].alive = True
        
        self.cells = new_cells
        self.generation += 1
    
    def display(self):
        """Affiche la grille"""
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"Génération {self.generation}")
        print("+" + "-" * self.width + "+")
        for row in self.cells:
            print("|" + "".join(str(cell) for cell in row) + "|")
        print("+" + "-" * self.width + "+")
    
    def count_alive(self):
        """Compte le nombre de cellules vivantes"""
        count = 0
        for row in self.cells:
            for cell in row:
                if cell.alive:
                    count += 1
        return count

class GameOfLife:
    def __init__(self, width, height, initial_state=None):
        self.grid = Grid(width, height, initial_state)
    
    def set_alive(self, row, col):
        """Rend une cellule vivante"""
        if 0 <= row < self.grid.height and 0 <= col < self.grid.width:
            self.grid.cells[row][col].alive = True
    
    def run(self, generations=100, speed=0.5):
        """Lance le jeu pour un nombre de générations"""
        self.grid.display()
        input("Appuyez sur Entrée pour commencer...")
        
        for _ in range(generations):
            time.sleep(speed)
            self.grid.next_generation()
            self.grid.display()
            print(f"Cellules vivantes: {self.grid.count_alive()}")
            
            if self.grid.count_alive() == 0:
                print("Toutes les cellules sont mortes!")
                break

print("Test 1: Blinker")
game1 = GameOfLife(10, 10)
game1.set_alive(5, 4)
game1.set_alive(5, 5)
game1.set_alive(5, 6)
game1.run(10, speed=0.3)

print("\n" + "="*50 + "\n")

print("Test 2: Glisseur (Glider)")
game2 = GameOfLife(15, 15)
game2.set_alive(2, 3)
game2.set_alive(3, 4)
game2.set_alive(4, 2)
game2.set_alive(4, 3)
game2.set_alive(4, 4)
game2.run(20, speed=0.3)

print("\n" + "="*50 + "\n")

print("Test 3: Bloc (Stable)")
game3 = GameOfLife(10, 10)
game3.set_alive(4, 4)
game3.set_alive(4, 5)
game3.set_alive(5, 4)
game3.set_alive(5, 5)
game3.run(10, speed=0.3)

print("\n" + "="*50 + "\n")

print("Test 4: Beehive (Stable)")
game4 = GameOfLife(12, 10)
game4.set_alive(3, 3)
game4.set_alive(3, 4)
game4.set_alive(4, 2)
game4.set_alive(4, 5)
game4.set_alive(5, 3)
game4.set_alive(5, 4)
game4.run(10, speed=0.3)
