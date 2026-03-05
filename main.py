def get_player_name():
    """Prompts the user to enter their name for the game.

    Returns:
        str: The name of the player."""
    print("=== BUSCA MINAS ===")
    name = input("Jugador: ")
    return name


def get_difficulty_level():
    """Displays a menu for the user to select the game difficulty.
    Validates the input and returns the corresponding board size and mine count.

    Returns:
        tuple: (board_size, total_mines)"""
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
            print("Elección inválida. Por favor seleccione 1, 2 o 3.")

from juego import Buscaminas
#gemini is used to correct errorrs.

def main():
    """Main execution function. Captures initial data to start the game."""
    # 1. Capture player name
    player_name = get_player_name()
    print(f"\n¡Bienvenido, {player_name}! Empecemos a jugar.")

    # 2. Capture difficulty level (dimensions and mines)
    board_size, total_mines = get_difficulty_level()
    print(f"\nIniciando juego con un tablero de {board_size}x{board_size} y {total_mines} minas.")
    #gemini was used to help with the code.

    juego = Buscaminas(player_name,board_size, total_mines)


if __name__ == "__main__":
    main()