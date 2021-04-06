
class player:
    """Définition d'un joueur"""

    def __init__(self, playerColor, playerName,):
        """
        Initialise un nouveau joueur avec les paramètres indiqués
        :param playerName: Nom du joueur
        :param playerColor: Couleur du joueur
        """
        self.name = str(playerName)
        self.color = int(playerColor)
        if self.name == "":
            self.isIA = 1
            self.name = "Ordinateur"
        else:
            self.isIA = 0
        self.nbVictoires = 0
