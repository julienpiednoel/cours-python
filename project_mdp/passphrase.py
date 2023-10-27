import random

class Passphrase:

    def run_passphrase(self):

        mot = ''
        index = 0
        lnombre = ['1', '2', '3', '4', '5', '6']
        lmot = ['','','','','','']

        while index != 6:

            nombre = ''

            for _ in range(5):
                nombre = nombre + random.choice(lnombre)

            file_path = "eff.txt"

            with open(file_path, 'r') as file:
                for ligne in file:
                    if nombre in ligne:
                        test = ligne.split()
                        mot = test[1]
                        lmot[index] = mot
                        break

            index += 1

        print(end="Voici les mots de votre passphrase : ")

        for words in lmot:
            print(words, end=' ')
