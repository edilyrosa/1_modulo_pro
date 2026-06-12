
#? ⭐ Bucles anidados (loops dentro de loops): para recorrer matrices y acceder a cada elemento.
# Una matriz es una lista de listas
# Cada ele de la lista principal es una FILA de la matriz (una lista). = 'i'
# Cada ele dentro de una fila es un valor en una COLUMNA. = 'j'
# matriz = [
#     [0, 1, 1],  # fila 0
#     [1, 0, 1],  # fila 1
#     [1, 1, 0]   # fila 2
# ]

# El bucle externo itera sobre las filas (i es el índice de fila).
# El bucle interno itera sobre las columnas (j es el índice de columna), elemento por elemento.

#& 🤸🏻 Ejemplo para imprimir cada elemento con su posición:



#? EXPLICACION DE RANGE → range(start, stop, step)
# range recive por parametro un escalar y retorna una serie de iterables, para ser recorridos.
# Su llamado NO crea una variable que guarda esa serie.
# Argumentos:
# start (opcional): entero donde comienza la secuencia. Por defecto = 0.
# stop (requerido si solo pasas un argumento): entero que marca el tope exclusivo (no se incluye).
# step (opcional): entero que indica el salto entre valores. 
# Por defecto = 1. Puede ser negativo para contar hacia atrás. No puede ser 0 (lanza ValueError).
#& Ejemplos prácticos 🔢



#TODO: ⛹🏽⛹🏽 ALUMNOS REALICEN EL SIGUIENTE EJERCICIO
# Imprime La diagonal principal de una matriz cuadrada.
# La diagonal principal son los elementos donde el índice de fila es 
# igual al índice de columna, es decir, donde i == j, 
# recuerda que la sabes usar condicionales.
matriz = [
    [0, 1, 1], # fila 0
    [1, 0, 1], # fila 1
    [1, 1, 0]  # fila 2
]




# TODO: Ahora que sabemos recorer iterables podemos podemos aprender mas sobre ellos
#? Explicacion ir a: 5_iterables_avanzados.py
