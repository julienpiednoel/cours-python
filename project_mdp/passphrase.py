#Importation de la librairie ramdom
import random

#Définition de la classe Passphrase
class Passphrase:

    #Définition d'un fonction run de ma classe Passphrase
    def run_passphrase(self):

        #Initialisation des variables de la fonction
        mot = ''
        index = 0
        lnombre = ['1', '2', '3', '4', '5', '6']
        lmot = ['','','','','','']

        #Boucle while permettant de générer 6 mots aléatoire comme le préconise l'EFF
        while index != 6:

            nombre = ''

            #Génération d'un nombre de 5 chiffres
            for _ in range(5):
                nombre = nombre + random.choice(lnombre)

            #Définition du fichier contenant les mots associés à un nombre
            file_path = "eff.txt"

            #Ouverture du fichier défini précédement
            with open(file_path, 'r') as file:

                #Boucle for permettant de se déplace dans le fichier eff.txt
                for ligne in file:

                    #Test permettant de récupérer la ligne contenant le nombre généré plus haut
                    if nombre in ligne:

                        #Split de la ligne récupéré pour dissocier le nombre et le mot - Format : nombre mot
                        test = ligne.split()

                        #Récupération du mot qui se situe en deuxième position sur ma ligne
                        mot = test[1]

                        #Ajout du mot dans la liste de 6 mots
                        lmot[index] = mot

                        #Fin de la boucle avec break
                        break

            #Incrémentation de l'index pour se déplace dans la liste de mot et générer X nombre
            index += 1

        #Affichage des mots à l'utilisateur
        print(end="Voici les mots de votre passphrase : ")

        #Utilsiation d'une boucle for pour se déplacer dans la liste des mots et les afficher
        for words in lmot:

            #Utilisation de end=' ' pour éviter un retour à la ligne
            print(words, end=' ')
