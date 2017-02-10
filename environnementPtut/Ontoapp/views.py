import os 
import rdflib
from django.shortcuts import render
from django.http import HttpResponse
from rdflib import *
from rdflib import Graph
from owllib.ontology import Ontology
from rdflib import URIRef

#Variables 
global repertoire1
global repertoire2
global listfile
global listfile2


###################Fonctions paramétrages#####################
	
def clearall():
#Fonction pour nettoyer la mémoire
	all = [var for var in globals() if var[0] != "_"]
	for var in all:
		del globals()[var]



#Fonctions d'affichage des templates#####################
def page(request):
	return render(request, 'page.html',{})


def Upload(request):
#Fonction principale qui appelle l'ensemble de fonction décrite précédemment
	repertoire1 = 'C:/projetPtutTuto/ProjetPtut/environnementPtut/Ontoapp/media/sources/'
	listfile = os.listdir(repertoire1)#remplissage de liste listefile avec les fichiers du dossiers média/sources
	listefileBis=[] #création nouvelle liste 
	i2=[]#création nouvelle liste 
	i1=len(listfile)#taille de la liste listefile
	
	#Etape1 : vider le fichier media 
	while i1>0 : 
		os.remove(repertoire1+listfile[i1-1])
		i1=i1-1	
	
	#Etape2: Récupération du contenu des fichiers .owl/.rdf 
		#Fichiers en local#########################################
	for count, x in enumerate (request.FILES.getlist("files")):
		def storage(f):
		#Fonction qui permet de récupérer le contenu des fichiers .owl/.rdf contenus dans les inputs et stockage dans un fichier media
			with open  (repertoire1+'file_'+ str(count), 'wb+') as destination:
				for chunk in f.chunks():
					destination.write(chunk)
			#Ajout du chemin de chaque chemin dans la liste listefile
			fichier=repertoire1+'file_'+str(count)
			listefileBis.append(fichier)
		storage(x)
		print('listefileBis:',listefileBis)
		#URL#########################################
	#for count, x in enumerate (request.POST.getlist('textLink')):
		#Ajout des url dans une liste
		#i2.append(x)
	#print(i2)
	print(len(i2))
	
	#Etape3 : Traiter l'ensemble des informations récupérées
	#Fusionner les listes
	if len(i2)==0 :
		mergedlist = listefileBis
	if len(listefileBis)==0 :
		mergedlist = i2
	else :
		mergedlist = i2 +  listefileBis
		
	
	print('mergedlist:', mergedlist)
	i1Bis=len(mergedlist)
	print('nbFichiers:', i1Bis)
	b=0
	clearall
	dictionnaire={}
	dictionnaire.clear()
	
	for b in range(0,i1Bis):	
		node='node_'+str(b)
		edge='edge_'+str(b)
		def traitement(f) : 
			#Fonction pour transformer un fichier .owl ou .rdf en noeuds.json + liens.json
			ont = Ontology()
			#Chargement de l'ontologie
			ont.load(location=mergedlist[f])
			#Transformation en JSON 
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
			#Export des fichiers json
				#with open('C:/projetPtutTuto/ProjetPtut/environnementPtut/Ontoapp/media/formatjson//liens_'+str(f)+'.json', "w") as text_file:
					#print(edges, file=text_file)
				#with open('C:/projetPtutTuto/ProjetPtut/environnementPtut/Ontoapp/media/formatjson//nodes_'+str(f)+'.json', "w") as text_file:
					#print(nodes, file=text_file)
				#Nodes,Egdes = nodes, edges
			#Renvoyer le contenu des variables
			return (nodes, edges)
		a,c =traitement(b)
		
		#remplissage d'un dictionnaire python
		dictionnaire[a]=c
		
	affichage = 0		
	if 	i1Bis==1 : 
		affichage = 8
		taille= 'size'
		
	if i1Bis ==2 : 
		affichage = 6
		taille= 'size'
	
	if i1Bis ==3: 
		affichage = 4
		taille= 'size'
	if i1Bis >=4: 
		affichage = 3
		taille= 'size'
	
		
	#Etape4: Affichage des fichiers traités sur la page 
	#dictionnaire['context']='caca'
	return  render (request,'pageDisplay.html',{'dictionnaire' : sorted(dictionnaire.items()),'context':affichage,'T':taille} )