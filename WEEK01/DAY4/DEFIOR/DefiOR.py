import random

class Gene:
    def __init__(self, value=None):
        self.value = value if value is not None else random.randint(0, 1)
    
    def mutate(self):
        self.value = 1 - self.value 
    
    def __str__(self):
        return str(self.value)


class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]
    
    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:
                gene.mutate()
    
    def __str__(self):
        return "".join(str(gene) for gene in self.genes)

class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]
    
    def mutate(self):
        for chromosome in self.chromosomes:
            if random.random() < 0.5:
                chromosome.mutate()
    
    def is_perfect(self):
        for chromosome in self.chromosomes:
            for gene in chromosome.genes:
                if gene.value != 1:
                    return False
        return True
    
    def __str__(self):
        return "\n".join(str(chromosome) for chromosome in self.chromosomes)

class Organism:
    def __init__(self, dna, mutation_probability=0.5):
        self.dna = dna
        self.mutation_probability = mutation_probability
        self.generation = 0
    
    def evolve(self):
        """Permet à l'organisme de muter jusqu'à l'ADN parfait"""
        while not self.dna.is_perfect():
            if random.random() < self.mutation_probability:
                self.dna.mutate()
            self.generation += 1
        return self.generation
    
    def __str__(self):
        return f"Organisme - Génération {self.generation}\nADN:\n{self.dna}"

print("=" * 50)
print("EXPÉRIENCE D'ÉVOLUTION BIOLOGIQUE")
print("=" * 50)

generations_list = []

for organism_num in range(5):
    dna = DNA()
    organism = Organism(dna, mutation_probability=0.5)
    
    generations_needed = organism.evolve()
    generations_list += [generations_needed]
    
    print(f"\nOrganisme {organism_num + 1}:")
    print(f"Générations nécessaires: {generations_needed}")
    print(f"ADN Final:\n{organism.dna}\n")

print("=" * 50)
print("RÉSULTATS")
print("=" * 50)
print(f"Générations moyennes: {sum(generations_list) / len(generations_list):.2f}")
print(f"Minimum: {min(generations_list)}")
print(f"Maximum: {max(generations_list)}")
print("=" * 50)