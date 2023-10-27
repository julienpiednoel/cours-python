#Importation de la librairie ramdom et string
import random
import string

#Définition de la classe Generator
class Generator:

    #Définition de mes variables en entrée pour une utilisation local
    def __init__(self, lowercase, uppercase, digits, special_chars):
        self.lowercase = lowercase
        self.uppercase = uppercase
        self.digits = digits
        self.special_chars = special_chars

    #Définition d'un fonction run de ma classe Generator
    def run_generator(self):

        #Définition des variables utiles pour le programme
        password = ''

        #Taille du mot de passe à générer
        length = int(self.lowercase + self.uppercase + self.digits + self.special_chars)

        #Test permettant de refuser la génération de mot de passe trop court
        if length < 8:
            print("Taille du mot de passe trop faible")
            exit()

        #Utilisation de la librairie string pour récupérer la liste de caractères minuscules, majuscules et les chiffres
        lchars = string.ascii_lowercase
        uchars = string.ascii_uppercase
        dchars = string.digits

        #Définition manuelle des caractères spéciaux
        schars = "!@#$%^&*()_+=-[]{}|;:'\",.<>/?\\"

        #Générez des caractères aléatoires pour chaque catégorie et ajout des caractères dans un string
        for _ in range(self.lowercase):
            password = password + random.choice(lchars)
        for _ in range(self.uppercase):
            password = password + random.choice(uchars)
        for _ in range (self.digits):
            password = password + random.choice(dchars)
        for _ in range(self.special_chars):
            password = password + random.choice(schars)

        #Transformation de mon string en liste
        password_list = list(password)

        #Utilisation de la librairie random pour mélanger aléatoirement les caractères de la liste
        random.shuffle(password_list)

        # Transformation de ma liste en string
        password = ''.join(password_list)

        #Affichage à l'utilisateur du mot de passe généré
        print("Voici le mot de passe généré par le programme :", password)

        #La fonction retourne le mot de passe pour une utilisation externe
        return password