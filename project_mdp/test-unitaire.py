#Test unitaire (`test_pass.py`)
from strength import Entropy
from generator import Generator
from passphrase import Passphrase
import unittest

class Test(unittest.TestCase):

    # Test de force mot de passe faible
    def test_mdp_faible(self):
        password = "EsieeIT"
        print("Voici le résultat du test : ", password)
        test = Entropy(password)
        test.run_entropy()
        print(' ')

    # Test de force mot de passe fort
    def test_mdp_fort(self):
        password = "eRV5i_UONnhiRJ8"
        print("Voici le résultat du test : ", password)
        test = Entropy(password)
        test.run_entropy()
        print(' ')

    # Test génération mot de passe
    def test_gen_password(self):

        lowercase = 4
        uppercase = 4
        digits = 4
        special_chars = 4

        #Création de l'objet gen (de type Generator)permettant d'appeler la fonction de génération de mot de passe
        gen = Generator(lowercase, uppercase, digits, special_chars)

        #Lancement de la fonction run_generator permettant de générer un mot de passe
        password = gen.run_generator()

        #Création de l'objet testpassword (de type Entropy) permettant d'appeler la focntion de test de mot de passe
        testpassword = Entropy(password)

        #Lancement de la fonction run_entropy permettant de tester un mot de passe
        testpassword.run_entropy()

        print(' ')

    # Test génération passphrase
    def test_gen_passphrase(self):

        # Création de l'objet phrase (de type Passphrase)permettant d'appeler la fonction de génération de mot
        phrase = Passphrase()

        # Lancement de la fonction run_passphrase permettant de générer les mots
        phrase.run_passphrase()

        print(' ')

if __name__ == '__main__':
    unittest.main()