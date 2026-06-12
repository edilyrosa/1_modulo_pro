

# *************************** 1. LAS LISTAS: (array, vector, arreglo)
# son colecciones ordenadas de datos, el orden es secuencial y preciso.
# Cada dato coleccionado es un elemento.
# La lista puede contener cualquier tipo de dato, incluso otras listas.
# Al elemento se accede por su posición (índice, que comienza desde 0), para:
# Obtenerlo, establecerlo, Modificarlo y Eliminarlo, entonces las listas son mutables.
# Se sabe su tamaño con la función con len(my_list).
#! Acceder a una posición fuera de rango, genera un error.

#?⭐ Creación de una lista: Se representa, conteniendo a sus elementos entre corchetes []
lista_numeros = [1, 2, 3, 4, "5", False] # *hay 6 elementos en 5 post, pq contamos desde la pos 0
#& 💡Utilidad de las listas: 
# Entre otras utilidades, es la forma de empaquetar un conjunto de data relacionada para, 
# por ejemplo, transportarla de un sistema a otro: https://jsonplaceholder.typicode.com/users

 
#?⭐ Acceso: medidante su índice (posición)
print(lista_numeros)
print(lista_numeros[5]) #False
print(lista_numeros[-1]) #False
print(lista_numeros[4]) #'5'
print(lista_numeros[-2]) #'5'

#?⭐ Saber el TDD de las Listas
print(type(lista_numeros[-1])) # class bool
print(type(lista_numeros)) # class list

print(lista_numeros[-1] + 6) # 6
print(lista_numeros[0] + 6) # 7
#* TDD Primitivos
# 'False' → str
# False → bool
# 12 → int
# 12.33 → float
# 12,77


#?⭐ Modificación de un elemento
print(type(lista_numeros[4])) # '5' → str
lista_numeros[4] = 5 #✅ NO PARA LAS TUPLAS!!
print(type(lista_numeros[4])) # 5 → int

#?⭐ Longitud
print(len(lista_numeros)) # 6


#?⭐ Metodo append(ele)
lista_numeros.append(6) 
print(lista_numeros)#[1, 2, 3, 4, 5, False, 6]
# Este metodo agrega el elemento paratro al final de la lista.
lista_vacia = []
# !lista_vacia[0] = 'hola' #!IndexError: list assignment index out of range
lista_vacia.append('hola')
print(lista_vacia)

#! lista_vacia[0] = 'hola'  
# Esto ocurre porque la lista inicialmente no tiene elementos y no se puede asignar directamente a un índice inexistente.
# Para agregar elementos a una lista vacía debes usar métodos como:
# append() para añadir al final


#TODO: 🧠TAREA:Existen otros metodos de las listas, 
# te invito a que los investigues y pruebes. Los usaremos mas adelante.
"""
TABLA DE MÉTODOS IMPORTANTES DE LISTAS EN PYTHON
| Método    | Parámetros                         | Retorna                         | Descripción / Señal de uso                  |
|-----------|------------------------------------|---------------------------------|---------------------------------------------|
| append()  | obj (cualquier objeto)             | None (modifica lista in-place)  | Añade elemento al final: lista.append(x)    |
| pop()     | index=-1 (opcional, índice)        | Elemento removido               | Elimina y retorna elemento: lista.pop([i])  |
| remove()  | obj (elemento a eliminar)          | None (modifica lista in-place)  | Elimina primera ocurrencia: lista.remove(x) |
| sort()    | key=None, reverse=False (opc.)     | None (modifica lista in-place)  | Ordena lista: lista.sort() o sort(reverse)  |
| index()   | obj, start=0, end=len(lista) (opc.)| Índice de primera ocurrencia    | Busca posición: lista.index(x[,start,end])  |

Ejemplos rápidos:
>>> lista = [3, 1, 4]
>>> lista.append(2)      # [3, 1, 4, 2]
>>> lista.pop()          # Retorna el ele eliminado → 2, y la lista queda → [3,1,4]
>>> lista.sort()         # [1, 3, 4]
>>> lista.index(3)       # Retorna 1
"""
# *************************** 2. TUPLAS: (tuple)
# Son colecciones ordenadas de datos, el orden es secuencial y preciso.
# Cada dato coleccionado es un elemento.
# A diferencia de las listas, las tuplas son inmutables, no se pueden modificar, agregar o eliminar elementos.
# Se sabe su tamaño con la función con len(my_tuple).
#! Acceder a una posición fuera de rango, genera un error.

#?⭐ Creación de una tupla: Se representa, conteniendo a sus elementos entre paréntesis ()
tupla_num_par = (1, 2, 3, 4, "5", False)
tupla_num_sin_p = 1, 2, 3, 4, [1, 'Edily', False]
lista_1 = [1, 'Edily', False]
lista_a_tupla = tuple(lista_1) #* casting de lista a tupla

print( tupla_num_par)
print( tupla_num_sin_p)
print( lista_a_tupla)
#?⭐ Saber el TDD de las Tuplas
print(type(lista_a_tupla)) #class tuple


#?⭐ Acceso: meidante su índice (posición)
print( tupla_num_sin_p[4]) #[1, 'Edily', False]
print( type(tupla_num_sin_p[4])) # clss list

nuev_list = tupla_num_sin_p[4].append(True) 
print(tupla_num_sin_p[4]) #[1, 'Edily', False, True]

#! tupla_num_sin_p[4] = 'Hola' # TypeError: 'tuple' object does not support item assignment

print(tupla_num_sin_p)

#& 💡Utilidad de las tuplas: 
# Entre otras utilidades, es la forma de empaquetar un conjunto de data que por seguridad no deseamos que sea modificable.

#?⭐ ❌ NO podemos Modificar las tuplas
#! tupla_numeros[-2] = 5

#?⭐ Longitud

print(len(tupla_num_sin_p))

# *************************** METODOS CONSTRUCTORES: list(mi_iletable), tuple(mi_iterable). 
# Existen metodos constructores de listas y tuplas, cuyo parametro es el iterable a comvertir.
# 💡Utilidad: hacer casting de un tipo de dato a otro por sus caracteristicas. Ejemplo: recibes 
# una tupla pero necesitas una lista para modificar sus ele, entonces haces el casting. 
#? Ejemplo:
# list()
# tuple()
# int(), bool().....


# TODO: 3. OTROS TIPOS DE COLECCIONES ITERABLES
# Existen otros tipos de colecciones en Python que también son iterables (ademas de lista, tupla), como:
# cadena de texto, diccionario, conjunto. Los veremos luego.


# TODO: El recorrido de las listas y tuplas para: 
# mapearlas y filtrarlas o extraer sus elementos se realiza con ciclos. (5_iterables_avanzado.py)

