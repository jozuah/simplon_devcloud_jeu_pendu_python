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
my_word_empty=[]

def test_letter_function(user_letter,game_word):
    for i in game_word :
        if i == user_letter:
            number = 1
            logger.info("L'utilisateur a entré une lettre valide")
            return number
    number = 0
    logger.info("L'utilisateur n'a pas entré une lettre valide")
    return number

my_word_as_list=list(my_word)
b=0
for b in range(len(my_word)):
    my_word_empty.append('_')

print(my_word_empty)


#Affichage du mot vide
i=0
for i in range(len(my_word)):
    print("__ ", end='')

logger.info("le mot à trouver est:")
logger.info(my_word)


    

while error_count < 5 :

    my_letter = input("\nEntrer une lettre:")
    logger.info("la lettre de l'user est:")
    logger.info(my_letter)

    test_letter= test_letter_function(my_letter,my_word)

    if(test_letter==0):
        print(my_letter, " n'est pas une lettre du mot caché")
        error_count = error_count + 1
        logger.info("Nombre d'erreurs actuel")
        logger.info(error_count)

    elif(test_letter==1):
        for compteur in range (len(my_word)):
            if my_letter == my_word_as_list[compteur]:
                my_word_empty[compteur]=my_word_as_list[compteur]
        logger.info(my_word_empty)

    my_word_empty_str=' '.join(map(str,my_word_empty))
    print(my_word_empty_str)

        

print("jeu perdu")