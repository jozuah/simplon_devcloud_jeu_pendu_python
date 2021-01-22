#!/usr/bin/env python3

import logging

from logging.handlers import RotatingFileHandler
# création de l'objet logger qui va nous servir à écrire dans les logs
logger = logging.getLogger()

def main(): 
    
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


    ### Reset du fichier log
    my_txt_file= open("log.txt", "r+")    
    # to erase all data  
    my_txt_file.truncate() 
    # to close file
    my_txt_file.close() 


    logger.info("Start log")


    from random_words import RandomWords
    rw = RandomWords()


    my_word = rw.random_word()
    error_count=0
    test_letter=0
    word_complete=0
    max_error=5
    my_word_empty=[]
    my_letter=0
    HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    =========''']

    #Fonction qui teste si une lettre est contenue dans un mot
    def test_letter_function(user_letter,game_word):
        for i in game_word :
            if i == user_letter:
                logger.info("L'utilisateur a entré une lettre valide contenue dans le mot à trouver")
                return 1
        logger.info("L'utilisateur n'a pas entré une lettre contenue dans le mot à trouver")
        return 0

    #Fonction qui test si le mot a cherché est completement trouvé
    def test_full_word (my_current_list):       
        for item in my_current_list: 
            if item == '_':
                logger.info("Le mot n'a pas été trouvé totalement")
                return 0
        logger.info("Le mot a été trouvé totalement")
        return 1

    #Fonction qui s'assure que l'utilisateur a mis une lettre
    def test_true_letter():
        while True:
            my_user_letter = input("\n\nEntrer une lettre:")
            logger.info("l'input de l'user est:")
            logger.info(my_user_letter)
            
            if len(my_user_letter)==1 :
                if my_user_letter.isalpha():
                    logger.info("L'utilisateur a entré une lettre")
                    return my_user_letter
            else:
                print("Il faut vraiment entrer une lettre ...")
                logger.info("L'utilisateur n'a pas entré une lettre'")

    #Initialisation d'une liste obtenue a partir du mot à chercher
    my_word_as_list=list(my_word)
    for i in range(len(my_word)):
        my_word_empty.append('_')

    #Affichage du mot vide et du pendu
    print(HANGMANPICS[0])
    for i in range(len(my_word)):
        print("_ ", end='')

    logger.info("le mot à trouver est:")
    logger.info(my_word)


        
    ###LE JEU : BOUCLE QUI TOURNE TANT QUE L'UTILISATEUR N'A PAS FAIT 5 ERREURS
    ### OU SI LE MOT N'A PAS ÉTÉ COMPLÈTEMENT TROUVÉ
    while (error_count < max_error) and (word_complete <1) :
        my_letter = test_true_letter()


        #Test pour savoir si la lettre de l'user est contenue dans le mot
        test_letter= test_letter_function(my_letter,my_word)

        #Si NON : on rajoute une erreur et on affiche le pendu
        if(test_letter==0):       
            error_count = error_count + 1
            print(my_letter, ": mauvais choix,  %s/%s erreurs" %(error_count,max_error))
            logger.info("Nombre d'erreurs actuel")
            logger.info(error_count)

        #Si OUI : on ajoute la lettre au mot vide
        elif(test_letter==1):
            for compteur in range (len(my_word)):
                if my_letter == my_word_as_list[compteur]:
                    my_word_empty[compteur] = my_word_as_list[compteur]
            logger.info(my_word_empty)
        
        #Test si le mot est complet
            word_complete = test_full_word(my_word_empty)
    
        #Affichage du mot a chercher en tant que chaine de caracteres
        my_word_empty_str=' '.join(map(str,my_word_empty))
        print(HANGMANPICS[error_count])
        print(my_word_empty_str)



    if error_count>= max_error:
        print("\nJeu perdu")
        logger.info("Jeu perdu")
        logger.info("nombre d'erreurs :")
        logger.info(error_count) 
        print("\nLe mot à trouver était :", my_word)  
    elif word_complete == 1 :
        print("\nJeu gagné")
        logger.info("Jeu gagné") 
        logger.info("mot initial :")   
        logger.info(my_word) 
        logger.info("mot trouvé :")  
        logger.info(my_word_empty_str)  
    logger.info("End log")