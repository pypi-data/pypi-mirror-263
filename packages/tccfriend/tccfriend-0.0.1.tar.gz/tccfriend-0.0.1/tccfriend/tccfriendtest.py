import sys
import unittest
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout,QLineEdit
import main
import courstcc
import globalvariables
import random
import printgraphclass
import gestion
import enregistrement
from PyQt5.QtTest import QTest



#class TestConnexionBDD(unittest.TestCase):
    #def test_enregistrement(self):
        #generation de comptes automatiques avec un random
    #    self.psswrd= random.randrange(600000,10000000)
    #    self.Email = str(random.randrange(600,100000))+"@"+str(random.randrange(600,100000))+".com"
    #    user = globalvariables.auth.create_user_with_email_and_password(password=self.psswrd, email=self.Email)
    #    globalvariables.auth.sign_in_with_email_and_password(password=self.psswrd, email=self.Email)
    #    self.assertIsNotNone(globalvariables.auth.current_user)
    #def test_connexion_FireBase(self):
        # connexion avec le compte de test:
    #    self.psswrd= "testing"
    #    self.Email= "test@test.com"
    #    user = globalvariables.auth.sign_in_with_email_and_password(password=self.psswrd, email=self.Email)
    #    self.assertIsNotNone(globalvariables.auth.current_user)


    #globalvariables.results = globalvariables.db.child("users").child(globalvariables.auth.current_user['localId']).get()



