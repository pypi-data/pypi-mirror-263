
import sys
from PyQt5.QtWidgets import  QLabel, QPushButton, QVBoxLayout, QWidget,  QGridLayout,QLineEdit ,QScrollArea

import IATCC
import matplotlib
from itertools import cycle
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
#Copyright (c) 2002-2011 John D. Hunter; All Rights Reserved
import globalvariables
import time
from PyQt5.QtCore import *

def instance_PrintGraphClass(key):
    if globalvariables.InstancePrintGraphClass != []:
        globalvariables.InstancePrintGraphClass.fen_graph.close()
        del globalvariables.InstancePrintGraphClass
    globalvariables.InstancePrintGraphClass =PrintGraphClass(key)


class PrintGraphClass:
    def __init__(self, key):
        if key != None:
            self.key = key
        print("***********************************************")
        print("On a appuyé sur un boutton ..")
        print("PrintgraphClass est lancée, l'argument est " + str(key))
        print("***********************************************")

        # la variable key 99 est la clé renvoyée pour un nouveau graph. Si la liste des graphs est vide le numero du graph dans la BDD sera 0:
        if key == None and globalvariables.results.val() is None:
            self.numero_graph = 0
            self.FenetreNouveauGraph()
        # sinon si la BDD contient déjà des valeurs le numero du graph dans la BDD sera len(results.val()), (le (nouveau)  dernier element de la BDD):
        elif key == None:
            self.numero_graph = len(globalvariables.results.val())
            self.FenetreNouveauGraph()
        # sinon on récupère la liste de points correspondant au graph demandé:
        else:

            self.numero_graph = key
            #La variable liste_points contient tous les points du graph
            self.liste_points =globalvariables.copie_results[self.numero_graph]
            print("La liste des points du nouveau graph est bien:")
            print(self.liste_points )
            self.PrintGraph()  # lancement de PrintGraph
    def FenetreNouveauGraph(self):
        #Qwidget ,Layout en grille et nom de la fenêtre:
        self.fen_graph = QWidget()
        self.fen_graph.setStyleSheet(globalvariables.WindowBackground)
        self.grid = QGridLayout()
        self.fen_graph.setLayout(self.grid)
        self.fen_graph.setWindowTitle("Nouveau Graph")

        #Qlabel du titre du nouveau graph:
        self.label_titre_nouveau_graph = QLabel("Nom du Nouveau Graph:")
        self.label_titre_nouveau_graph.setStyleSheet(globalvariables.StyleText)
        self.grid.addWidget(self.label_titre_nouveau_graph,1,0,1,2)

        #QLineEdit du nom ud nouveau graph
        self.titre_nouveau_g_ins = QLineEdit()
        self.titre_nouveau_g_ins.setStyleSheet(globalvariables.StyleHover)
        self.titre_nouveau_g_ins.resize(150, 40)
        self.grid.addWidget(self.titre_nouveau_g_ins ,2,0,1,2)

        #Boutton de lancement du nouveau graph:
        self.Boutton_nouveau_titre =  QPushButton("Envoi")
        self.Boutton_nouveau_titre.setStyleSheet(globalvariables.StyleHover)
        self.grid.addWidget(self.Boutton_nouveau_titre,3,0,1,2)
        self.Boutton_nouveau_titre.clicked.connect(lambda x:self.GestionNouveauTitre())
        self.fen_graph.show()

    def GestionNouveauTitre(self):
        #Creation d'un nouveau graph: liste_points est une liste vide
        self.liste_points=[]
        #On lui ajoute le titre:
        self.liste_points.append(self.titre_nouveau_g_ins.text())
        self.PrintGraph()

    def PrintGraph(self):
        #Fenêtre Layout et style:
        self.fen_graph=  QWidget()
        self.fen_graph.resize(900,800)
        self.fen_graph.setWindowTitle(self.liste_points[0])
        self.grid = QGridLayout()
        self.fen_graph.setLayout(self.grid)
        self.fen_graph.setStyleSheet(globalvariables.WindowBackground)

        #Qlabel du titre : self.liste_point[0] contient le titre du graph
        self.label3 = QLabel(self.liste_points[0])
        self.label3.setStyleSheet(globalvariables.StyleTitre)
        self.grid.addWidget(self.label3,0,0,1,1)

        #QLabel du graphique:
        self.titre = QLabel("Cliquez Graph Switch pour commencer")
        self.titre.setStyleSheet(globalvariables.StyleText)
        self.grid.addWidget(self.titre, 2, 0, 1, 1)

        #Boutton du Nouveau point du graph:
        self.BouttonNouveauPoint = QPushButton("Nouveau Point")
        self.BouttonNouveauPoint.setStyleSheet(globalvariables.StyleHover)
        self.grid.addWidget(self.BouttonNouveauPoint, 2, 1, 1, 1)
        self.BouttonNouveauPoint.clicked.connect(lambda x:CreationListeInsertion({} ,0,self.numero_graph))

        #Boutton de "switch" du graph
        self.BouttonGraph2 = QPushButton("Graph Switch")
        self.BouttonGraph2.setStyleSheet(globalvariables.StyleHover)
        self.grid.addWidget(self.BouttonGraph2 ,3,0,1,1)
        # creation d'une liste circulaire:
        self.liste_des_clicks = [0,1,2]
        self.cicle= cycle(self.liste_des_clicks)
        #La fonction va lancer la fonction de dessin du graph avec une variable circulaire next(self.cicle))
        #qui pourra prendre comme argument 0 , 1 ou 2 :
        self.BouttonGraph2.clicked.connect(lambda x:self.plot(next(self.cicle)))

        #Preparation du graphique:
        self.fig, self.ax = plt.subplots()

        #Cadre pour le graphique:
        self.canvas = FigureCanvas(self.fig)
        self.grid.addWidget(self.canvas,1,0,1,1)



        #Variables qui vont recevoir les chaines d'émotions négatives et émotions résultats:
        self.les_x=0
        #Axe des x du graphique:
        self.xaxis=[]
        #Emotions négatives
        self.yaxis=[]
        #Emotions résultats:
        self.emotions_resultats = []
        #Création d'un scroll pour recevoir la liste des bouttons construits a partir de chaque exposition:
        self.scroll = QScrollArea()
        #Widget receptacle
        self.widget = QWidget()
        self.widget.resize(900,900)
        #Layout à l'interieur du widget:
        self.vbox = QVBoxLayout()
        #Paramètres du scroll:
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.grid.addWidget(self.scroll, 1, 1, 1, 1)
        self.widget.setLayout(self.vbox)


        if self.liste_points[1:]: # on enlève le titre (index 0), donc si liste_points contient des points:
            for points in self.liste_points[1:]:
                BouttonDePoint(self,self.les_x,points)

                self.xaxis.append(self.les_x)
                print("------------------------------------------------------------------------")
                print("On rajoute le point emotion négative :"+ str(points['emotion']) )
                #Ajout de l'element emotions négative à la liste correspondante:
                self.yaxis.append(int(points['emotion']))
                print("On rajoute le point emotion résultat :" + str(points['emotion_resultat']))
                #Ajout de l'element emotions résultat à la liste correspondante:
                self.emotions_resultats.append(int(points['emotion_resultat']))
                print(self.yaxis,self.xaxis)
                self.les_x += 1
        #Si la liste est vide, plot avec l'argument 0:
        else:
            self.plot(0)

        #lancement du module d'IA:
        self.IATCC()

        self.fen_graph.show()



    def IATCC(self):

        if len(self.xaxis) < 3 :
            #Qlabel d'IA:
            self.LabelIA = QLabel("Pas assez de données de graph pour lancer une IA")
            self.LabelIA.setStyleSheet(globalvariables.StyleText)
            self.grid.addWidget(self.LabelIA, 4, 0, 1, 2)
        else :
            #try:
            #lancement du module d'IA
            self.IA = IATCC.IATCC( self.yaxis,self.emotions_resultats)
            self.IA.lancement()
            self.TextIA =""
            #La variable globalvariables.phrases contient les phrases à afficher après analyse.
            for i in globalvariables.phrases:
                self.TextIA += i + "\n"
            #Qlabel d'IA:
            self.LabelIA = QLabel(self.TextIA)
            self.LabelIA.setStyleSheet(globalvariables.StyleScrollGraph)
            self.grid.addWidget(self.LabelIA, 4, 0, 1, 2)







    def plot(self,param): # dessin du graph en fonction du paramètre circulaire de valeur 0 ,1 ou 2:
        print("***********************************************")
        print("Plot du graph ..")
        print("xaxis vaut:"+str(self.xaxis))
        print("yaxis vaut:" +str(self.yaxis))
        print("***********************************************")
        if param ==0:
            #Qlabel du titre:
            self.titre = QLabel(" Graph émotions resultats")
            self.titre.setStyleSheet(globalvariables.StyleText)
            self.grid.addWidget(self.titre, 2,0, 1, 1)
            #Netoyage du graph:
            self.ax.clear()
            #Dessin du graph:
            self.ax.plot(self.xaxis, self.emotions_resultats)

        if param ==1:
            #Qlabel du titre:
            self.titre = QLabel(" Graph émotions négative")
            self.titre.setStyleSheet(globalvariables.StyleText)
            self.grid.addWidget(self.titre, 2,0, 1, 1)
            #Netoyage du graph:
            self.ax.clear()
            #Dessin du graph:
            self.ax.plot(self.xaxis, self.yaxis)

        if param == 2:
            #Qlabel du titre:
            self.titre = QLabel(" Graph émotions négative et émotions résultats")
            self.titre.setStyleSheet(globalvariables.StyleText)
            self.grid.addWidget(self.titre, 2,0, 1, 1)
            #Netoyage du graph:
            self.ax.clear()
            #Dessin du graph (les deux courbes):
            self.ax.plot(self.xaxis, self.emotions_resultats)
            self.ax.plot(self.xaxis, self.yaxis)

        self.canvas.draw()



