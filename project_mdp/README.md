# Projet 2 : Générateur et Testeur de Mot de Passe

Ce projet consiste en la création d'un programme embarquant des outils de sécurité pour générer et tester des mots de passe. Il inclut un testeur de mot de passe basé sur l'entropie, un générateur de mots de passe aléatoires et un générateur de passphrase.

## Testeur de Mot de Passe

Le testeur de mot de passe évalue la force d'un mot de passe en se basant sur l'entropie et en respectant les critères définis par l'ANSSI (Agence nationale de la sécurité des systèmes d'information). Vous pouvez consulter les critères ici : [Calculer la force d'un mot de passe](https://www.ssi.gouv.fr/administration/precautionselementaires/calculer-la-force-dun-mot-de-passe/).

## Générateur de Mot de Passe Aléatoire

Le générateur de mot de passe aléatoire permet à l'utilisateur de sélectionner des critères pour générer un mot de passe personnalisé. Les critères incluent le nombre de minuscules, de majuscules, de chiffres et de caractères spéciaux. Le programme génère un mot de passe aléatoire qui correspond à ces critères et affiche l'entropie ainsi que la force du mot de passe.

## Générateur de Passphrase

Le générateur de passphrase est basé sur la méthode de dés de l'EFF (Electronic Frontier Foundation). Vous pouvez en apprendre davantage sur cette méthode ici : [Méthode de Dés de l'EFF](https://www.eff.org/fr/dice). Le générateur crée des passphrases sécurisées en utilisant des dés pour obtenir des mots aléatoires.

## Structure du Projet

Le projet est structuré en utilisant des classes et des objets pour organiser le code de manière modulaire. Le code est également séparé en plusieurs fichiers, qui sont importés en tant que modules pour assurer une meilleure gestion du projet.

## Comment Utiliser le Programme

Pour utiliser le programme, suivez les instructions dans les fichiers Python correspondants. Vous pouvez exécuter le testeur de mot de passe, le générateur de mot de passe aléatoire ou le générateur de passphrase en utilisant les fonctions appropriées.