class TestFenetres(unittest.TestCase):


    def test_instance_of_identification(self):
        print("Test de test_instance_of_identification")
        fen_identification = main.Identification() # lancement d'une instance de la classe
        self.assertIsInstance(fen_identification,main.Identification)

        #test des cases d'entrées:
        self.assertIsNotNone(fen_identification.window)
        self.assertIsNotNone(fen_identification.grid)
        #test de la bonne création des widgets et bouttons:
        self.assertIsNotNone(fen_identification.label)
        self.assertIsNotNone(fen_identification.label2)
        self.assertIsNotNone(fen_identification.SaisieMail)
        self.assertIsNotNone(fen_identification.label3)
        self.assertIsNotNone(fen_identification.SaisiePasswd)
        self.assertIsNotNone(fen_identification.BouttonIdentification)
        self.assertIsNotNone(fen_identification.BouttonEnregistrement)

        #Test du boutton d'identification:
        fen_identification.SaisieMail.setText("test@test.com")
        fen_identification.SaisiePasswd.setText("testing")
        QTest.mouseClick(fen_identification.BouttonIdentification,Qt.LeftButton)
        #Test si l'identification a bien eu lieu
        self.assertIsNotNone(globalvariables.auth.current_user)
        #Test du boutton d'Enregistrement:
        QTest.mouseClick(fen_identification.BouttonEnregistrement,Qt.LeftButton)
    def test_instance_of_enregistrement(self):
        print("Test de test_instance_of_enregistrement")
        fen_enregistrement = enregistrement.Enregistrement() # lancement d'une instance de la classe
        self.assertIsInstance(fen_enregistrement,enregistrement.Enregistrement)



        self.assertIsNotNone(fen_enregistrement.enregitrement)
        self.assertIsNotNone(fen_enregistrement.grid)
        #test de la bonne création des widgets et bouttons:
        self.assertIsNotNone(fen_enregistrement.label)
        self.assertIsNotNone(fen_enregistrement.label2)
        self.assertIsNotNone(fen_enregistrement.SaisieMail)
        self.assertIsNotNone(fen_enregistrement.label3)
        self.assertIsNotNone(fen_enregistrement.SaisiePasswd)
        self.assertIsNotNone(fen_enregistrement.BouttonEnregistrement)

        self.psswrd = random.randrange(600000, 10000000)
        self.Email = str(random.randrange(600, 100000)) + "@" + str(random.randrange(600, 100000)) + ".com"
        print("Mot de passe est :"+ str(self.psswrd))
        print("L'email est :" + self.Email)
        #Test du boutton d'enregistrement:
        fen_enregistrement.SaisieMail.setText(str(self.Email))
        fen_enregistrement.SaisiePasswd.setText(str(self.psswrd))
        QTest.mouseClick(fen_enregistrement.BouttonEnregistrement,Qt.LeftButton)
        self.assertIsNotNone(globalvariables.user)
    def test_instance_of_courstcc(self):
        print("Test de test_instance_of_courstcc")
        fen_courstcc = courstcc.Cours_TCC() # lancement d'une instance de la classe



        self.assertIsInstance(fen_courstcc,courstcc.Cours_TCC)
        self.assertIsNotNone(fen_courstcc.grid)
        self.assertIsNotNone(fen_courstcc.LabelText)
        self.assertIsNotNone(fen_courstcc.scroll)
        self.assertIsNotNone(fen_courstcc.widget)
        self.assertIsNotNone(fen_courstcc.vbox)


    def test_instance_of_gestion(self):
        print("Test de test_instance_of_gestion")
        globalvariables.gestion = gestion.Gestion()
        self.assertIsInstance(globalvariables.gestion,gestion.Gestion)
        self.assertIsNotNone(globalvariables.gestion.gestion)  # test de la fenêtre
        self.assertIsNotNone(globalvariables.gestion.grid)     # test de la grille de layout
        self.assertIsNotNone(globalvariables.gestion.BouttonSignOut)
        self.assertIsNotNone(globalvariables.gestion.BouttonCommencer)



        #Sign in pour que les fonctions soient valides:
        self.psswrd= "testing"
        self.Email= "test@test.com"
        user = globalvariables.auth.sign_in_with_email_and_password(password=self.psswrd, email=self.Email)
        globalvariables.results = globalvariables.db.child("users").child(globalvariables.auth.current_user['localId']).get()


        # Test du click sur les bouttons:
        QTest.mouseClick(globalvariables.gestion.BouttonCommencer,Qt.LeftButton) #lancement de commencer
        QTest.mouseClick(globalvariables.gestion.Boutton_nouveauG.BouttonNouveauGraph,Qt.LeftButton)

        #QTest.mouseClick(globalvariables.gestion.BouttonSignOut,Qt.LeftButton) # SignOut




    def test_instance_of_BouttonDePoint(self):
        self.psswrd = "testing"
        self.Email = "test@test.com"
        globalvariables.user = globalvariables.auth.sign_in_with_email_and_password(password=self.psswrd, email=self.Email)
        print("globalvariables.auth.current_user['localId']")
        print(globalvariables.auth.current_user['localId'])
        #Get sur la base de données au niveau de l'utilisateur:
        globalvariables.results = globalvariables.db.child("users").child(globalvariables.auth.current_user['localId']).get()
        globalvariables.copie_results = globalvariables.results.val().copy()

        # création d'une instance de PrintGraphClass pour créer des bouttons:
        printgraphclass.instance_PrintGraphClass(0)
        #Création d'une instance de printgraphclass:
        self.fen_fenetrePrintGraph = printgraphclass.PrintGraphClass(0)
        self.assertIsInstance(self.fen_fenetrePrintGraph, printgraphclass.PrintGraphClass)
        #Fabrication d'un boutton pour la liste de scrolls :
        self.Boutton = printgraphclass.BouttonDePoint(self.fen_fenetrePrintGraph,2,{'confirmation': 'confirmation', 'emotion': 2, 'emotion_resultat': 2, 'pensée_adaptée': 'pensée_adaptée', 'pensées_auto': 'pensées_auto', 'preuves_contraires': 'pensée_adaptée', 'situation': 'situation'})
        QTest.mouseClick(self.Boutton.BouttonListePoints,Qt.LeftButton) # test du click sur le boutton fabriqué.

    def test_instance_of_PrintGraph(self):

        print("Test de test_instance_of_PrintGraph")
        # Sign in pour que les fonctions soient valides:
        self.psswrd = "testing"
        self.Email = "test@test.com"
        user = globalvariables.auth.sign_in_with_email_and_password(password=self.psswrd, email=self.Email)
        globalvariables.results = globalvariables.db.child("users").child(globalvariables.auth.current_user['localId']).get()
        #copie de copie_results conformément au code de la fonction "commencer" de gestion:
        globalvariables.copie_results = globalvariables.results.val()
        #Creation d'une instance de gestion pour la validité des tests plus bas:
        globalvariables.gestion = gestion.Gestion()
        # création d'une instance de PrintGraphClass pour créer des bouttons:
        printgraphclass.instance_PrintGraphClass(0)
        self.fen_fenetrePrintGraph = printgraphclass.PrintGraphClass(0)
        self.assertIsInstance(self.fen_fenetrePrintGraph, printgraphclass.PrintGraphClass)

        self.assertIsNotNone(self.fen_fenetrePrintGraph.fen_graph)
        self.assertIsNotNone(self.fen_fenetrePrintGraph.grid)
        self.assertIsNotNone(self.fen_fenetrePrintGraph.label3)
        self.assertIsNotNone(self.fen_fenetrePrintGraph.BouttonGraph2)
        self.assertIsNotNone(self.fen_fenetrePrintGraph.titre)
        self.assertIsNotNone(self.fen_fenetrePrintGraph.BouttonNouveauPoint)
        self.assertIsNotNone(self.fen_fenetrePrintGraph.scroll)
        self.assertIsNotNone(self.fen_fenetrePrintGraph.canvas)
        #Test du boutton de switch du graph
        QTest.mouseClick(self.fen_fenetrePrintGraph.BouttonGraph2,Qt.LeftButton)
        # Test de creation d'un nouveau point
        QTest.mouseClick(self.fen_fenetrePrintGraph.BouttonNouveauPoint,Qt.LeftButton)
        # Test de la creation d'une fenêtre d'ajout d'un point:

        self.fen_insertion = printgraphclass.ListeInsertion({},0 ,0)
        self.assertIsNotNone(self.fen_insertion .fen_insertion)
        self.assertIsNotNone(self.fen_insertion .scroll2)
        self.assertIsNotNone(self.fen_insertion .grid_insertion1)
        self.assertIsNotNone(self.fen_insertion .widget_insertion)
        self.assertIsNotNone(self.fen_insertion .grid_insertion)
        self.assertIsNotNone(self.fen_insertion .vboxlayout)
        # Test de la création de tous les Qlabels et QlineEdit avec les insertions:
        self.assertIsNotNone(self.fen_insertion .situation)
        self.assertIsNotNone(self.fen_insertion .situation_ins)
        self.fen_insertion .situation_ins.setText("Test")

        self.assertIsNotNone(self.fen_insertion .emo_label)
        self.assertIsNotNone(self.fen_insertion .emo_ins)
        self.fen_insertion .emo_ins.insert("4")

        self.assertIsNotNone(self.fen_insertion .pensee_auto)
        self.assertIsNotNone(self.fen_insertion .pensee_auto_ins)
        self.fen_insertion .pensee_auto_ins.setText("Test")

        self.assertIsNotNone(self.fen_insertion .conf_label)
        self.assertIsNotNone(self.fen_insertion .conf_label_ins)
        self.fen_insertion .conf_label_ins.setText("Test")

        self.assertIsNotNone(self.fen_insertion .preuves_contr)
        self.assertIsNotNone(self.fen_insertion .preuves_contr_ins)
        self.fen_insertion .preuves_contr_ins.setText("Test")

        self.assertIsNotNone(self.fen_insertion .pensee_adap)
        self.assertIsNotNone(self.fen_insertion .pensee_adap_ins)
        self.fen_insertion .pensee_adap_ins.setText("Test")

        self.assertIsNotNone(self.fen_insertion .emo_result)
        self.assertIsNotNone(self.fen_insertion .emo_result_ins)
        self.fen_insertion .emo_result_ins.insert("3")

        self.assertIsNotNone(self.fen_insertion .BouttonRetourAttribut)
        #Envoi des attributs
        QTest.mouseClick(self.fen_insertion .BouttonRetourAttribut,Qt.LeftButton)
        #Test du scroll des bouttons de points dans la fenêtre de printgraphclass:
        self.assertIsNotNone(self.fen_fenetrePrintGraph.widget)
        self.assertIsNotNone(self.fen_fenetrePrintGraph.vbox)
        self.assertIsNotNone(self.fen_fenetrePrintGraph.scroll)
        self.assertIsNotNone(self.fen_fenetrePrintGraph.grid)


    def test_instance_of_FenetreNouveauGraph(self):
        print("Test de test_instance_of_FenetreNouveauGraph")
        #Sign in pour que les fonctions soient valides:
        self.psswrd= "testing"
        self.Email= "test@test.com"
        user = globalvariables.auth.sign_in_with_email_and_password(password=self.psswrd, email=self.Email)
        globalvariables.results = globalvariables.db.child("users").child(globalvariables.auth.current_user['localId']).get()



        fen_fenetrenouveaugraph = printgraphclass.PrintGraphClass(None)
        self.assertIsInstance(fen_fenetrenouveaugraph,printgraphclass.PrintGraphClass)
        #test des labels et bouttons:
        self.assertIsNotNone(fen_fenetrenouveaugraph.fen_graph)
        self.assertIsNotNone(fen_fenetrenouveaugraph.grid)
        self.assertIsNotNone(fen_fenetrenouveaugraph.titre_nouveau_g_ins)
        self.assertIsNotNone(fen_fenetrenouveaugraph.label_titre_nouveau_graph)
        self.assertIsNotNone(fen_fenetrenouveaugraph.Boutton_nouveau_titre)

        #Test du boutton de la création d'un nouveau graph:
        fen_fenetrenouveaugraph.titre_nouveau_g_ins.setText("Test")
        QTest.mouseClick(fen_fenetrenouveaugraph.Boutton_nouveau_titre,Qt.LeftButton)


    def test_instance_of_Class_bouttons(self):
        print("Test de test_instance_of_Class_bouttons")
        # Sign in pour que les fonctions soient valides:
        self.psswrd = "testing"
        self.Email = "test@test.com"
        user = globalvariables.auth.sign_in_with_email_and_password(password=self.psswrd, email=self.Email)
        globalvariables.results = globalvariables.db.child("users").child(
            globalvariables.auth.current_user['localId']).get()
        #copie de copie_results conformément au code de la fonction "commencer" de gestion:
        globalvariables.copie_results = globalvariables.results.val()


        # Creation d'une instance de gestion pour recevoir le boutton:
        globalvariables.gestion = gestion.Gestion()
        # Création d'une instance de class_boutton:
        self.class_boutton = gestion.Class_bouttons("test", "nom_boutton", 4)
        self.assertIsInstance(self.class_boutton, gestion.Class_bouttons)
        # Test du clique que le boutton:
        QTest.mouseClick(self.class_boutton.BouttonGraphique, Qt.LeftButton)



if __name__ == '__main__':
    unittest.main()

def starttest():
    unittest.main()
