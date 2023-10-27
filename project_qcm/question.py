#Définition de la classe Question
class Question:
    #Définition de mes variables en entrée pour une utilisation local
    def __init__(self, texte_question, responses):
        self.texte_question = texte_question
        self.responses = responses