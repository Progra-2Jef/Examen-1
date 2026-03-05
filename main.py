from juego import Buscaminas
from ranking import Ranking


def get_player_name():
    print("=== BUSCA MINAS ===")
    name = input("Jugador: ")
    return name


def get_difficulty_level():

    while True:
        print("\n=== SELECCIONE DIFICULTAD ===")
        print("1- Principiantes (08x08 celdas, 12 minas)")
        print("2- Intermedio (10x10 celdas, 20 minas)")
        print("3- Experto (12x12 celdas, 30 minas)")

        choice = input("Ingrese su elección (1/2/3): ")

        if choice == '1':
            return (8, 12)
        elif choice == '2':
            return (10, 20)
        elif choice == '3':
            return (12, 30)
        else:
            print("Elección inválida.")


def main():

    ranking = Ranking()

    player_name = get_player_name()
    board_size, total_mines = get_difficulty_level()

    juego = Buscaminas(player_name, board_size, total_mines)

    estado = "seguir"

    while estado == "seguir":

        juego.mostrar()

        print("\nMovimientos:")
        print("W = Arriba")
        print("S = Abajo")
        print("A = Izquierda")
        print("D = Derecha")

        tecla = input("Movimiento: ").lower()

        if tecla == "w":
            estado = juego.mover(-1, 0)
        elif tecla == "s":
            estado = juego.mover(1, 0)
        elif tecla == "a":
            estado = juego.mover(0, -1)
        elif tecla == "d":
            estado = juego.mover(0, 1)
        else:
            print("Movimiento inválido")

    juego.mostrar()

    if estado == "mina":
        print("\nPerdiste el juego.")
    elif estado == "fin":
        print("\n¡Ganaste!")

    prom = juego.promedio()
    print("Promedio final:", prom)

    ranking.agregar(player_name, prom, board_size)
    ranking.mostrar()


if _name_ == "_main_":
    main()