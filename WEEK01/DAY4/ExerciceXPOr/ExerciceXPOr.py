#Exercice
class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = False
    
    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            return True
        return False
    
    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("Authentification requise pour déposer de l'argent!")
        if amount <= 0:
            raise Exception("Le montant doit être positif!")
        self.balance += amount
        print(f"Dépôt de {amount}€ effectué. Solde actuel: {self.balance}€")
    
    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentification requise pour retirer de l'argent!")
        if amount <= 0:
            raise Exception("Le montant doit être positif!")
        if amount > self.balance:
            raise Exception("Solde insuffisant!")
        self.balance -= amount
        print(f"Retrait de {amount}€ effectué. Solde actuel: {self.balance}€")
    
    def __str__(self):
        return f"Compte de {self.username} - Solde: {self.balance}€"

class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance
    
    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentification requise pour retirer de l'argent!")
        if amount <= 0:
            raise Exception("Le montant doit être positif!")
        if amount > self.balance:
            raise Exception("Solde insuffisant!")
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Impossible de retirer! Le solde minimum est {self.minimum_balance}€")
        self.balance -= amount
        print(f"Retrait de {amount}€ effectué. Solde actuel: {self.balance}€")

class ATM:
    def __init__(self, account_list, try_limit=3):
        for account in account_list:
            if not isinstance(account, (BankAccount, MinimumBalanceAccount)):
                raise Exception("Tous les comptes doivent être des BankAccount ou MinimumBalanceAccount!")
        
        try:
            if try_limit <= 0:
                raise ValueError("try_limit doit être positif")
            self.try_limit = try_limit
        except (ValueError, TypeError):
            print("Valeur invalide pour try_limit, définie à 2 par défaut")
            self.try_limit = 2
        
        self.account_list = account_list
        self.current_tries = 0
        self.show_main_menu()
    
    def show_main_menu(self):
        while True:
            print("\n" + "="*40)
            print("GUICHET AUTOMATIQUE")
            print("="*40)
            print("1. Connexion")
            print("2. Quitter")
            
            choice = input("Choisissez une option: ")
            
            if choice == "1":
                username = input("Nom d'utilisateur: ")
                password = input("Mot de passe: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Au revoir!")
                break
            else:
                print("Choix invalide!")
    
    def log_in(self, username, password):
        for account in self.account_list:
            if account.authenticate(username, password):
                self.show_account_menu(account)
                return
        
        self.current_tries += 1
        print(f"Identifiants incorrects! Tentative {self.current_tries}/{self.try_limit}")
        
        if self.current_tries >= self.try_limit:
            print("Nombre maximal de tentatives atteint. Fermeture du programme.")
            exit()
        
        username = input("Nom d'utilisateur: ")
        password = input("Mot de passe: ")
        self.log_in(username, password)
    
    def show_account_menu(self, account):
        print(f"\nBienvenue {account.username}!")
        
        while True:
            print("\n" + "-"*40)
            print(f"Solde actuel: {account.balance}€")
            print("-"*40)
            print("1. Déposer de l'argent")
            print("2. Retirer de l'argent")
            print("3. Quitter")
            
            choice = input("Choisissez une option: ")
            
            try:
                if choice == "1":
                    amount = int(input("Montant à déposer: "))
                    account.deposit(amount)
                elif choice == "2":
                    amount = int(input("Montant à retirer: "))
                    account.withdraw(amount)
                elif choice == "3":
                    account.authenticated = False
                    print("Déconnexion effectuée.")
                    break
                else:
                    print("Choix invalide!")
            except ValueError:
                print("Entrée invalide! Veuillez entrer un nombre.")
            except Exception as e:
                print(f"Erreur: {e}")

if __name__ == "__main__":
    account1 = BankAccount("alice", "1234", 500)
    account2 = MinimumBalanceAccount("bob", "5678", 1000, minimum_balance=100)
    account3 = MinimumBalanceAccount("charlie", "9999", 2000, minimum_balance=200)
    accounts = [account1, account2, account3]
    
    atm = ATM(accounts, try_limit=3)