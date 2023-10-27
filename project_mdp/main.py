from strength import Entropy
from generator import Generator
from passphrase import Passphrase

print("Kolizion : Projet de gestion de mot de passe")

while True:

    print("\nOptions :")
    print("1. Tester l'entropie et la force d'un mot de passe")
    print("2. Générer un mot de passe fort aléatoirement")
    print("3. Générer une liste de mot pour votre passphrase")
    print("4. Quitter")

    choice = input("Choisissez une option (1/2/3/4) : ")

    match choice:

        case "1":
            password = input("Quel est le mot de passe à tester ?")
            testpassword = Entropy(password)
            testpassword.run_entropy()

        case"2":
            lowercase = int(input("Nombre de minuscule ?"))
            uppercase = int(input("Nombre de majuscule ?"))
            digits = int(input("Nombre de chiffre ?"))
            special_chars = int(input("Nombre de caractères spéciaux ?"))

            gen = Generator(lowercase, uppercase, digits, special_chars)
            password = gen.run_generator()
            testpassword = Entropy(password)
            testpassword .run_entropy()

        case "3":
            phrase = Passphrase()
            phrase.run_passphrase()

        case"4":
            break