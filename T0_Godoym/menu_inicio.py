
from funciones import partida

print("\n- - - - Bienvenid@ a Star Advanced  - - - - ")

def menu_inicio():
    print(
        "\n** Menú de Inicio **\n\n",
        "[1] Comenzar partida nueva\n",
        "[2] Cargar partida existente\n",
        "[3] Ranking de puntajes\n",
        "[4] Salir del programa"
        )
    input_inico = input()
    if input_inico == "1":
        partida()
        if True:
            print("Tamaño del tablero")
            input_tamañotab = input()
    elif input_inico == "2":
        pass        
    elif input_inico == "3":
        pass
    elif input_inico == "4":
        print("Salió exitosamente del programa")
    else:
        print("\nPor favor ingresa una de las opciones validas ")
        menu_inicio()




def menu_juego():
    print(
        "\n** Menú de Juego **\n\n",
        "[1] Descubrir un sector\n",
        "[2] Guardar la partida\n",
        "[3] Salir de la partida\n",
        "[4] Volver atrás"      
    )
    input_menu_juego = input()
    if input_menu_juego == "3":
        print(
            "\n[1] Guardar partida\n"
            "[2] No guardar partida\n"
        )
    elif input_menu_juego == "4":
        menu_inicio()