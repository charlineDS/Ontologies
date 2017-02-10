import rdflib
from rdflib import *
from rdflib import Graph
from owllib.ontology import Ontology
from rdflib import URIRef
import os

# Une méthode pour vider la mémoire car en python il y a toujours des soucis avec la mem , si elle vous pose problème vous l'enlevez tout simplement 
def clearall():
    all = [var for var in globals() if var[0] != "_"]
    for var in all:
        del globals()[var]
repertoire = 'C:/projetPtutTuto/ProjetPtut/environnementPtut/Ontoapp/media/'
file=os.listdir(repertoire)
ont = Ontology()
for i in range(0,len(file)):
ont.load(location=repertoire+file[i])
#ont.load(location=r'G:\PtutOnto\aeo.owl')
# ont.load(location=r'G:\PtutOnto\cmt.owl')
edgestemp ='[ ' 

nodestemp='['
for cls in ont.classes:
    if cls.is_named():
        nodestemp+=str('{"id" : "'+ str(cls.uri)+'",')
        laaaables = ont.get_labels(cls.uri)
        for labelo in laaaables:
            nodestemp+=str('"label" : "'+ labelo+'"' )
			#rajouter une alternative si y'a pas de labels ? (exemple de cmt)
        for s,p,o in cls.triples:
            if(o==cls.uri and s.split('/')[0]=="http:"):
                edgestemp+=str('{"from" : "'+str(o)+'", "to" : "'+str(s)+'"},')
        nodestemp+=str("},")
nodes=nodestemp[:-1]
nodes+=str("]")

edges=edgestemp[:-1]
edges+=str("]")
with open("liens.json", "w") as text_file:
    print(edges, file=text_file)
with open("noeuds.json", "w") as text_file:
    print(edges, file=text_file)

clearall