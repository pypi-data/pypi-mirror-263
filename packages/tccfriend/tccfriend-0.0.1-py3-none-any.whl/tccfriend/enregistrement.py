
from PyQt5.QtWidgets import QLabel, QPushButton,  QWidget,  QGridLayout,QLineEdit
import gestion
import globalvariables

class Enregistrement:
    def __init__(self):
        #Fenêtre et paramètres de fenêtre:
        self.enregitrement = QWidget()
        self.enregitrement.setWindowTitle("TCC Friend: Enregitrement")
        self.enregitrement.setFixedWidth(500)
        self.enregitrement.setStyleSheet(globalvariables.WindowBackground)
        self.grid = QGridLayout()
        self.enregitrement.setLayout(self.grid)

        #Qlabel "Enregristrement"
        self.label = QLabel("Enregistrement")
        self.label.setStyleSheet(globalvariables.StyleTitre)
        self.grid.addWidget(self.label, 0, 0, 1, 2)
        #Qlabel "Email"
        self.label2 = QLabel("Email:")
        self.label2.setStyleSheet(globalvariables.StyleText)
        self.grid.addWidget(self.label2, 2, 0, 1, 2)
        #QlineEdit de saisie de mail
        self.SaisieMail = QLineEdit()
        self.SaisieMail.setStyleSheet(globalvariables.StyleHover)
        self.SaisieMail.resize(150, 40)
        self.grid.addWidget(self.SaisieMail, 3, 0, 1, 2)
        #Qlabel "Password"
        self.label3 = QLabel("Password:")
        self.label3.setStyleSheet(globalvariables.StyleText)
        self.grid.addWidget(self.label3, 4, 0, 1, 2)
        #QlineEdit de saisie de password
        self.SaisiePasswd = QLineEdit()
        self.SaisiePasswd.setStyleSheet(globalvariables.StyleHover)
        self.SaisiePasswd.resize(150, 40)
        self.grid.addWidget(self.SaisiePasswd, 5, 0, 1, 2)
        #Boutton d'enregistrement
        self.BouttonEnregistrement = QPushButton("Envoi")
        self.BouttonEnregistrement.setStyleSheet(globalvariables.StyleHover)
        self.grid.addWidget(self.BouttonEnregistrement, 6, 0, 1, 2)
        self.BouttonEnregistrement.clicked.connect(lambda x: self.SignIn())
        #Affichage fenêtre:
        self.enregitrement.show()


    def SignIn(self):
        self.Email = self.SaisieMail.text()
        self.psswrd = self.SaisiePasswd.text()
        globalvariables.user = globalvariables.auth.create_user_with_email_and_password(password=self.psswrd,
                                                                                    email=self.Email)
        globalvariables.user = globalvariables.auth.sign_in_with_email_and_password(password=self.psswrd,
                                                                                    email=self.Email)
        #globalvariables.db.child("users").set(globalvariables.auth.current_user['localId'])
        print("***********************************************")
        print('Utilisateur enregistré avec succes ')
        print("***********************************************")
        print('Info de l\'utilisateur:')
        print(globalvariables.auth.current_user)
        print("***********************************************")
        print(globalvariables.auth)
        #Lancement de la fenêtre Gestion (classe Gestion du fichier gestion.py)
        globalvariables.gestion= gestion.Gestion()