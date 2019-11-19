# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Individual Class
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"
from random import randint
import random


class Individual(object):

    def __init__(self):
        self.minNumberChar = 32
        self.maxNumberChar = 128
        self.minRateMutation = 0.0
        self.maxRateMutation = 1.0
        self.genes = []

    def generateGenes(self, numberGenes, objetive):
        self.numberGenes = numberGenes
        self.objetive = objetive
        for _ in range(0, self.numberGenes):
            self.genes.append(
                chr(randint(self.minNumberChar, self.maxNumberChar)))

    def getPhenotype(self):
        return ''.join(self.genes).encode("utf-8")

    def getFitness(self):
        score = 0
        for i in range(0, len(self.genes)):
            if self.genes[i] == self.objetive[i]:
                score += 1
        return float(score)/float(len(self.objetive))

    def cross(self, couple):
        children = Individual()
        children.generateGenes(self.numberGenes,self.objetive)
        middlePoint = int(randint(1, len(self.genes) - 1))
        for i in range(0, len(self.genes)):
            if (i > middlePoint):
                children.genes[i] = self.genes[i]
            else:
                children.genes[i] = couple.genes[i]
        return children

    def mutate(self, rateMutation):
        for i in range(0, len(self.genes)):
            randRateMutation = float(random.uniform(
                self.minRateMutation, self.maxRateMutation))
            if (randRateMutation < rateMutation):
                if (self.genes[i] != self.objetive[i]):
                    self.genes[i] = chr(
                        randint(self.minNumberChar, self.maxNumberChar))