class BouttonDePoint:
    def __init__(self,InstancePrintGraphClass,NumeroBoutton,points):
        self.NumeroPoint= NumeroBoutton +1
        self.point=points
        self.InstancePrintGraphClass = InstancePrintGraphClass
        self.numeroGraph = self.InstancePrintGraphClass.numero_graph

        #Fabrication du boutton
        self.BouttonListePoints= QPushButton(
        "Situation " + str(self.NumeroPoint) + " :" +
        str(self.point["situation"]) + "\n" +
        "Emotion :" + str(self.point["emotion"]) + "\n" +
        "Pensées automatiques :" + str(self.point["pensées_auto"]) + "\n" +
        "Confirmation des pensées automatiques :" + str(self.point["confirmation"]) + "\n"
        + "Preuves contraires :" +
        str(self.point["preuves_contraires"]) + "\n" +
        "Pensées adaptées :" + str(self.point["pensée_adaptée"]) + "\n" +
        "Emotion resultat :" + str(self.point["emotion_resultat"]) + "\n")
        self.BouttonListePoints.setStyleSheet(globalvariables.StyleScrollGraphHover)

        #Insertion du point dans la vbox de l'objet InstancePrintGraphClass:
        self.InstancePrintGraphClass.vbox.addWidget(self.BouttonListePoints)
        #Le point lancera la fonction ListeInsertion avec en paramètre le dictionnaire du point et le numero de sa place
        #Dans le graph:
        self.BouttonListePoints.clicked.connect(lambda x:CreationListeInsertion(self.point,self.NumeroPoint,self.numeroGraph))


