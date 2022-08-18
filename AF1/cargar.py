# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,categoria,tiempo_preparacion,precio,ingrediente_1,...,ingrediente_n
def cargar_platos(ruta_archivo: str) -> list:
    with open(ruta_archivo, 'rt') as archivo:
        lineas = archivo.readlines()
    
        lineas
        print(lineas)
    for linea in lineas:
        lineas.strip(",")

    platos = []



# --- EXPLICACION --- #
# los datos vienen en este orden el el .csv:
# nombre,cantidad
def cargar_ingredientes(ruta_archivo: str) -> dict:
    pass

#with open("platos.csv", "r") as f:
    #print(f.readlines())
#cargar_platos("platos.csv")

cargar_platos("platos.csv")