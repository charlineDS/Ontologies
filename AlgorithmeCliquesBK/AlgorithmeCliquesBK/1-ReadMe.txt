Liste des fichiers:
DataTestAlgo ==> Tableau de valeur utilisé pour tester l'algorithme
ExempleDataClasse ==> Le fichier contient la liste des classes utilisé dans l'algorithme
ExempleDataLink ==> L'ensemble des liens d'une classe au autre selon ce format :
	[] --> toujours commencer par une liste vide
	[...] --> Les classes liées à la permière classe
	[...] --> Les classes liées à la deuxième classe
	ect
BronKerbosch ==> Algorithme de Coen Bron et Joep Kerbosch
PivotBronKerbosch ==> Algorithme de Coen Bron et Joep Kerbosch, opti avec un pivot
Sommet ==> Classe composé d'une Data et un Id, Data = import et Id = image de la Data dans l'algorithme
Traducteur ==> Convertit les fichiers Data en remplacant les String des nom des classes par des Id
Reporter ==> Gère l'ensemble de l'affichage
Main ==> Appelle les fonctions

Auto_Data ==> Fichiers créés par la traduction de ExempleDataLink en Id
cliques_Result ==> Le fichier contenant les résultats