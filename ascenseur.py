from etage import Etage

class Ascenseur:

    def __init__(self, etage_init: Etage, liste_etages):
        self.queue = []
        self.etage = liste_etages.index(etage_init)