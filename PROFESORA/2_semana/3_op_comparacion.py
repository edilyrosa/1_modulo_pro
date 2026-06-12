
# ***************Los operadores de Comparación en Python: ==, !=, <, >, <=, >=
# permiten "comparar dos" valores o expresiones y devuelven un bool.
# Usados para tomar decisiones en un programa, como estructuras condicionales (if, while, etc.).
# 💡Ejemplo: que hago si edad ingesada de usuario es menor de 18 años?

#*************⁉️¿Con tipo de dato numéricos?
# Es intuitivo, comparan sus valores numéricos naturalmente.
print(4 == 4.0) # T
print(4 >= 4.0) # T
print(4 > 4.0)  # F
print(4 > 3)  # T
print(4 < 3)  # F
print(4 != 3)  # T 
print(5 != 5.0)  # F

#*************⁉️¿Con tipo de dato Bool?
# Se tratan como 1 (True) y 0 (False).
print('Con tipo de dato Bool')
print(True == 1) # T
print(True > 1) # F
print(True >= 1) # T
print(False >= 1) # F


# *************⁉️💡¿Con tipo de dato String?
# ✅Se comparan lexicográficamente según el orden Unicode de cada carácter.
# Python compara cadenas carácter a carácter, cada caracter tiene un codigo numerico. 
print('\nCon tipo de dato String')
print('hola' == 'Hola') # F
print('hola' != 'Hola') # V
print('num de la "H"', ord('H')) #72
print('num de la "h"', ord('h')) #104
print('H' < 'h') # 72 < 104
print(72 < 104) # 72 < 104

print()
print(72 == 'H') # False
print(72 == ord('H')) # T
print(type(ord('H'))) #<class 'int'>
#* Python compara carácter a carácter:
# usando el valor numérico Unicode de cada carácter (obtenible con ord(caracter)).
 
#*✅ La comparación se realiza en orden: 
# se compara el primer carácter de ambas cadenas; si son iguales, se pasa al siguiente, 
# y así sucesivamente, hasta encontrar la diferencia que devuelva el booleano resultado.

#* ✅Puedes usar los operadores de comparacion "entre dos cadenas".
#! 🚫No mezcles tipos diferentes, como str con int en comparaciones directas, porque no son compatibles, 
# si lo intentas usando operadores de orden (<, >, etc.), Python lanzará un TypeError. 
#!print("3" < 3)   #* TypeError: '<' not supported between instances of 'str' and 'int'
# Sin embargo, == y != sí pueden comparar distintos tipos siempre, 
# print("3" == 3)  # False  
# Lo anterior retorna casi siempre False, (excepto casos especiales).

#* ®️💡Resumen clave
# 👀Los operadores de comparación devuelven True o False.
# 👀Debes comparar preferentemente valores del mismo tipo para evitar errores.
# 👀Para cadenas, la comparación es lexicográfica, sensible a mayúsculas y minúsculas.
# 👀En tipos numéricos, se comportan naturalmente según valor.
# 👀== y != pueden comparar distintos tipos pero otros operadores NO.