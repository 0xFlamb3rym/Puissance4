from player import *
from utils import *

class game:
    """Définitions des composants de jeu"""
    def __init__(self, playerName1, playerName2):
        """
        Initialise la grille de jeu et les joueurs
        :param playerName1: str (si vide, c'est l'ordinateur)
        :param playerName2: str (si vide, c'est l'ordinateur)
        """
        #1. grille de jeu
        self.grid = []
        for raw in range(NB_ROWS+2):
            self.grid.append(list((NB_COLUNMS+2)*[0]))
        #2. joueurs
        player1 = player(1, playerName1)
        player2 = player(2, playerName2)

        self.players = (player1, player2)


    def emptyGrid(self):
        """
        Vide la grille du jeu
        :return:
        """
        for i in range(NB_ROWS+2):
            for j in range(NB_COLUNMS+2):
                self.grid[i][j] = VIDE


    def printGrid(self):
        """
        Affiche la grille de jeu et son contenu
        :return:
        """
        print()
        #1. affiche le bord supérieur
        printNumberColunms()
        #2. affichage de la grille avec les bords gauche et droite
        for i in range(NB_ROWS, 0, -1):
            print(i, end=" ")
            for j in range(1,NB_COLUNMS+1):
                print(symbolCase(self.grid[i][j]), end=" ")
            print(i)
        #3. affichage du bord inférieur
        printNumberColunms()


    def isMovePossible(self, intColunms):
        """
        Test si la colonne spécifiée peut être jouée sinon renvoie @False
        :param intColunms:
        :return:
        """
        if intColunms < 1 or intColunms > NB_COLUNMS:
            return False
        else:
            return self.grid[NB_ROWS][intColunms] == VIDE