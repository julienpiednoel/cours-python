#Importation des classes venant des fichiers question et reposne de la librairie ramdom
from question import Question
from reponse import Reponse
import random

#Définition de la classe Quiz
class Quiz:

    #Définition de mes variables en entrée pour une utilisation local
    def __init__(self, questions):
        self.questions = questions

    #Définition d'un fonction run de ma classe Quiz
    def run(self):

        #Définition des variables utiles pour le programme
        score = 0
        note = 0

        #Utilisation de la librairie random pour mélanger les questions
        random.shuffle(self.questions)

        #Utilisation d'une boucle for pour afficher toutes les questions contenu dans l'objet question
        for question in self.questions:

            #Incrémentation du nombre de question posé à l'utilisateur
            note += 1

            #Utilisation de la librairie random pour mélanger les réponses associées à la question
            random.shuffle(question.responses)

            #Affichage du texte de la question
            print(question.texte_question)

            #Boucle for permettant d'afficher les réponses avec les lettres a, b et c
            for i, reponse in enumerate(question.responses, start=0):
                print(f"{chr(97 + i)}. {reponse.option}" )

            #Demande à l'utilisateur de rentrer une réponse, ajout de lower() pour transformer les majuscules en minuscules en cas d'erreur de l'utilisateur
            user_answer = input("Votre réponse (a, b ou c) : ").lower()

            #Vérification via une boucle if de la réponse de l'utilisateur si la réponse est différente de a, b ou c la réponse est définie comme invalide
            if user_answer in ['a', 'b', 'c']:

                #Boucle for permettant de vérifier si la réponse de l'utilisateur correspond à la réponse de la question
                for i, reponse in enumerate(question.responses, start=0):
                   if chr(97 + i) == user_answer:

                       #Chaque réponse à un statut true ou false ce qui permet de définir la bonne réponse ou la mauvaise. La programme se base sur cette option pour vérifier la réponse
                       if reponse.answer == True:

                           #Affichage du résultat de la réponse et incrémentation du score de l'utilisateur
                           print("")
                           print("Bonne réponse !")
                           print("")
                           score += 1
                       else:

                           #Affichage du résultat de la réponse
                           print("")
                           print("Mauvaise réponse !")
                           print("")

            else:

                #Affichage de l'erreur
                print("")
                print("Réponse invalide.")
                print("")

        #Affichage du score de l'utilisateur
        print("Fin du QCM, votre score est de :", score, "sur", note)
        print("")
        print("Voici le corrigé du QCM")

        #Utilisation de la même boucle for que précédement pour afficher les questions pour le corrigé
        for question in self.questions:

            # Affichage du texte de la question
            print("")
            print(question.texte_question)
            print("")

            #Boucle for permettant d'afficher les réponses et d'associé le staut de la réponse
            for i, reponse in enumerate(question.responses, start=0):
                if reponse.answer == True:

                    #Si le statut est True alors affichage de bonne réponse à côte de la réponse
                    print(f"{chr(97 + i)}. {reponse.option} | Bonne réponse")
                else:

                    #Si le statut est False alors affichage de mauvaise réponse à côte de la réponse
                    print(f"{chr(97 + i)}. {reponse.option} | Mauvaise réponse")