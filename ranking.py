class Ranking:

    def _init_(self):
        self.jugadores = []

    def agregar(self, nombre, promedio, tablero):

        if promedio == 0:
            return

        # verificar si ya existe
        for jugador in self.jugadores:
            if jugador["nombre"] == nombre:
                if promedio > jugador["promedio"]:
                    jugador["promedio"] = promedio
                    jugador["tablero"] = tablero
                return

        # si hay espacio
        if len(self.jugadores) < 3:
            self.jugadores.append({
                "nombre": nombre,
                "promedio": promedio,
                "tablero": tablero
            })
        else:
            menor = min(self.jugadores, key=lambda x: x["promedio"])

            if promedio > menor["promedio"]:
                self.jugadores.remove(menor)
                self.jugadores.append({
                    "nombre": nombre,
                    "promedio": promedio,
                    "tablero": tablero
                })

    def mostrar(self):

        print("\n" * 5)

        for i in range(self.tam):
            for j in range(self.tam):

                if (i, j) == (self.x, self.y):
                    print(Fore.GREEN + " X ", end="")

                elif (i, j) in self.visitadas:
                    print(Fore.YELLOW + " * ", end="")

                else:
                    print(" . ", end="")

            print()

        print("\nMinas cercanas:", self.minas_cercanas())
        print("Puntos:", self.puntos)