class ListeInsertion:
    def __init__(self, point ,NumeroPoint, numeroGraph):
        #self.point contient le dictionnaire du point:
        self.point=point
        #self.NumeroPoint contient l'index du point dans la liste du graph:
        self.NumeroPoint = NumeroPoint
        self.numeroGraph = numeroGraph
        #Paramètres de fenêtre:
        self.fen_insertion=  QWidget()
        self.fen_insertion.setStyleSheet(globalvariables.WindowBackground)
        self.fen_insertion.resize(900,800)
        #Si le point vaut 0 alors il s'agit de l'ajout d'un nouveau point:
        if self.NumeroPoint == 0:
            #Titre de fenêtre et Qlabel de titre correspondants:
            self.fen_insertion.setWindowTitle("Nouveau Point pour: " +globalvariables.InstancePrintGraphClass.liste_points[0])
            self.label_titre_point = QLabel("Nouveau Point pour: " + globalvariables.InstancePrintGraphClass.liste_points[0])

        else : #Sinon il s'agit de la réécriture d'un point précis dans la liste:
            #Titre de fenêtre et Qlabel de titre correspondants:
            self.fen_insertion.setWindowTitle("Correction du point " + str(self.NumeroPoint)+" pour " + globalvariables.InstancePrintGraphClass.liste_points[0])
            self.label_titre_point = QLabel("Correction du point " + str(self.NumeroPoint)+" pour " + globalvariables.InstancePrintGraphClass.liste_points[0])
        #Style des deux Qlabels du dessus.
        self.label_titre_point.setStyleSheet(globalvariables.StyleTitre)
        self.grid_insertion = QGridLayout()
        self.grid_insertion.addWidget(self.label_titre_point, 4, 0, 1, 1)

        self.grid_insertion1 = QGridLayout()
        #scroll de la fenêtre:
        self.scroll2 = QScrollArea()
        #Qwidget qui va être encadré par le scroll
        self.widget_insertion = QWidget()
        self.widget_insertion.resize(900, 900)

        #Layout de vbox:
        self.vboxlayout =  QVBoxLayout()
        #Layout de grille contenu dans le layout de vbox:
        self.vboxlayout.addLayout(self.grid_insertion)

        #Paramètres du scroll:
        self.scroll2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll2.setWidgetResizable(True)
        #Ajout du scroll2 au widget_insertion
        self.scroll2.setWidget(self.widget_insertion)
        #Linkage du scroll à grid_insertion1
        self.grid_insertion1.addWidget(self.scroll2, 1, 1, 1, 1)
        #insertion de widget_insertion dans le layout de vboxlayout
        self.widget_insertion.setLayout(self.vboxlayout)
        #insertion de la fenêtre globale dans le layout de la grille grid_insertion1
        self.fen_insertion.setLayout(self.grid_insertion1)


        #Ensemble des Qlabels et des QlineEdit pour ajouter le point:
        self.situation = QLabel("Situation:")
        self.situation.setStyleSheet(globalvariables.StyleScrollGraph)
        self.grid_insertion.addWidget(self.situation,5,0,1,1)

        self.situation_ins = QLineEdit()
        self.situation_ins.setStyleSheet(globalvariables.StyleScrollGraphHover)
        self.situation_ins.resize(150, 40)
        self.grid_insertion.addWidget(self.situation_ins ,6,0,1,1)

        self.emo_label = QLabel("Emotion (chiffre entre 0 et 10):")
        self.emo_label.setStyleSheet(globalvariables.StyleScrollGraph)
        self.grid_insertion.addWidget(self.emo_label,7,0,1,1)

        self.emo_ins = QLineEdit()
        self.emo_ins.setStyleSheet(globalvariables.StyleScrollGraphHover)
        self.emo_ins.resize(150, 40)
        self.grid_insertion.addWidget(self.emo_ins ,8,0,1,1)

        self.pensee_auto = QLabel("Pensées automatiques:")
        self.pensee_auto.setStyleSheet(globalvariables.StyleScrollGraph)
        self.grid_insertion.addWidget(self.pensee_auto,9,0,1,1)

        self.pensee_auto_ins = QLineEdit()
        self.pensee_auto_ins.setStyleSheet(globalvariables.StyleScrollGraphHover)
        self.pensee_auto_ins.resize(150, 40)
        self.grid_insertion.addWidget(self.pensee_auto_ins ,10,0,1,1)

        self.conf_label = QLabel("Confirmation:")
        self.conf_label.setStyleSheet(globalvariables.StyleScrollGraph)
        self.grid_insertion.addWidget(self.conf_label,11,0,1,1)

        self.conf_label_ins = QLineEdit()
        self.conf_label_ins.setStyleSheet(globalvariables.StyleScrollGraphHover)
        self.conf_label_ins.resize(150, 40)
        self.grid_insertion.addWidget(self.conf_label_ins ,12,0,1,1)

        self.preuves_contr = QLabel("Preuves contraires:")
        self.preuves_contr.setStyleSheet(globalvariables.StyleScrollGraph)
        self.grid_insertion.addWidget(self.preuves_contr,13,0,1,1)

        self.preuves_contr_ins = QLineEdit()
        self.preuves_contr_ins.setStyleSheet(globalvariables.StyleScrollGraphHover)
        self.preuves_contr_ins.resize(150, 40)
        self.grid_insertion.addWidget(self.preuves_contr_ins ,14,0,1,1)

        self.pensee_adap = QLabel("Pensées adaptées:")
        self.pensee_adap.setStyleSheet(globalvariables.StyleScrollGraph)
        self.grid_insertion.addWidget(self.pensee_adap,15,0,1,1)

        self.pensee_adap_ins = QLineEdit()
        self.pensee_adap_ins.setStyleSheet(globalvariables.StyleScrollGraphHover)
        self.pensee_adap_ins.resize(150, 40)
        self.grid_insertion.addWidget(self.pensee_adap_ins ,16,0,1,1)

        self.emo_result = QLabel("Emotions résultats (chiffre entre 0 et 10):")
        self.emo_result.setStyleSheet(globalvariables.StyleScrollGraph)
        self.grid_insertion.addWidget(self.emo_result,17,0,1,1)

        self.emo_result_ins = QLineEdit()
        self.emo_result_ins.setStyleSheet(globalvariables.StyleScrollGraphHover)
        self.emo_result_ins.resize(150, 40)
        self.grid_insertion.addWidget(self.emo_result_ins ,18,0,1,1)

        if point != {}:
            #Si il s'agit de la correction d'un point, récupération des données du dictionnaire du point
            #Et inscriptions de celles-ci dans chaque case:
            self.situation_ins.setText(self.point["situation"])
            self.emo_ins.setText(str(self.point["emotion"]))
            self.pensee_auto_ins.setText(self.point["pensées_auto"])
            self.conf_label_ins.setText(self.point["confirmation"])
            self.preuves_contr_ins.setText(self.point["preuves_contraires"])
            self.pensee_adap_ins.setText(self.point["pensée_adaptée"])
            self.emo_result_ins.setText(str(self.point["emotion_resultat"]))

        #Boutton d'envoi des attributs:
        self.BouttonRetourAttribut= QPushButton("Envoi")
        self.BouttonRetourAttribut.setStyleSheet(globalvariables.StyleHover)
        self.grid_insertion.addWidget(self.BouttonRetourAttribut ,19,0,1,2)
        self.BouttonRetourAttribut.clicked.connect(lambda x:self.RetourAttributs(self.NumeroPoint,self.numeroGraph))

        self.fen_insertion.show()

    def RetourAttributs(self,NumeroPoint,numeroGraph):
        #Récupération de tous les attributs dans des variables:
        self.situation = self.situation_ins.text()
        if self.situation == "":
            self.situation = "vide"

        self.emotion= self.emo_ins.text()
        if self.emotion == "":
            self.emotion = 0
        else :
            self.emotion = int(self.emotion)

        self.pensee_auto =self.pensee_auto_ins.text()
        if self.pensee_auto == "":
            self.pensee_auto = "vide"

        self.confirmation = self.conf_label_ins.text()
        if self.confirmation == "":
            self.confirmation = "vide"

        self.preuves_contraires = self.preuves_contr_ins.text()
        if self.preuves_contraires == "":
            self.preuves_contraires = "vide"

        self.pensee_adaptee = self.pensee_adap_ins.text()
        if self.pensee_adaptee == "":
            self.pensee_adaptee = "vide"

        self.emotion_resultat= int(self.emo_result_ins.text())
        if self.emotion_resultat== "":
            self.emotion_resultat = 0
        else :
            self.emotion_resultat = int(self.emotion)

        #On les mets dans un point:
        self.nouveau_point= { 'situation': self.situation,'emotion': self.emotion, 'pensées_auto':self.pensee_auto,'confirmation':self.confirmation,'preuves_contraires':self.preuves_contraires,'pensée_adaptée':self.pensee_adaptee,'emotion_resultat':self.emotion_resultat}
        if NumeroPoint == 0 :
            #On rajoute le point a la liste de points:
            globalvariables.InstancePrintGraphClass.liste_points.append(self.nouveau_point)
        else :
            #Sinon on le remplace à l'index voulu:
            globalvariables.InstancePrintGraphClass.liste_points[NumeroPoint] = { 'situation': self.situation,'emotion': self.emotion, 'pensées_auto':self.pensee_auto,'confirmation':self.confirmation,'preuves_contraires':self.preuves_contraires,'pensée_adaptée':self.pensee_adaptee,'emotion_resultat':self.emotion_resultat}

        #On remplace le graph de la BDD par la nouvelle série  de points avec un set sur FireBase:
        print("*******************************************************")
        print("Set FireBase la liste de point du graph suivant:")
        ########moment crucial: copie sur la Base de données FireBase avec un set:
        globalvariables.db.child("users").child(globalvariables.auth.current_user['localId']).child(globalvariables.InstancePrintGraphClass.numero_graph).set(globalvariables.InstancePrintGraphClass.liste_points)
        #Traitement particulier du cas ou il s'agit du tout premier graphique:
        if numeroGraph ==0 :
            print("*******************************************************")
            print("Ajout du nouveau point à la variable self.nouveau_graph:")
            print("Ajout du titre suivant :" + str(globalvariables.InstancePrintGraphClass.liste_points[0]) )
            print("Ajout du point suivant :" + str(self.nouveau_point) )

            self.nouveau_graph= []
            self.nouveau_graph.append(globalvariables.InstancePrintGraphClass.liste_points[0])
            self.nouveau_graph.append(self.nouveau_point)
            globalvariables.copie_results.append(self.nouveau_graph)
            #Ici je relance "Commencer" dans gestion pour avoir une mise à jour des bouttons dans la fenêtre gestion
            globalvariables.gestion.Commencer()

        #Sinon pour la modification du point ou la creation du point d'un graph déjà existant:
        else :
            print("La variable copie_results a été transformée au rang :" + str(numeroGraph))
            print("Par le graph :" + str(globalvariables.InstancePrintGraphClass.liste_points))
            if len(globalvariables.copie_results) != numeroGraph -1:
                globalvariables.copie_results.append([])
                if NumeroPoint == 0:
                    # Ici je relance "Commencer" dans gestion pour avoir une mise à jour des bouttons dans la fenêtre gestion
                    globalvariables.gestion.Commencer()

            #copie de la liste de point augmentée du nouveau point dans la variable globale copie_results:
            globalvariables.copie_results[numeroGraph] = globalvariables.InstancePrintGraphClass.liste_points


        self.fen_insertion.close()
        globalvariables.InstancePrintGraphClass.fen_graph.close()

        instance_PrintGraphClass(globalvariables.InstancePrintGraphClass.numero_graph)

def CreationListeInsertion(point,NumeroPoint,numeroGraph):
    globalvariables.ListeInsertion= ListeInsertion(point,NumeroPoint,numeroGraph)