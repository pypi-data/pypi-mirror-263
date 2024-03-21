import pyrebase


firebaseConfig = {

  "apiKey": "AIzaSyDMx_ejVc9I1M4WoAxgJjzHWsYvx0fYDgo",

  "authDomain": "freetcc-4ffb8.firebaseapp.com",

  "databaseURL": "https://freetcc-4ffb8-default-rtdb.europe-west1.firebasedatabase.app",

  "projectId": "freetcc-4ffb8",

  "storageBucket": "freetcc-4ffb8.appspot.com",

  "messagingSenderId": "55141602566",

 "appId": "1:55141602566:web:92a6af1a5b5c803dca7a87",

  "measurementId": "G-TEJXKX7GK1"

}
#Variables de FireBase:
global firebase
global auth
global db
global storage

#Variables des instances de classes des fenêtres:
global InstancePrintGraphClass
InstancePrintGraphClass = []
global enregistrement
global gestion
global debut # instance de "Insccription"
global instance_cours
global ListeInsertion


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db=firebase.database()
storage=firebase.storage()

#La variable globale qui va recevoir le retour de la Base de donnée (un objet):
global results
#La copie de la variable results sous forme d'une liste de liste (pour chaque graph) contenant une chaine pour
# le titre d'un graph et un dictionnaire pour le point d'un graph:
#Cette copie était nécessaire en raison d'un disfonctionnement de la variable results qui contenait l'objet firebase
#dans certains cas.
global copie_results
copie_results= []

def GetText(FileName):
    f = open(FileName, "r")
    chaine = f.readline()
    text =""
    text += chaine

    while chaine:
        chaine = f.readline()
        text += chaine
    f.close()
    return text

#recupération du CSS de l'ensemble des variables de style:
global WindowBackground
WindowBackground = GetText("WindowBackground.py")

global StyleTitre
StyleTitre = GetText("StyleSheetTitle.py")

global StyleScrollGraph
StyleScrollGraph= GetText("StyleSheetScrollGraph.py")

global StyleText
StyleText = GetText("StyleSheet.py")

global StyleScrollGraphHover
StyleScrollGraphHover = GetText("StyleSheetScrollGraphHover.py")

global StyleHover
StyleHover = GetText("StyleSheetHover.py")

global Licence
Licence = GetText("licence.py")

global CoursTCC
CoursTCC = GetText('cours_TCC.py')

# pour l'IA
global phrases
phrases = []
