from parametros import PROB_BESTIA
from math import ceil
def partida():
    print(
        "\n** Tamaño del tablero **\n",
        " Debe estar en el intervalo [3,15]\n\n"
        " [1] Ancho"
        )
    input_tamanoX = input()
    if input_tamanoX.isdigit() == True:
        if  int(input_tamanoX) in range (3,16):
            x = int(input_tamanoX)
            print(
                "\n** Tamaño del tablero **\n\n",
                "[2] Largo"
            )
            input_tamanoY = input()
            if input_tamanoY.isdigit() == True:
                if  int(input_tamanoY) in range (3,16):
                    y = int(input_tamanoY)

                    N = ceil(x*y*float(PROB_BESTIA))
                    print(f"Cantidad de bestias es: {N}")

                else:
                    print("Por favor, ingresar un digito valido en el intervalo [3,15]")
                    partida()
            else:
                print("Por favor, ingresar un digito valido, no letras")
                partida()                    
        else:
            print("Por favor, ingresar un digito valido en el intervalo [3,15]")
            partida()

####### PONER LAS BESTIAS EN CANTIDAD 
### cada bestia debe ubicarse en un sector aleatorio del tablero
    else:
        print("Por favor, ingresar un digito valido, no letras")
        partida()
        




def ranking_puntajes():
    #puntaje = bestias tablero * casillas descubiertas * POND_PUNT
    pass

partida()