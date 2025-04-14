import random
import os
import time

def crear_tablero(tamanio=4):
    """Crea un tablero con pares, por defecto de 4x4"""
    total_pares = (tamanio * tamanio) // 2
    valores = list(range(1, total_pares + 1)) * 2
    random.shuffle(valores)
    
    tablero = []
    for i in range(tamanio):
        fila = valores[i*tamanio : (i+1)*tamanio]
        tablero.append(fila)
    return tablero

def mostrar_tablero(tablero, reveladas, pares_encontrados):
    # Muestra el tablero en la terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    print("  " + " ".join(str(i+1).rjust(2) for i in range(len(tablero))))
    for i, fila in enumerate(tablero):
        linea = str(i+1) + " "
        for j, valor in enumerate(fila):
            pos = (i+1, j+1)
            if pos in pares_encontrados:
                linea += str(valor).rjust(2) + " "
            elif pos in reveladas:
                linea += str(valor).rjust(2) + " "
            else:
                linea += " #" + " "
        print(linea)

def obtener_coordenada(mensaje, maximo):
    # Obtiene una coordenada válida del usuario
    while True:
        try:
            valor = int(input(mensaje))
            if 1 <= valor <= maximo:
                return valor
            print(f"El valor debe estar entre 1 y {maximo}")
        except ValueError:
            print("Por favor ingresa un número válido")

def dificultad():
    tamanio = 0
    print("Bienvenido al juego de memoria")
    print("Encuentra los pares de cartas")
    try:
        menu = input("Elige dificultad: \n1 > fácil,\n2 > medio,\n3 > difícil\n").strip()
        
        if menu == '1':
            tamanio = 4
        elif menu == '2':
            tamanio = 6
        elif menu == '3':
            tamanio = 8
    except ValueError:
        print("Por favor ingresa un número válido")

    return tamanio
 
 
def jugar_memory(tamanio):
    # Función principal del juego
    
    tablero = crear_tablero(tamanio)
    reveladas = []  # Cartas temporalmente reveladas
    pares_encontrados = set()  # Pares ya encontrados
    intentos = 0
    
    while len(pares_encontrados) < tamanio * tamanio:
        mostrar_tablero(tablero, reveladas, pares_encontrados)
        print(f"\nIntentos: {intentos}")
        
        # Obtener primera carta
        if not reveladas:
            print("Elige la primera carta:")
            fila = obtener_coordenada("Fila (1-4): ", tamanio)
            col = obtener_coordenada("Columna (1-4): ", tamanio)
            
            pos = (fila, col)
            if pos in pares_encontrados:
                print("¡Esa carta ya fue encontrada!")
                time.sleep(1)
                continue
                
            reveladas.append(pos)
            continue
        
        # Obtener segunda carta
        print("Elige la segunda carta (fila,columna):")
        fila = obtener_coordenada("Fila (1-4): ", tamanio)
        col = obtener_coordenada("Columna (1-4): ", tamanio)
        
        pos = (fila, col)
        if pos in pares_encontrados:
            print("¡Esa carta ya fue encontrada!")
            time.sleep(1)
            continue
        if pos in reveladas:
            print("¡Esa carta ya está revelada!")
            time.sleep(1)
            continue
            
        reveladas.append(pos)
        intentos += 1
        
        # Mostrar ambas cartas
        mostrar_tablero(tablero, reveladas, pares_encontrados)
        time.sleep(1)
        
        # Verificar si matchean
        carta1 = tablero[reveladas[0][0]-1][reveladas[0][1]-1]
        carta2 = tablero[reveladas[1][0]-1][reveladas[1][1]-1]
        
        if carta1 == carta2:
            print("\n¡Encontraste un par!")
            pares_encontrados.add(reveladas[0])
            pares_encontrados.add(reveladas[1])
        else:
            print("\nNo coinciden, sigue intentando")
        
        reveladas = []
        time.sleep(1)
    
    mostrar_tablero(tablero, [], pares_encontrados)
    print(f"\n¡Felicidades! Completaste el juego en {intentos} intentos.")

if __name__ == "__main__":
    nivel = dificultad()
    jugar_memory(nivel)