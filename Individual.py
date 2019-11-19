# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Individual Class
"""
__author__ = "Gonzalo Chacaltana Buleje"
__email__ = "gchacaltanab@gmail.com"
from random import randint

class Individual(object):

    def __init__(self, numberGenes, objetive):
        self.numberGenes = numberGenes
        self.objetive = objetive
        self.minNumberChar = 32
        self.maxNumberChar = 128
        self.genes = []
        for _ in range(0, self.numberGenes):
            n = randint(self.minNumberChar, self.maxNumberChar)
            self.genes.append(chr(n))
    
    def getPhenotype(self):
        return ''.join(self.genes).encode("utf-8")

    def getFitness(self):
        score = 0
        for i in range(0, len(self.genes)):
            if self.genes[i]==self.objetive[i]:
                score+=1
        return float(score)/float(len(self.objetive))
    