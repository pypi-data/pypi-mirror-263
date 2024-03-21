from PyQt5.QtWidgets import  QLabel,  QVBoxLayout, QWidget,  QGridLayout, QScrollArea
import globalvariables
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Cours_TCC:
    def __init__(self):
        #fenêtre et paramètres:
        self.CoursWindow = QWidget()  # creation d'une fenêtre
        self.CoursWindow.setFixedWidth(1000)
        self.CoursWindow.setStyleSheet(globalvariables.WindowBackground)
        self.CoursWindow.setFixedHeight(1000)
        self.grid = QGridLayout()
        self.CoursWindow.setLayout(self.grid)

        #Récupération du fichier texte "cours_TCC.txt" dans le fichier globalvariables.py
        self.TextCours= globalvariables.CoursTCC

        #Qlabel du texte:
        self.LabelText = QLabel(self.TextCours)
        self.LabelText.setStyleSheet(globalvariables.StyleScrollGraph)

        #Fabrication du scroll:
        self.scroll = QScrollArea()
        #Widget qui va contenir le "layout" de boite
        self.widget = QWidget()
        #Layout de boite verticale :
        self.vbox = QVBoxLayout()
        #Ajout du texte dans le Layout de la boite:
        self.vbox.addWidget(self.LabelText)
        #Ajout du layout de vbox au Widget créé plus haut
        self.widget.setLayout(self.vbox)
        #Paramètres du scroll vertical:
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        #Paramètres du scroll Horizontal:
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        #"Linkage" du scroll au widget
        self.scroll.setWidget(self.widget)
        #Ajout du scroll à la grille de la fenêtre principale:
        self.grid.addWidget(self.scroll,4,0,1,2)


        self.CoursWindow.show()
