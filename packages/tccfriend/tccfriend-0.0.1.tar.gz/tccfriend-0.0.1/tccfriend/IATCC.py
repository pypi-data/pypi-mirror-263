#! /home/terce/.pyenv/pyenv/shims/python3

import globalvariables




class IATCC:
    def __init__(self,chaine_negative,chaine_positive):
        globalvariables.phrases= []
        print("Creation de l'instance de IATCC")
        self.chaine_n= chaine_negative[:3]
        self.chaine_p = chaine_positive[:3]
        print("Chaine émotions négatives de départ:\n "+ str(self.chaine_n))
        print("Chaine émotions résultats de départ:\n "+ str(self.chaine_p))
    def parcours_ligne(self,liste_emotions, chainage_conditions):

        if not chainage_conditions:
            return
        else:
            case_contenu = chainage_conditions[0]  # preparation du contenu d'une case
            case_contenu = case_contenu.split("-")  # on "slice" avec les "-"

        if len(liste_emotions) != 0 and isinstance(liste_emotions[0],
                                                   int):  # recursion ici si la liste d'émotions contient des chiffres

            if case_contenu[0] == "sup" and liste_emotions[0] > int(case_contenu[1]):
                print("t")
                return self.parcours_ligne(liste_emotions[1:], chainage_conditions[1:])

            if case_contenu[0] == "inf" and liste_emotions[0] < int(case_contenu[1]):
                print("t")
                return self.parcours_ligne(liste_emotions[1:], chainage_conditions[1:])

            if case_contenu[0] == "bt" and int(case_contenu[1]) < liste_emotions[0] < int(case_contenu[2]):
                print("t")
                return self.parcours_ligne(liste_emotions[1:], chainage_conditions[1:])

            if case_contenu[0] == "null":
                print("t")
                self.parcours_ligne(liste_emotions[1:], chainage_conditions[1:])


        elif case_contenu[
            0] == "ph":  # sinon, lecture de phrase ici et recursion sur liste vide à la fin de la condition

            print("IA: phrase atteinte.")

            print(case_contenu[1])
            # impression à racorder
            for i in globalvariables.phrases:
                #Si la phrase a déjà été lue, on ne fait rien:
                if i == case_contenu[1]:
                    #Ici on enlève le préfixe de la liste des émotions "positives"
                    self.chaine_p.pop(0)
                    #Et on continue la récursion pour mettre un autre préfixe
                    self.parcours_ligne([], chainage_conditions[1:])

            #Sinon on l'ajoute:
            globalvariables.phrases += [case_contenu[1]]

            self.parcours_ligne([], chainage_conditions[1:])

        elif case_contenu[0] == "add":  # sinon, lecture de add ici et recursion sur liste vide à la fin de la condition
            print("add")
            print("la case est:")
            print(chainage_conditions[0])
            ajout = case_contenu[1]
            self.chaine_p.insert(0, ajout)  # ajout d'un élément sur la chaine d'emotions positives
            self.parcours_ligne([], chainage_conditions[1:])

        elif isinstance(liste_emotions[0], str):  # cas du chainage sur la chaine positive
            print("IA :conditions chainage remplies")
            # print("liste contenu[0]= " + case_contenu[0])
            if liste_emotions[0] != case_contenu[0]:
                print("Chainage negatif")
            if liste_emotions[0] == case_contenu[0]:
                print("Chainage positif")
                self.parcours_ligne(liste_emotions[1:], chainage_conditions[1:])
    def lancement(self):

        print("Le fichier est " + "reglesn.py")
        self.lecture_fichier("reglesn.py")

        print("Le fichier est " + "reglesp.py")
        self.lecture_fichier("reglesp.py")


    def lecture_fichier(self,nom_fichier):
        if nom_fichier == "reglesn.py":
            print("Travail sur la chaine émotions négatives : " + str(self.chaine_n))
            liste_emotions_copy = self.chaine_n.copy()
        elif nom_fichier == "reglesp.py":
            print("Travail sur la chaine émotions négatives : " + str(self.chaine_p))
            liste_emotions_copy = self.chaine_p.copy()
        #Ouverture du fichier:
        f = open(nom_fichier, "r")
        chaine = f.readline()
        chaine= chaine[:-1] # on enlève le retour à la ligne

        self.total_ligne =[]
        self.total_ligne += [chaine]

        #Découpage de chaque ligne dans la variable liste self.total_ligne:
        while chaine:
            chaine = f.readline()
            chaine= chaine[:-1]
            self.total_ligne += [chaine]
        ####################################################
        for ligne in self.total_ligne:
            #Découpage des cases de la ligne:
            cases = ligne.split("|")
            #Parcours de la ligne avec la liste de émotions:
            self.parcours_ligne(liste_emotions_copy, cases)
        f.close()
