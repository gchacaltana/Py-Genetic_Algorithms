"""
Implementación de clase Individuo
"""

__author__ = "Gonzalo Chacaltana Buleje"
from random import randint
import random


class Individual(object):
    """
    Clase que implementa al individuo de una generación
    """

    def __init__(self):
        self.min_number_char: int = 32
        self.max_number_char: int = 128
        self.min_rate_mutation: float = 0.0
        self.max_rate_mutation: float = 1.0
        self.objetive: str = ""
        self.number_genes: int = 0
        self.genes = []

    def generate_genes(self, number_genes, objetive):
        """
        Método para generar los genes
        """
        self.number_genes = number_genes
        self.objetive = objetive
        for _ in range(0, self.number_genes):
            self.genes.append(
                chr(randint(self.min_number_char, self.max_number_char)))

    def get_phenotype(self):
        """
        Método que devuelve fenotipo de individuo
        """
        return ''.join(self.genes).encode("utf-8")

    def get_fitness(self):
        """
        Método para obtener valor de fitness
        """
        score: int = 0
        for i in range(0, len(self.genes)):
            if self.genes[i] == self.objetive[i]:
                score += 1
        return float(score)/float(len(self.objetive))

    def cross(self, couple):
        """
        Método que implementa el cruce del individuo
        """
        children = Individual()
        children.generate_genes(self.number_genes, self.objetive)
        middlePoint = int(randint(1, len(self.genes) - 1))
        for i in range(0, len(self.genes)):
            if i > middlePoint:
                children.genes[i] = self.genes[i]
            else:
                children.genes[i] = couple.genes[i]
        return children

    def mutate(self, rate_mutation):
        """
        Método que implementa la mutación
        """
        for i in range(0, len(self.genes)):
            randRateMutation = float(random.uniform(
                self.min_rate_mutation, self.max_rate_mutation))
            if (randRateMutation < rate_mutation):
                if (self.genes[i] != self.objetive[i]):
                    self.genes[i] = chr(
                        randint(self.min_number_char, self.max_number_char))
