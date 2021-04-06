from player import *

"""Constantes"""
NB_ROWS = 6             #Nombres de lignes
NB_COLUNMS = 7          #Nombres de colonnes
NB_PLAYERS = 2          #Nombres de joueurs
VIDE = 0; ROUGE = 1; JAUNE = 2

class game:
    """Définitions des composants de jeu"""
    def __init__(self, playerName1, playerName2):
        """
        Initialise la grille de jeu et les joueurs
        :param playerName1: str (si vide, c'est l'ordinateur)
        :param playerName2: str (si vide, c'est l'ordinateur)
        """
        self.grille = []
        for ligne in range(NB_ROWS+2):
            self.grille.append(list((NB_ROWS+2)*[0]))
