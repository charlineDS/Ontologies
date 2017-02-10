# coding: utf-8
from Traduction import *

class Reporter(object):
    def __init__(self, name):
        self.name = name
        self.cnt = 0
        self.cliques = []
 
    def inc_count(self):
        self.cnt += 1
 
    def record(self, clique):
        self.cliques.append(clique)
        print(clique)
#Affiche le résultat de la recherche de clique avec les valeurs de Data_Test
    def print_report(self):
        print (self.name)
        print ('%d recursive calls' % self.cnt)
        listeClique=[]
        for i, clique in enumerate(self.cliques):
            for c in clique:
                for s in listeSommet:
                    if c == s.getId():
                        listeClique.append(s.getValue())
            print ('%d: %s' % (i, listeClique))
            listeClique = []
        print
#Export les resultats dans un fichier python
    def export_report(self):
        nbrClique = 0
        fichier = open("cliques_Result.py","w")
        fichier.write("Cliques = [")
        listeClique = []
        for i, clique in enumerate(self.cliques):
            for c in clique:
                for s in listeSommet:
                    if c == s.getId():
                        listeClique.append(s.getValue())
            nbrClique = nbrClique +1
            if nbrClique == len(self.cliques):
                fichier.write("\r{0}".format(listeClique))
            else:
                fichier.write("\r{0},".format(listeClique))
            listeClique = []
        fichier.write("\r]")
        fichier.close()