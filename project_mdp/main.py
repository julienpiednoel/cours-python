from strength import Entropy
from generator import Generator
from passphrase import Passphrase

#password = input("Quel est le mot de passe à tester ?")

lowercase = int(input("Nombre de minuscule ?"))
uppercase = int(input("Nombre de majuscule ?"))
digits = int(input("Nombre de chiffre ?"))
special_chars = int(input("Nombre de caractères spéciaux ?"))

gen = Generator(lowercase, uppercase, digits, special_chars)

password = gen.run_generator()

montest = Entropy(password)

montest.run_entropy()
