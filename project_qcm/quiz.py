# quiz.py
from question import Question
from reponse import Reponse
import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def run(self):

        score = 0
        note = 0

        random.shuffle(self.questions)

        for question in self.questions:

            note += 1

            random.shuffle(question.responses)

            print(question.texte_question)

            for i, reponse in enumerate(question.responses, start=0):
                print(f"{chr(97 + i)}. {reponse.option}" )

            user_answer = input("Votre réponse (a, b ou c) : ").lower()

            if user_answer in ['a', 'b', 'c']:

                for i, reponse in enumerate(question.responses, start=0):
                   if chr(97 + i) == user_answer:
                       if reponse.answer == True:
                           print("")
                           print("Bonne réponse !")
                           print("")
                           score += 1
                       else:
                           print("")
                           print("Mauvaise réponse !")
                           print("")

            else:
                print("")
                print("Réponse invalide.")
                print("")

        print("Fin du QCM, votre score est de :", score, "sur", note)
        print("")
        print("Voici le corrigé du QCM")

        for question in self.questions:

            print("")
            print(question.texte_question)
            print("")

            for i, reponse in enumerate(question.responses, start=0):
                if reponse.answer == True:
                    print(f"{chr(97 + i)}. {reponse.option} | Bonne réponse")
                else:
                    print(f"{chr(97 + i)}. {reponse.option} | Mauvaise réponse")