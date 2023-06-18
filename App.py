"""
Aplicación que implementa un algoritmo de optimización utilizando algoritmos genéticos.
"""
__author__ = "Gonzalo Chacaltana Buleje"

import sys
from random import randint
from individual import Individual


class App(object):
    """
    Clase que implementa la aplicación de consola
    """

    def __init__(self):
        self.max_length_objetive: int = 300
        self.min_length_objetive: int = 1
        self.max_population: int = 300
        self.min_population: int = 100
        self.min_rate_mutation: float = 0.0
        self.max_rate_mutation: float = 1.0
        self.number_population: int = 0
        self.objetive: str = ""
        self.populations = []
        self.parents = []

    def run(self):
        """
        Método principal de la aplicación
        """
        self.input_params()
        self.execute_genetic_algorithm()

    def input_params(self):
        """
        Método para el ingreso de parámetros
        """
        self.input_objetive()
        self.input_population()
        self.input_rate_mutation()

    def input_objetive(self):
        """
        Método para el ingreso del texto objetivo
        """
        self.objetive = input("Ingrese el texto objetivo: ")
        if len(self.objetive) == 0:
            raise Exception("Exception: El objetivo no fue ingresado!")
        if len(self.objetive) < self.min_length_objetive:
            raise Exception("Exception: El objetivo es muy corto!")
        if len(self.objetive) > self.max_length_objetive:
            raise Exception("Exception: El objetivo es muy extenso!")

    def input_population(self):
        """
        Método para el ingreso de datos de la población
        """
        self.number_population = int(
            input("Ingrese cantidad de individuos por poblacion [100 a 300]: "))
        if (self.number_population == 0):
            raise Exception(
                "Exception: La poblacion de individuos es invalida!")
        if (self.number_population < self.min_population):
            raise Exception(
                "Exception: La poblacion de individuos es muy reducida!")
        if (self.number_population > self.max_population):
            raise Exception(
                "Exception: La poblacion de individuos es muy extensa!")

    def input_rate_mutation(self):
        """
        Método para el ingreso del ratio de mutación.
        """
        self.rate_mutation = float(
            input("Ingrese la tasa de mutacion [0 a 1]: "))
        if (self.rate_mutation < self.min_rate_mutation):
            raise Exception(
                "Exception: La tasa de mutacion no puede ser menor de %s" % self.min_rate_mutation)
        if (self.rate_mutation > self.max_rate_mutation):
            raise Exception(
                "Exception: La tasa de mutacion no puede ser mayor de %s" % self.max_rate_mutation)

    def execute_genetic_algorithm(self):
        """
        Método para ejecutar el algoritmo genético
        """
        for _ in range(0, self.number_population):
            individual = Individual()
            individual.generate_genes(len(self.objetive), self.objetive)
            self.populations.append(individual)
        self.generation = 0
        print("Buscando mejor individuo....")
        while True:
            self.evaluate_members_generation()
            self.select_members_generation()
            self.reproduction_members_generation()

    def evaluate_members_generation(self):
        """
        Método para evaluar miembros de una generación
        """
        self.generation += 1
        print(f"\n GENERACION {self.generation}\n")
        for x in range(0, self.number_population):
            print(
                f"Generacion[{self.generation}] | Individuo[{x}]: {self.populations[x].get_phenotype()} | fitness: {self.populations[x].get_fitness()}")
            if self.evaluate_objetive(self.populations[x]):
                sys.exit()

    def select_members_generation(self):
        """
        Método para seleccionar a los miembros de una generación
        """
        self.parents = []
        for _ in range(0, self.number_population):
            n = int(self.populations[_].get_fitness()*100)
            if n > 0:
                self.parents.append(self.populations[_])

    def reproduction_members_generation(self):
        """
        Método que implementa la reproducción de miembros de una generación
        """
        total_parents: int = len(self.parents)
        print("Padres seleccionados: ", total_parents)
        for i in range(0, self.number_population):
            a = int(randint(0, (total_parents-1)))
            b = int(randint(0, (total_parents-1)))
            father = self.parents[a]
            mother = self.parents[b]
            children = father.cross(mother)
            children.mutate(self.rate_mutation)
            self.populations[i] = children

    def evaluate_objetive(self, individual: Individual):
        """
        Método para evaluar objetivo
        """
        if individual.get_fitness() == 1.0:
            print(f"Objetivo encontrado: {individual.get_phenotype()}")
            return True
        return False

    def show_individual_phenotype(self):
        """
        Método para mnostrar fenotipo individual
        """
        for j in range(0, self.number_population):
            print(f"Individuo {j} : {self.populations[j].get_phenotype()}")


if __name__ == "__main__":
    try:
        app = App()
        app.run()
    except (ValueError, FileNotFoundError, AttributeError, Exception) as ex:
        print(ex)
