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
        for _ in range(1, (self.numberGenes + 1)):
            self.genes.append(chr(randint(self.minNumberChar, self.maxNumberChar)))
    
    def getPhenotype(self):
        return ''.join(self.genes)

