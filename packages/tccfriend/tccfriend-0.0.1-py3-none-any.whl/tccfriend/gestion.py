import sys
from PyQt5.QtWidgets import  QPushButton,  QWidget,  QGridLayout


import printgraphclass
import courstcc
import globalvariables


class Class_bouttons:
    #cette classe permet de mémoriser et de conserver une valeur de "numbutton" fixe pour chaque boutton.
    def __init__(self,nom_classe_hebergeuse,NomBoutton,numbutton):
        self.NomBoutton=NomBoutton
        self.numGraph=numbutton
        print("***********************************************")
        print("Creation  d'un boutton de la classe bouttons au rang :" + str(self.numGraph))
        print("***********************************************")
        #Création du boutton:
        self.BouttonGraphique = QPushButton(self.NomBoutton)
        self.BouttonGraphique.setStyleSheet(globalvariables.StyleHover)
        #Celui-ci est rattaché à la grille de la fenêtre gestion, au rang numgraph:
        globalvariables.gestion.grid.addWidget(self.BouttonGraphique ,self.numGraph,0,1,2)#le numero de ligne dans la grille est
                                                                                        #numGraph

        self.numGraph=self.numGraph - 4#ici on enleve le numero de ligne du boutton pour avoir les index dans la BDD
        #numGraph correspond désormais à un index dans la BDD.



        self.BouttonGraphique.clicked.connect(lambda x:printgraphclass.instance_PrintGraphClass(self.numGraph))

class BouttonNouveauGraph:
    def __init__(self,hauteur):
        self.HauteurBoutton = hauteur
        print("***********************************************")
        print("Creation du boutton pour le nouveau graph:")
        print("***********************************************")
        print("La valeur de HauteurBoutton est :"+ str(self.HauteurBoutton))
        #Boutton pour le nouveau graph:
        #PrintGraphClass est lancée avec le code 99 pour lancer un graph vide.


        self.BouttonNouveauGraph = QPushButton("Nouveau Graph")
        self.BouttonNouveauGraph.setStyleSheet(globalvariables.StyleHover)
        globalvariables.gestion.grid.addWidget(self.BouttonNouveauGraph, self.HauteurBoutton, 0, 1, 2)

        self.BouttonNouveauGraph.clicked.connect(lambda x: printgraphclass.instance_PrintGraphClass(None))
class Gestion:
    def __init__(self):
        #Fenêtre et paramètres:
        self.gestion = QWidget()
        self.gestion.setFixedWidth(500)
        self.gestion.setStyleSheet(globalvariables.WindowBackground)
        self.grid = QGridLayout()
        self.gestion.setLayout(self.grid)

        #Boutton "SignOut":
        self.BouttonSignOut = QPushButton("SignOut")
        self.BouttonSignOut.setStyleSheet(globalvariables.StyleHover)
        self.grid.addWidget(self.BouttonSignOut ,1,0,1,2)
        self.BouttonSignOut.clicked.connect(lambda x:self.SignOut())

        #Boutton "Info TCC":
        self.BouttonInfoTCC = QPushButton("Infos sur la TCC")
        self.BouttonInfoTCC.setStyleSheet(globalvariables.StyleHover)
        self.grid.addWidget(self.BouttonInfoTCC ,2,0,1,2)
        self.BouttonInfoTCC.clicked.connect(lambda x:self.Infos())


        #Boutton "Commencer":
        self.BouttonCommencer = QPushButton("Commencer")
        self.BouttonCommencer.setStyleSheet(globalvariables.StyleHover)
        self.grid.addWidget(self.BouttonCommencer, 3, 0, 1, 2)
        self.BouttonCommencer.clicked.connect(lambda x:self.Commencer())


        self.gestion.show()




    def SignOut(self):



        globalvariables.auth.current_user= None
        print("***********************************************")
        print("L'utilisateur a quitté avec succès.")
        print("***********************************************")
        self.gestion.close()
        sys.exit()




    def Commencer(self):
        #self.gestion.close()
        #del globalvariables.gestion
        #globalvariables.gestion= Gestion()
        self.HauteurBoutton = 4
        #Get sur la base de données au niveau de l'utilisateur:
        globalvariables.results = globalvariables.db.child("users").child(globalvariables.auth.current_user['localId']).get()
        if globalvariables.results.val() != None:
            print("***********************************************")
            print("Retour de FireBase dans la variable results:")
            print("***********************************************")
            print("Le type de la variable results est :" + str((type(globalvariables.results))))
            print("***********************************************")
            print("la valeur de results.val() est " + str(type(globalvariables.results.val())))
            print("Le dir de la classe est:" + str(dir(globalvariables.results)))
            # copie de cette variable results sous forme de liste dans la variable glogale globalvariables.copie_results:
            globalvariables.copie_results = globalvariables.results.val().copy()
            print("La variable globalvariables.copie_results contient : "+ str(globalvariables.copie_results))
            #Boucle for sur le retour de la Base de données:
            for result in globalvariables.results.each():
                liste_valeurs = result.val()
                print("***********************************************")
                print("Analyse du retour du graph :" + liste_valeurs[0] )
                print("***********************************************")

                print("La clé est :" + str(result.key()) + "La valeur est :" + str(result.val()))
                print("***********************************************")
                print("La valeur de self.HauteurBoutton est :" + str(self.HauteurBoutton))
                print("***********************************************")

                #Un boutton est créé pour chaque graph avec la classe Class_bouttons qui gardera en mémoire
                #des données précises.
                Class_bouttons(self, liste_valeurs[0], self.HauteurBoutton)
                self.HauteurBoutton = self.HauteurBoutton + 1
            #Le boutton pour un nouveau graph est rajouté à la fin:
            self.Boutton_nouveauG =BouttonNouveauGraph(self.HauteurBoutton)
        else:
            #sinon copie_results est une liste vide:
            globalvariables.copie_results =[]
            self.Boutton_nouveauG =BouttonNouveauGraph(self.HauteurBoutton)




    def Infos(self):
        globalvariables.instance_cours = courstcc.Cours_TCC()




