
"""Constantes"""
NB_ROWS = 6             #Nombres de lignes
NB_COLUNMS = 7          #Nombres de colonnes
NB_PLAYERS = 2          #Nombres de joueurs
VIDE = 0; ROUGE = 1; JAUNE = 2  #Code couleur
SYMBOL_COLOR = (" ", "X", "O")

"""Fonctions"""
def symbolCase(intColor):
    """
    Renvoie le caractère symbolisant la valeur d'une case
    :param intColor:
    :return:
    """
    return SYMBOL_COLOR[intColor]


def printNumberColunms():
    """
    affiche une ligne correspondant au bord supérieur ou inférieur
    en indiquant les numéros des colonnes
    :return:
    """
    for i in range(1, NB_COLUNMS+1):
        print(i, end=" ")
    print()
