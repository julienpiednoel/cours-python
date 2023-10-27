#Importation des fonctions venant des fichiers annexes
from strength import Entropy
from generator import Generator
from passphrase import Passphrase

#Début de l'affichage utilisateur
print("Kolizion : Projet de gestion de mot de passe")

#Boucle while permettant d'afficher le menu en continu seul l'option 4 ou un arrêt de force du programme permet d'arrêter l'exécution
while True:

    print("\nOptions :")
    print("1. Tester l'entropie et la force d'un mot de passe")
    print("2. Générer un mot de passe fort aléatoirement")
    print("3. Générer une liste de mot pour votre passphrase")
    print("4. Quitter")

    choice = input("Choisissez une option (1/2/3/4) : ")

    #Mise en place d'un match pour permettre à l'utilisateur d'être dirigé vers les bonnes fonctions
    match choice:

        #Partie permettant à l'utilisateur de tester un mot de passe
        case "1":

            #Demande à l'utilisateur du mot de passe à tester
            password = input("Quel est le mot de passe à tester ?")
            #Création de l'objet testpassword (de type Entropy) permettant d'appeler la focntion de test de mot de passe
            testpassword = Entropy(password)
            #Lancement de la fonction run_entropy permettant de tester un mot de passe
            testpassword.run_entropy()

        #Partie permettant à l'utilisateur de générer un mot de passe customisé
        case"2":

            #Demande à l'utilisateur de la composition du mot de passe à générer
            lowercase = int(input("Nombre de minuscule ?"))
            uppercase = int(input("Nombre de majuscule ?"))
            digits = int(input("Nombre de chiffre ?"))
            special_chars = int(input("Nombre de caractères spéciaux ?"))

            #Création de l'objet gen (de type Generator)permettant d'appeler la fonction de génération de mot de passe
            gen = Generator(lowercase, uppercase, digits, special_chars)
            # Lancement de la fonction run_generator permettant de générer un mot de passe
            password = gen.run_generator()
            # Création de l'objet testpassword (de type Entropy) permettant d'appeler la focntion de test de mot de passe
            testpassword = Entropy(password)
            # Lancement de la fonction run_entropy permettant de tester un mot de passe
            testpassword .run_entropy()

        #Partie permettant à l'utilisateur de générer des mots aléatoire pour créer une passphrase
        case "3":

            #Création de l'objet phrase (de type Passphrase)permettant d'appeler la fonction de génération de mot
            phrase = Passphrase()
            # Lancement de la fonction run_passphrase permettant de générer les mots
            phrase.run_passphrase()

        #Partie permettant à l'utilisateur de quitter le programme
        case"4":

            #Utilisation d'un break pour terminer le programme
            break