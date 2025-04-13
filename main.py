import random
import os
import time

def crear_tablero(tamanio=4):
    # Crea un tablero con pares, po defecto de 4x4

    total_pares = (tamanio * tamanio) // 2 # calculamos el total de pares
    valores = list(range(1, total_pares + 1)) * 2 # creamos y duplicamos los valores pares
    random.shuffle(valores) # mezclamos los valores para que aparezcan en orden aleatorio
    
    tablero = []
    for i in range(tamanio):
        fila = valores[i*tamanio : (i+1)*tamanio]
        # separar los valores en la fila y creamos una matriz en forma de tablero
        tablero.append(fila)
    return tablero

def mostrar_tablero(tablero, reveladas, pares_encontrados):
    """Muestra el tablero en la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("  " + " ".join(str(i).rjust(2) for i in range(len(tablero))))
    
    for i, fila in enumerate(tablero):
        linea = str(i) + " "
        for j, valor in enumerate(fila):
            if (i, j) in pares_encontrados:
                linea += str(valor).rjust(2) + " "
            elif (i, j) in reveladas:
                linea += str(valor).rjust(2) + " "
            else:
                linea += " #" + " "
        print(linea)

def jugar_memory():
    """Función principal del juego"""
    tamanio = 4  # Tamaño del tablero (4x4)
    tablero = crear_tablero(tamanio)
    reveladas = []  # Cartas temporalmente reveladas
    pares_encontrados = set()  # Pares ya encontrados
    intentos = 0
    
    while len(pares_encontrados) < tamanio * tamanio:
        mostrar_tablero(tablero, reveladas, pares_encontrados)
        print(f"\nIntentos: {intentos}")
        print("Elige una carta (fila,columna): ")
        
        try:
            entrada = input("> ").strip().split(',')
            fila, col = int(entrada[0]), int(entrada[1])
            
            if (fila, col) in pares_encontrados or (fila, col) in reveladas:
                print("¡Esa carta ya está revelada!")
                time.sleep(1)
                continue
                
            reveladas.append((fila, col))
            
            if len(reveladas) == 2:
                intentos += 1
                carta1 = tablero[reveladas[0][0]][reveladas[0][1]]
                carta2 = tablero[reveladas[1][0]][reveladas[1][1]]
                
                mostrar_tablero(tablero, reveladas, pares_encontrados)
                time.sleep(1)
                
                if carta1 == carta2:
                    pares_encontrados.add(reveladas[0])
                    pares_encontrados.add(reveladas[1])
                    print("\n¡Encontraste un par!")
                else:
                    print("\nNo coinciden, sigue intentando")
                
                reveladas = []
                time.sleep(1)
                
        except (ValueError, IndexError):
            print("Entrada inválida. Usa formato: fila,columna (ej: 1,2)")
            time.sleep(1)
            continue
    
    mostrar_tablero(tablero, [], pares_encontrados)  # Mostrar todo al final
    print(f"\n¡Felicidades! Completaste el juego en {intentos} intentos.")

if __name__ == "__main__":
    jugar_memory()