# Memory-mini-game
mini game aobut the original Memory game (cards pairs)

Juego de Memoria en Python - Explicación por Partes
1. Importación de módulos
python
Copy
import random
import os
import time
Explicación: Importamos los módulos necesarios:

random para mezclar las cartas

os para limpiar la pantalla

time para pausas entre jugadas

2. Función crear_tablero()
python
Copy
def crear_tablero(tamanio=4):
    """Crea un tablero de memoria con pares de números"""
    if tamanio % 2 != 0:
        tamanio += 1  # Asegurar que sea par
    
    total_pares = (tamanio * tamanio) // 2
    valores = list(range(1, total_pares + 1)) * 2
    random.shuffle(valores)
    
    tablero = []
    for i in range(tamanio):
        fila = valores[i*tamanio : (i+1)*tamanio]
        tablero.append(fila)
    
    return tablero
Explicación:

Crea una matriz cuadrada (tablero) con pares de números

Asegura que el tamaño sea par (si no lo es, lo incrementa en 1)

Genera valores duplicados, los mezcla y distribuye en el tablero

Retorna el tablero listo para jugar

3. Función mostrar_tablero()
python
Copy
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
Explicación:

Limpia la pantalla y muestra el tablero actualizado

Muestra índices de columnas (0, 1, 2...) en la primera fila

Para cada celda:

Muestra el número si la carta está revelada o emparejada

Muestra # si la carta está oculta

Formatea la salida para alinear correctamente los números

4. Función principal jugar_memory()
python
Copy
def jugar_memory():
    """Función principal del juego"""
    tamanio = 4  # Tamaño del tablero (4x4)
    tablero = crear_tablero(tamanio)
    reveladas = []  # Cartas temporalmente reveladas
    pares_encontrados = set()  # Pares ya encontrados
    intentos = 0
Explicación (parte inicial):

Inicializa el juego con:

Tamaño del tablero (4x4 por defecto)

Tablero con cartas mezcladas

Lista para cartas reveladas temporalmente

Conjunto para pares encontrados

Contador de intentos

5. Bucle principal del juego
python
Copy
    while len(pares_encontrados) < tamanio * tamanio:
        mostrar_tablero(tablero, reveladas, pares_encontrados)
        print(f"\nIntentos: {intentos}")
        print("Elige una carta (fila,columna): ")
        
        try:
            entrada = input("> ").strip().split(',')
            fila, col = int(entrada[0]), int(entrada[1])
Explicación:

El juego continúa hasta encontrar todos los pares

Muestra el tablero actual y pide coordenadas al jugador

Convierte la entrada (ej: "1,2") en coordenadas numéricas

6. Validación de jugadas
python
Copy
            if (fila, col) in pares_encontrados or (fila, col) in reveladas:
                print("¡Esa carta ya está revelada!")
                time.sleep(1)
                continue
                
            reveladas.append((fila, col))
Explicación:

Verifica si la carta ya está revelada o emparejada

Si es válida, añade la carta a las reveladas temporalmente

7. Lógica de comparación de cartas
python
Copy
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
Explicación:

Cuando se seleccionan 2 cartas:

Incrementa el contador de intentos

Compara los valores de las cartas

Si coinciden, las marca como pares encontrados

Si no, las vuelve a ocultar

Limpia la lista de cartas reveladas

8. Manejo de errores
python
Copy
        except (ValueError, IndexError):
            print("Entrada inválida. Usa formato: fila,columna (ej: 1,2)")
            time.sleep(1)
            continue
Explicación:

Captura errores de entrada inválida

Muestra mensaje de error y continúa el juego

9. Final del juego
python
Copy
    mostrar_tablero(tablero, [], pares_encontrados)  # Mostrar todo al final
    print(f"\n¡Felicidades! Completaste el juego en {intentos} intentos.")
Explicación:

Muestra el tablero completo al ganar

Muestra mensaje de felicitación con el número de intentos

10. Inicio del juego
python
Copy
if __name__ == "__main__":
    jugar_memory()
Explicación:

Punto de entrada del programa

Llama a la función principal cuando se ejecuta el script

Puedes copiar y pegar cada sección en tu archivo Python, y ejecutarlo cuando tengas todas las partes. Te sugiero que:

Empieces con las importaciones y la función crear_tablero()

Luego añadas mostrar_tablero()

Finalmente implementes la función principal jugar_memory()

Puedes modificar:

El tamaño del tablero (cambiando tamanio)

Los símbolos usados para cartas ocultas (cambiando #)

Los tiempos de espera (ajustando los time.sleep())

