import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout,QLineEdit

import gestion
import globalvariables
import enregistrement

app = QApplication(sys.argv)


class Identification:
    def __init__(self):

        self.window = QWidget()
        self.window.setWindowTitle("TCC Friend: Inscription")
        self.window.setFixedWidth(500)
        self.window.setStyleSheet(globalvariables.WindowBackground)
        self.grid = QGridLayout()
        self.window.setLayout(self.grid)



        #titre :
        self.label = QLabel("Identification")
        self.label.setStyleSheet(globalvariables.StyleTitre)
        self.grid.addWidget(self.label,0,0,1,2)

        #Qlabel de l'email
        self.label2 = QLabel("Email:")
        self.label2.setStyleSheet(globalvariables.StyleText)
        self.grid.addWidget(self.label2,2,0,1,2)

        #QLineEdit de la saisie du mail
        self.SaisieMail = QLineEdit()
        self.SaisieMail.setStyleSheet(globalvariables.StyleHover)
        self.SaisieMail.resize(150, 40)
        self.grid.addWidget(self.SaisieMail ,3,0,1,2)

        #Qlabel du password:
        self.label3 = QLabel("Password:")
        self.label3.setStyleSheet(globalvariables.StyleText)
        self.grid.addWidget(self.label3,4,0,1,2)

        #QLineEdit de la saisie du password
        self.SaisiePasswd = QLineEdit()
        self.SaisiePasswd.setStyleSheet(globalvariables.StyleHover)
        self.SaisiePasswd.resize(150, 40)
        self.grid.addWidget(self.SaisiePasswd ,5,0,1,2)

        #Boutton de Login:
        self.BouttonIdentification = QPushButton("Envoi")
        self.BouttonIdentification.setStyleSheet(globalvariables.StyleHover)
        self.grid.addWidget(self.BouttonIdentification ,6,0,1,2)
        self.BouttonIdentification.clicked.connect(lambda x:self.LogIn())

        #Boutton d'enregistrement:
        self.BouttonEnregistrement= QPushButton("Enregistrement")
        self.BouttonEnregistrement.setStyleSheet(globalvariables.StyleHover)
        self.grid.addWidget(self.BouttonEnregistrement ,8,0,1,2)
        self.BouttonEnregistrement.clicked.connect(lambda x:self.Enregistrement())



        self.window.show()
        app.exec()

    def Enregistrement(self):
        globalvariables.enregistrement= enregistrement.Enregistrement()
    def LogIn(self):
        self.Email = self.SaisieMail.text()
        self.psswrd = self.SaisiePasswd.text()
        globalvariables.user = globalvariables.auth.sign_in_with_email_and_password(password=self.psswrd, email=self.Email)
        print("***********************************************")
        print('Utilisateur logé avec succes ')
        print("***********************************************")
        print('Info de l\'utilisateur:')
        print(globalvariables.auth.current_user)
        print("***********************************************")
        print(globalvariables.auth)
        globalvariables.gestion= gestion.Gestion()



if __name__ == '__main__':
    globalvariables.debut = Identification()

def start():
    globalvariables.debut = Identification()
