#Importation des fonctions venant des fichiers annexes
from question import Question
from reponse import Reponse
from quiz import Quiz
import unittest


class TestReponse(unittest.TestCase):
    def test_quiz(self):

        #Création des réponses et des questions (les réponses doivent être créées avant les questions)
        reponses = [Reponse("Berlin", False), Reponse("Paris", False), Reponse("Rome", True)]
        question = Question("Quelle est la capitale de l'Italie?", reponses)

        questions = [question]

        for i, reponse in enumerate(question.responses, start=0):
            if reponse.answer == True:

                # Si le statut est True alors affichage de bonne réponse à côte de la réponse
                print("La réponse True fonctionne")
            else:

                # Si le statut est False alors affichage de mauvaise réponse à côte de la réponse
                print("La réponse False fonctionne")

        quiz = Quiz(questions)

        quiz.run()

if __name__ == "__main__":
    unittest.main()