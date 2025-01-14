# classes/avion.py
from .vehicule import Vehicule

class Avion(Vehicule):
    def __init__(self, nbPortes, nbRoues):
        super().__init__(nbPortes, nbRoues)

    def demarrer(self):
        print("L'avion démarre lentement...")

    def avancer(self):
        print("L'avion avance comme un escargot...")

    def reculer(self):
        print("L'avion recule et se prend un poteau !")
