import random
from colorama import Fore, init

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

    # count nearby mines (with bounds validation)
    def minas_cercanas(self):

        contador = 0

        for i in range(self.x - 1, self.x + 2):
            for j in range(self.y - 1, self.y + 2):

                if 0 <= i < self.tam and 0 <= j < self.tam:
                    if (i, j) in self.minas:
                        contador += 1

        return contador

    # display board correctly as a square
    def mostrar(self):

        print("\n" * 3)

        for i in range(self.tam):
            for j in range(self.tam):

                if (i, j) == (self.x, self.y):
                    print(Fore.GREEN + " X ", end="")

                elif (i, j) in self.visitadas:
                    print(Fore.YELLOW + " * ", end="")

                else:
                    print(" . ", end="")

            print()  # line break for square format

        print("\nMinas cercanas:", self.minas_cercanas())
        print("Puntos:", self.puntos)

    # move player
    def mover(self, dx, dy):

        nx = self.x + dx
        ny = self.y + dy

        if 0 <= nx < self.tam and 0 <= ny < self.tam:

            self.movimientos += 1

            if (nx, ny) in self.visitadas:
                self.puntos -= 15
            else:
                self.puntos += 100
                self.visitadas.append((self.x, self.y))

            self.x = nx
            self.y = ny

            if (self.x, self.y) in self.minas:
                print(Fore.RED + "BOOM! Una mina.")
                return "mina"

            if (self.x, self.y) == (self.tam - 1, self.tam - 1):
                return "fin"

        return "seguir"

    # calculate average
    def promedio(self):

        if self.movimientos == 0:
            return 0

        if (self.x, self.y) in self.minas:
            return 0

        return self.puntos / self.movimientos