#!/usr/bin/env python3

import logging

from logging.handlers import RotatingFileHandler
 
# création de l'objet logger qui va nous servir à écrire dans les logs
logger = logging.getLogger()
# on met le niveau du logger à DEBUG, comme ça il écrit tout
logger.setLevel(logging.DEBUG)
 
# création d'un formateur qui va ajouter le temps, le niveau
# de chaque message quand on écrira un message dans le log
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
# création d'un handler qui va rediriger une écriture du log vers
# un fichier en mode 'append', avec 1 backup et une taille max de 1Mo
file_handler = RotatingFileHandler('log.txt', 'a', 1000000, 1)
# on lui met le niveau sur DEBUG, on lui dit qu'il doit utiliser le formateur
# créé précédement et on ajoute ce handler au logger
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info("Start log")

my_word='maison'
error_count=0
test_letter=0

#Affichage du mot vide
i=0
for i in range(len(my_word)):
    print("__ ", end='')

logger.info("le mot à trouver est:")
logger.info(my_word)

def test_letter_function(user_letter,game_word):
    for i in game_word :
        if i == user_letter:
            number = 1
            return number
    number = 0
    return number
    

while error_count <= 5 :

    my_letter = input("Entrer une lettre:")
    logger.info("la lettre de l'user est:")
    logger.info(my_letter)

    test_letter= test_letter_function(my_letter,my_word)

    print(test_letter)