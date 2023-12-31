#Importation de la librairie math
import math

#Définition de la classe Entropy
class Entropy:

    #Définition de mes variables en entrée pour une utilisation local
    def __init__(self, password):

        self.password = password

    # Définition d'un fonction run de ma classe Passphrase
    def run_entropy(self):

        # Définition des variables utiles pour le programme
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"
        special_chars = "!@#$%^&*()_+=-[]{}|;:'\",.<>/?"

        # Définition des variables utiles pour le programme
        num_lowercase = 0
        num_uppercase = 0
        num_digits = 0
        num_special_chars = 0

        #Fonction for permettant de se déplace dans le mot de passe de l'utilisateur
        for char in self.password:

            #Fonction if permettant de vérifier si un caractère minuscule est présent dans le mot de passe
            if char in lowercase:
                num_lowercase = 26

            #Fonction elif permettant de vérifier si un caractère majuscule est présent dans le mot de passe
            elif char in uppercase:
                num_uppercase = 26

            #Fonction elif permettant de vérifier si un caractère chiffre est présent dans le mot de passe
            elif char in digits:
                num_digits = 10

            # Fonction elif permettant de vérifier si un caractère spécial est présent dans le mot de passe
            elif char in special_chars:
                num_special_chars = 30

        #Calcule de l'entropie via une formule
        lentropi = round(len(self.password)*math.log2(num_lowercase + num_uppercase + num_digits + num_special_chars))

        #Affichage à l'utilisateur de la valeur de l'entropie du mot de passe et la force (selon l'ANSSI)
        if lentropi < 64:
            print("L'entropie de votre mot de passe est de :", lentropi, "| Votre mot de passe est Très faible selon l'ANSSI")
        elif lentropi >= 64 and lentropi< 80:
            print("L'entropie de votre mot de passe est de :", lentropi, "| Votre mot de passe est Faible selon l'ANSSI")
        elif lentropi>= 80 and lentropi < 100:
            print("L'entropie de votre mot de passe est de :", lentropi, "| Votre mot de passe est Moyen selon l'ANSSI")
        elif lentropi >= 100:
            print("L'entropie de votre mot de passe est de :", lentropi, "| Votre mot de passe est Fort selon l'ANSSI")