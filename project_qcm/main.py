#Importation des fonctions venant des fichiers annexes
from question import Question
from reponse import Reponse
from quiz import Quiz

#Création des réponses et des questions (les réponses doivent être créées avant les questions)
reponses1 = [Reponse("Berlin", False), Reponse("Paris", False), Reponse("Rome", True)]
question1 = Question("Quelle est la capitale de l'Italie?", reponses1)

reponses2 = [Reponse("Madrid", False), Reponse("Lisbonne", True), Reponse("Athènes", False)]
question2 = Question("Quelle est la capitale du Portugal?", reponses2)

reponses3 = [Reponse("Dublin", False), Reponse("Londres", True),Reponse("Amsterdam", False)]
question3 = Question("Quelle est la capitale du Royaume-Uni?", reponses3)

reponses4 = [Reponse("Oslo", True), Reponse("Stockholm", False), Reponse("Copenhague", False)]
question4 = Question("Quelle est la capitale de la Norvège?", reponses4)

reponses5 = [Reponse("Varsovie", True), Reponse("Prague", False), Reponse("Vienne", False)]
question5 = Question("Quelle est la capitale de la Pologne?", reponses5)

reponses6 = [Reponse("Bratislava", False), Reponse("Budapest", True), Reponse("Bucarest", False)]
question6 = Question("Quelle est la capitale de la Hongrie?", reponses6)

reponses7 = [Reponse("Helsinki", False), Reponse("Tallinn", True), Reponse("Vilnius", False)]
question7 = Question("Quelle est la capitale de l'Estonie?", reponses7)

reponses8 = [Reponse("Sofia", True), Reponse("Skopje", False), Reponse("Zagreb", False)]
question8 = Question("Quelle est la capitale de la Bulgarie?", reponses8)

reponses9 = [Reponse("Madrid", False), Reponse("Rome", True), Reponse("Berlin", False)]
question9 = Question("Quelle est la capitale de l'Espagne?", reponses9)

reponses10 = [Reponse("Vienne", False), Reponse("Prague", False), Reponse("Bruxelles", True)]
question10 = Question("Quelle est la capitale de la Belgique?", reponses10)

#Création de la liste des questionsa
questions = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10]

#Création du quiz en se basant sur la liste de question
quiz = Quiz(questions)

#Lancement du quiz
quiz.run()
