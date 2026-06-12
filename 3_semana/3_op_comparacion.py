
# ***************Los operadores de Comparación en Python: ==, !=, <, >, <=, >=
# permiten "comparar dos" valores o expresiones y devuelven un bool.
# Usados para tomar decisiones en un programa, como estructuras condicionales (if, while, etc.).
# 💡Ejemplo: que hago si edad ingesada de usuario es menor de 18 años?

#*************⁉️¿Con tipo de dato numéricos?
# Es intuitivo, comparan sus valores numéricos naturalmente.
print(4 == 4.0) # T
print(4 != 4.0) # F
print(4 >= 4.0) # T
print(4 > 4.0) # F
print(6 > 10) # F
print(6< 10) # T

#*************⁉️¿Con tipo de dato Bool?
# Se tratan como 1 (True) y 0 (False).
print('\nCon tipo de dato Bool')
print(True == 1 ) # T
print(False == 0 ) # T
print(False < True ) # T


# *************⁉️💡¿Con tipo de dato String?
# ✅Se comparan lexicográficamente según el orden Unicode de cada carácter.
# Python compara cadenas carácter a carácter, cada caracter tiene un codigo numerico. 
print('\nCon tipo de dato String')
print('Hola' == 'hola') #F
print('hola' == 'hola') #T
print(ord('h'), ord('H'), ord('+')) #104 72 43 metodo ord('caractter') return TDD int
print(type(ord('h'))) # <class int>
print( ord('h') == 104) # T
print( ord('h') > ord('H')) # T

# METODO INPUT, OBTIENE DATA DE USUARIO DESDE LA TERMNAL, RETORNA TDD STR EL DATO Q USUARIO ESCRIBA POR TERMINAL
# edad = input('Ingrese su edad: ')
edad = int(input('Ingrese su edad: '))
print(type(edad)) #<class int> 
print(f'La edad el ususario es {edad} y en el anio que vi tendr {edad + 1}') #INTERPOLACION " STR {VARIABLES} "



#* Python compara carácter a carácter:
# usando el valor numérico Unicode de cada carácter (obtenible con ord(caracter)).


#*✅ La comparación se realiza en orden: 
# se compara el primer carácter de ambas cadenas; si son iguales, se pasa al siguiente, 
# y así sucesivamente, hasta encontrar la diferencia que devuelva el booleano resultado.

#* ✅Puedes usar los operadores de comparacion "entre dos cadenas".
#! 🚫No mezcles tipos diferentes, como str con int en comparaciones directas, porque no son compatibles, 
# si lo intentas usando operadores de orden (<, >, etc.), Python lanzará un TypeError. 


#* ®️💡Resumen clave
# 👀Los operadores de comparación devuelven True o False.
# 👀Debes comparar preferentemente valores del mismo tipo para evitar errores.
# 👀Para cadenas, la comparación es lexicográfica, sensible a mayúsculas y minúsculas.
# 👀En tipos numéricos, se comportan naturalmente según valor.
# 👀== y != pueden comparar distintos tipos pero otros operadores NO.