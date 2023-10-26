import random
import string

class Generator:

    def __init__(self, lowercase, uppercase, digits, special_chars):
        self.lowercase = lowercase
        self.uppercase = uppercase
        self.digits = digits
        self.special_chars = special_chars

    def run_generator(self):

        password = ''
        length = int(self.lowercase + self.uppercase + self.digits + self.special_chars)

        if length < 8:
            print("Taille du mot de passe trop faible")
            exit()

        lchars = string.ascii_lowercase
        uchars = string.ascii_uppercase
        dchars = string.digits
        schars = "!@#$%^&*()_+=-[]{}|;:'\",.<>/?\\"

        # Générez des caractères aléatoires pour chaque catégorie
        for _ in range(self.lowercase):
            password = password + random.choice(lchars)
        for _ in range(self.uppercase):
            password = password + random.choice(uchars)
        for _ in range (self.digits):
            password = password + random.choice(dchars)
        for _ in range(self.special_chars):
            password = password + random.choice(schars)

        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

        print("Voici le mot de passe généré par le programme :", password)

        return password