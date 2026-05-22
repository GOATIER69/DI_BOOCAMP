#Défi
import math

class Circle:
    """Classe représentant un cercle avec ses propriétés et opérations"""
    
    def __init__(self, radius: int | float = 1) -> None:
        """Initialise un cercle avec un rayon"""
        if radius <= 0:
            raise ValueError("Le rayon doit être positif!")
        self._radius = radius
    
    # ===== PROPRIÉTÉS (Getters et Setters) =====
    
    @property
    def radius(self):
        """Retourne le rayon du cercle"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Définit le rayon du cercle"""
        if value <= 0:
            raise ValueError("Le rayon doit être positif!")
        self._radius = value
    
    @property
    def diameter(self):
        """Retourne le diamètre du cercle"""
        return self._radius * 2
    
    @diameter.setter
    def diameter(self, value):
        """Définit le diamètre du cercle"""
        if value <= 0:
            raise ValueError("Le diamètre doit être positif!")
        self._radius = value / 2
    
    # ===== MÉTHODES DE CALCUL =====
    
    def area(self):
        """Calcule l'aire du cercle"""
        return math.pi * self._radius ** 2
    
    def circumference(self):
        """Calcule la circonférence du cercle"""
        return 2 * math.pi * self._radius
    
    # ===== MÉTHODES DUNDER (MAGIQUES) =====
    
    def __str__(self):
        """Représentation lisible du cercle"""
        return f"Circle(rayon={self._radius:.2f})"
    
    def __repr__(self):
        """Représentation technique du cercle"""
        return f"Circle({self._radius})"
    
    def __add__(self, other):
        """Additionne deux cercles et retourne un nouveau cercle"""
        if not isinstance(other, Circle):
            raise TypeError("Vous pouvez seulement additionner deux Circle!")
        new_radius = self._radius + other._radius
        return Circle(new_radius)
    
    def __sub__(self, other):
        """Soustrait deux cercles"""
        if not isinstance(other, Circle):
            raise TypeError("Vous pouvez seulement soustraire deux Circle!")
        new_radius = self._radius - other._radius
        if new_radius <= 0:
            raise ValueError("Le rayon résultant doit être positif!")
        return Circle(new_radius)
    
    def __mul__(self, factor):
        """Multiplie le rayon d'un cercle"""
        if not isinstance(factor, (int, float)):
            raise TypeError("Le facteur doit être un nombre!")
        if factor <= 0:
            raise ValueError("Le facteur doit être positif!")
        return Circle(self._radius * factor)
    
    def __rmul__(self, factor):
        """Multiplie le rayon d'un cercle (opération inverse)"""
        return self.__mul__(factor)
    
    def __eq__(self, other):
        """Vérifie si deux cercles sont égaux"""
        if not isinstance(other, Circle):
            return False
        return abs(self._radius - other._radius) < 1e-9
    
    def __ne__(self, other):
        """Vérifie si deux cercles sont différents"""
        return not self.__eq__(other)
    
    def __lt__(self, other):
        """Vérifie si ce cercle est plus petit"""
        if not isinstance(other, Circle):
            raise TypeError("Vous pouvez seulement comparer avec un Circle!")
        return self._radius < other._radius
    
    def __le__(self, other):
        """Vérifie si ce cercle est plus petit ou égal"""
        if not isinstance(other, Circle):
            raise TypeError("Vous pouvez seulement comparer avec un Circle!")
        return self._radius <= other._radius
    
    def __gt__(self, other):
        """Vérifie si ce cercle est plus grand"""
        if not isinstance(other, Circle):
            raise TypeError("Vous pouvez seulement comparer avec un Circle!")
        return self._radius > other._radius
    
    def __ge__(self, other):
        """Vérifie si ce cercle est plus grand ou égal"""
        if not isinstance(other, Circle):
            raise TypeError("Vous pouvez seulement comparer avec un Circle!")
        return self._radius >= other._radius
    
    def __hash__(self):
        """Permet d'utiliser Circle dans des sets et dictionnaires"""
        return hash(round(self._radius, 9))


# ===== TESTS =====

if __name__ == "__main__":
    print("="*50)
    print("CLASSE CIRCLE - TESTS")
    print("="*50)
    
    # Test 1 : Création de cercles
    print("\n✅ Test 1: Création de cercles")
    c1 = Circle(5)
    c2 = Circle(3)
    c3 = Circle(7)
    print(f"c1: {c1}")
    print(f"c2: {c2}")
    print(f"c3: {c3}")
    
    # Test 2 : Propriétés
    print("\n✅ Test 2: Propriétés")
    print(f"Rayon de c1: {c1.radius}")
    print(f"Diamètre de c1: {c1.diameter}")
    c1.diameter = 20  # Définir via le diamètre
    print(f"Rayon après changement de diamètre: {c1.radius}")
    
    # Test 3 : Calculs
    print("\n✅ Test 3: Calculs")
    print(f"Aire de c1: {c1.area():.2f}")
    print(f"Circonférence de c1: {c1.circumference():.2f}")
    
    # Test 4 : Addition
    print("\n✅ Test 4: Addition de cercles")
    c4 = c2 + c3
    print(f"{c2} + {c3} = {c4}")
    print(f"Rayon du résultat: {c4.radius}")
    
    # Test 5 : Multiplication
    print("\n✅ Test 5: Multiplication de cercles")
    c5 = c2 * 2
    print(f"{c2} * 2 = {c5}")
    
    # Test 6 : Comparaisons
    print("\n✅ Test 6: Comparaisons")
    print(f"{c2} < {c3}: {c2 < c3}")
    print(f"{c2} > {c3}: {c2 > c3}")
    print(f"{c2} == {c2}: {c2 == c2}")
    c6 = Circle(3)
    print(f"{c2} == {c6}: {c2 == c6}")
    
    # Test 7 : Tri de cercles
    print("\n✅ Test 7: Tri de cercles")
    circles = [Circle(7), Circle(2), Circle(5), Circle(1), Circle(9)]
    print(f"Avant tri: {[str(c) for c in circles]}")
    circles_sorted = sorted(circles)
    print(f"Après tri: {[str(c) for c in circles_sorted]}")
    
    # Test 8 : __repr__
    print("\n✅ Test 8: __repr__")
    print(f"repr(c1): {repr(c1)}")
    print(f"str(c1): {str(c1)}")
    
    print("\n" + "="*50)
    print("TOUS LES TESTS RÉUSSIS! ✅")
    print("="*50)