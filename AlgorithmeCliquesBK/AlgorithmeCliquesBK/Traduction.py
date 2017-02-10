from ExempleDataClasse import *
from ExempleDataLink import *
from Sommet import *

# liste = []
# find = False
#Cree une liste avec toutes les valeurs de Data_Test
# for s in Data_Test:
    # for p in s:
        # for u in liste:
            # if u == p:
                # find=True
        # if(find==False):
            # liste.append(p)
        # find = False
#Cree un tableau de sommet avec un id puis la valeur de Data_Test
i = 1
listeSommet = []
for l in Data_Classe:
    listeSommet.append(sommet(i,l))
    i=i+1
# Ecrit Data_Test mais avec les ID
NEIGHBORS = []
emptyListe = []
NEIGHBORS.append(emptyListe)
for s in Data_Link:
    listeId = []
    for p in s:
        for ls in listeSommet:
            if p == ls.getValue():
                listeId.append(ls.getId())
    NEIGHBORS.append(listeId)
#Pour l algorithme, il ne faut pas que la premiere valeur, ici 1, soit dans le premier tuple.
# listePosition = []
# for n in NEIGHBORS:
    # for id in n:
        # if id == 1:
           # listePosition.append(n)
           # NEIGHBORS.remove(n)
# for p in listePosition:
    # NEIGHBORS.append(p)
#creation du fichier de contenant les data de notre exemple
i=0
result="NEIGHBORS = ["
for n in NEIGHBORS:
    if i == len(NEIGHBORS)-1:
        result= "{0}\r    {1}".format(result,n)
    else:
        result= "{0}\r    {1},".format(result,n)
        i=i+1
result="{0}\r]\n\rNODES = set(range(1, len(NEIGHBORS)))\n\rMIN_SIZE=3".format(result)
#result = "NEIGHBORS = {0} \n\rNODES = set(range(1, len(NEIGHBORS))) \n\rMIN_SIZE=3".format(NEIGHBORS)
fichier = open("auto_Data.py", "w")
fichier.write(result)
fichier.close()