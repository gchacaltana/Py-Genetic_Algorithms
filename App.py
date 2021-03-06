# !/usr/bin/env python
# -*- coding: utf-8 -*-
# App Script
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"

import sys
from random import randint
from Individual import Individual


class App(object):

    def __init__(self):
        self.maxLengthObjetive = 300
        self.minLengthObjetive = 1
        self.maxPopulation = 300
        self.minPopulation = 100
        self.minRateMutation = 0.0
        self.maxRateMutation = 1.0
        self.populations = []
        self.inputParams()
        self.executeGeneticAlgorithm()

    def inputParams(self):
        self.inputObjetive()
        self.inputPopulation()
        self.inputRateMutation()

    def inputObjetive(self):
        self.objetive = input("Ingrese el texto objetivo: ")
        if (len(self.objetive) == 0):
            raise Exception("Exception: El objetivo no fue ingresado!")
        if (len(self.objetive) < self.minLengthObjetive):
            raise Exception("Exception: El objetivo es muy corto!")
        if (len(self.objetive) > self.maxLengthObjetive):
            raise Exception("Exception: El objetivo es muy extenso!")

    def inputPopulation(self):
        self.numberPopulation = int(
            input("Ingrese cantidad de individuos por poblacion [100 a 300]: "))
        if (self.numberPopulation == 0):
            raise Exception(
                "Exception: La poblacion de individuos es invalida!")
        if (self.numberPopulation < self.minPopulation):
            raise Exception(
                "Exception: La poblacion de individuos es muy reducida!")
        if (self.numberPopulation > self.maxPopulation):
            raise Exception(
                "Exception: La poblacion de individuos es muy extensa!")

    def inputRateMutation(self):
        self.rateMutation = float(
            input("Ingrese la tasa de mutacion [0 a 1]: "))
        if (self.rateMutation < self.minRateMutation):
            raise Exception(
                "Exception: La tasa de mutacion no puede ser menor de %s" % self.minRateMutation)
        if (self.rateMutation > self.maxRateMutation):
            raise Exception(
                "Exception: La tasa de mutacion no puede ser mayor de %s" % self.maxRateMutation)

    def executeGeneticAlgorithm(self):
        for _ in range(0, self.numberPopulation):
            individual = Individual()
            individual.generateGenes(len(self.objetive), self.objetive)
            self.populations.append(individual)
        self.generation = 0
        print("Buscando mejor individuo....")
        while True:
            self.evaluateMembersGeneration()
            self.selectMembersGeneration()
            self.reproductionMembersGeneration()

    def evaluateMembersGeneration(self):
        self.generation += 1
        print("\n*************** GENERACION %s\n" % self.generation)
        for _ in range(0, self.numberPopulation):
            print("Generacion[%s] | Individuo[%s]: %s | fitness: %s" % (
                self.generation, _, self.populations[_].getPhenotype(), self.populations[_].getFitness()))
            if (self.evaluateObjetive(self.populations[_])):
                sys.exit()

    def selectMembersGeneration(self):
        self.parents = []
        for _ in range(0, self.numberPopulation):
            n = int(self.populations[_].getFitness()*100)
            #for j in range(0, n):
            if n>0:
                self.parents.append(self.populations[_])

    def reproductionMembersGeneration(self):
        totalParents = len(self.parents)
        print("Padres seleccionados: ", totalParents)
        for i in range(0, self.numberPopulation):
            a = int(randint(0, (totalParents-1)))
            b = int(randint(0, (totalParents-1)))
            father = self.parents[a]
            mother = self.parents[b]
            children = father.cross(mother)
            children.mutate(self.rateMutation)
            self.populations[i] = children

    def evaluateObjetive(self, individual):
        if (individual.getFitness() == 1.0):
            print("Objetivo encontrado: %s" % individual.getPhenotype())
            return True
        return False

    def showIndividualPhenotype(self):
        for j in range(0, self.numberPopulation):
            print("Individuo %s : %s" %
                  (j, self.populations[j].getPhenotype()))


if __name__ == "__main__":
    try:
        app = App()
    except (ValueError, FileNotFoundError, AttributeError, Exception) as ex:
        print(ex)
