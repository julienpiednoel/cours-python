import math

class Entropy:
    def __init__(self, password):

        self.password = password

    def run_entropy(self):

        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"
        special_chars = "!@#$%^&*()_+=-[]{}|;:'\",.<>/?"

        num_lowercase = 0
        num_uppercase = 0
        num_digits = 0
        num_special_chars = 0

        for char in self.password:
            if char in lowercase:
                num_lowercase = 26
            elif char in uppercase:
                num_uppercase = 26
            elif char in digits:
                num_digits = 10
            elif char in special_chars:
                num_special_chars = 30

        lentropi = round(len(self.password)*math.log2(num_lowercase + num_uppercase + num_digits + num_special_chars))

        if lentropi < 64:
            print("L'entropie de votre mot de passe est de :", lentropi, "| Votre mot de passe est Très faible selon l'ANSSI")
        elif lentropi >= 64 and lentropi< 80:
            print("L'entropie de votre mot de passe est de :", lentropi, "| Votre mot de passe est Faible selon l'ANSSI")
        elif lentropi>= 80 and lentropi < 100:
            print("L'entropie de votre mot de passe est de :", lentropi, "| Votre mot de passe est Moyen selon l'ANSSI")
        elif lentropi >= 100:
            print("L'entropie de votre mot de passe est de :", lentropi, "| Votre mot de passe est Fort selon l'ANSSI")