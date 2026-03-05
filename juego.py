import random

# Use gpt chat to understand and implement colorama
from colorama import Fore, init

# line that initializes colorama
init(autoreset=True)

class Buscaminas:

    def __init__(self, nombre, tam, minas):
        self.nombre = nombre
        self.tam = tam
        self.cantidad_minas = minas
        self.minas = []
        self.visitadas = []
        self.x = 0
        self.y = 0
        self.puntos = 0
        self.movimientos = 0
        self.generar_minas()

    # generate random mines
    def generar_minas(self):
        while len(self.minas) < self.cantidad_minas:

            i = random.randint(0, self.tam - 1)
            j = random.randint(0, self.tam - 1)

            if (i, j) != (0, 0) and (i, j) != (self.tam - 1, self.tam - 1):
                if (i, j) not in self.minas:
                    self.minas.append((i, j))