
#* TDD PRIMITIVOS EN PY: str, int, float, bool (True, False).
varibles = 20  #int
dato = 'Edily' #str
num = 12.12    #float
isAuth = True  #bool

#? print() 
# Metodo: imprimir en la terminal, el resultado de una operación, 
# el valor de una variable, o el dato pasado como argumento.
print(varibles, dato, num, 'str', isAuth, 12, 'Soy una cadena', False) 
# todos los parametros pasado como argumentos a este metodo se imprimen en la terminal

print('******************STR')
str_notmal  = 'Linea 1'
str_notmal_tabulado  = 'Linea 1-s \tLinea 2-s \tLinea3-s \n'
str_notmal_salto  = 'Linea 1-s \nLinea 2-s \nLinea3-s \n'

str_triple_1  = '''Linea 1 
linea 2 
Linea 3'''

str_triple_2  = """Linea 1 
linea 2 
Linea 3"""
print(str_notmal, str_triple_1, str_triple_2)  


print('******************METODO TYPE(VALOR)')
print(type(dato)) #<class 'str'>
print(type(False)) #<class 'bool'>
print(type(num)) #<class 'float'>

#* LOS TDD TIENEN METODOS ASOCIADOS 
# PARA STRINGS HAY METODOS PARA TRANSFORMAR EL TEXTO EN MAYUSCULAS, MINUSCULAS, ETC.
print(dato.upper()) #EDILY
print(round(num, 1)) #12.1

#* VARIABLES: o identificadores: Usa snake_case.
# Etiquetas con las que se ocupa espacios en memoria para guardar el valor asignado, representándolo.
#! Caracteres Prohibidos @, #, $, %, &, *, ( ), [ ], { }, +, =, empezar con numero, espacios.
# La declaracion NO requiere establecer su TDD, dado que PY NO es tipado. El interprete lo entenderá por el valor
#! $nombre = 'Carlo'
#* Reasignacion. 
# El valor y el TDD pueden cambiar a lo largo del programa, ya que PY es de tipado dinámico.
nombre = 'Teresa'
nombre = 'Teresa 2'

#*💡 CONSTANTES: PY NO tiene directiva que impida que un valor sea modificado una vez asignado. 
# Si las usas se recomienda usar mayusculas y guion bajo para identificarlas.
PI = 4.15
print(PI)
PI = 14.15
print(PI)

#* print('************************Metodos Casting***********************')
# #* Metodos Casting: para convertir entre TDD.
# Permiten convertir un valor de un TDD a otro TDD compatible.
precio_str = "2020" #TDD str
precio_num = 2020.01 #TDD float

precio_str_a_int = int(precio_str)

precio_str = int(precio_str)

int(precio_str)
int(precio_num) 

print(type(int(precio_str)), type(int(precio_num)) ) #2020 2020
print(type(int(precio_str)), type(int(precio_num)) ) # <class 'int'> <class 'int'>
print(type(precio_str)) # <class 'str'>

print(type(str(12))) #<class 'str'>

int_a_bool = 20
print(bool(0)) #F
print(bool(1)) #T
print(bool([])) #F
print(bool(['H'])) #T
print(bool(int_a_bool)) #T


print(float('100.03'))
#! print(int('100.09'))
#! print(int('22.22'))
# * print(int('100'))
# * print(int(100.07))

#* USO DE CASTING PARA CONCATENAR, Y CREAR STRINGS
#!print(' "h" + 3 ', 'h'+3)
#!print(' "3" + 3 ', '3'+3)
print(' "3" + 3 = ', int('3')+3)
print(' "3" + "3" = ','3'+ '3') #CONCATENACION
print(' "3" * 3 = ','3' *3)     #333


#********** OP ARITMETICAS **********
print('*'*10, 'OP ARITMETICAS', '*'*10,) 

#********** SIMBOLO SUMA **********
saludo = 'hola, soy '
nombre  = 'Carla y tengo '
edad = 20
saludo_compelto = saludo + nombre + str(edad) 

print(saludo_compelto) 
print(f'{saludo}{nombre}{edad}') #* Interpolacion  != concatenacion (str)

#* USO DEL CASTING PARA REALIZAR OPERACIONES ARITMÉTICAS


#***************************Generalidades de los numbers: pueden ser:
# Positivos o negativos 
# Expresados en potencia con el carácter "e"
# Son operandos en operaciones (aritmético y comparacion).
# Operando: valor o variable. Ej: 44, 44.44, 4.8e3, ...
# Operador: símbolo o palabra que realiza una operación sobre uno o más operandos. Ej: +, _, *, /, >=, ...
 
# ************************* OPERACIONES ARITMÉTICAS CON NÚMEROS 🧮📱
# ? OPERACIONES ARITMÉTICAS: se realizan SOLO entre int y float
# Suma: +, Resta: -,  Multiplicación: *,  División: / (resultado float) 
#* División entera: // (resultado int) 
# Módulo (residuo): % y Potencia: **
print(5+5)
print(5.07+5)
print(5.07-5)
print(5.07*5)
print(5**2) #Pot
print(5*True) # = 1
print(5*0) # = 1
print(3/2)      #1.5
print(3//2)     # 1
print(3.0//2)  #1.0
#? ⚠️Operador de la división entera "//", depende del tipo de dato del dividendo.

# ************************* 🔎OPERACION ARITMÉTICA: EL MODULO
# Devuelve el residuo de la división entre dos números.
# Se expresa como: 10 modulo 4 → dividendo modulo divisor → 10 % 4
print(10 % 4) # 2
print(10 % 5) # 0
print(3 % 4)  # 3
print(5 % 10)  # 5
num = input('Ingrese la log: ')
print(num)

# ************************* OPERACIONES "ARITMÉTICAS" CON STRINGS
#? concatenacion: entre STRINGS con operador '+' 
contatenacion = 'Hola ' + 'Edily'
print(contatenacion)
#? multiplicacion de los strings: str '*' int

print('Para JAROD', 'h' * 20)

#! El resto de operaciones aritmeticas entre str e int/float son IMPOSIBLES
#💡Haz casting para realizar operaciones, sean aritmeticas o concatenacion


#?*************************Notación Científica “E” o notación exponencial. 
# Es una forma de expresar números muy grandes o muy pequeños de manera abreviada, 
# usando un coeficiente (generalmente entre 1 y 10) multiplicado por una potencia de base 10.
# Coeficiente = 3.7
# Base = 10
# Exponente = 4 → E || e
#? Ejemplos: 3.5 × 10^4 = 35000

# Significado: El exponente (positivo o negativo) indica cuántas posiciones se debe desplazar la coma decimal 
# del coeficiente para obtener el número original.

#? E || e El valor se guardará como TDD float.

#? ➕E Positiva: El punto se mueve los dígitos E a la derecha y agregas 0 si es necesario.
peso = 2.5e3 # → 2.5 * 10 ^ 3
print(peso) #2500.0
print( 2.5 * (10 ** 3)) #2500.0

#? ➖E Negativa: El punto se mueve los dígitos E a la izquierda y agregas 0 si es necesario.
peso = 2.5E-3 # → 2.5 * 10 ^ 3
print(peso) # 0.0025
print( 2.5 * (10 ** -3)) # 0.0025
print( 2.5 * (10 ** - 3)) # 0.0025
#TODO:  QUE OPERACION HACE! print( 2.5 * (10 ^ -3)) # -22.5


#******************** Propiedades de las Potencias
# base con exponente positivo, se multiplica por sí mismo tantas veces como indique el exponente.
print('2**3 = ', 2**3)  # → 2 * 2 * 2
#? REGLA: cualquier base con exponente 0, el resultado es 1
print('2**0 = ', 2**0)  # 1
#? REGLA: base 0 con exponente cualquier, el resultado es 0
print('0**3 = ', 0**3)  # 0

#*EXCEPCION:💡 base y exponente es 0, es una indeterminacion matematica, pero en contextos discretos como  
# álgebra o programación se define convencionalmente como 1 
print('0**0 = ', 0**0)  # 1

#? El exponente negativo indica el inverso multiplicativo de la base elevada al exponente positivo. 
print('2**-3 = ', 2**-3) # 2 (2/1) ^-3 → 1/(2**3) →  1/8 → 0.125

print('(1/3)**-2 = ', (1/3)**-2) #  3/1 = 3; 3**2 → 3 * 3

#* ejemplo con notacion cientifica
print('ejemplo con notacion cientifica')
print(3.5e-3)             #0.0035
print(3.5 * (1/(10 **3))) #0.0035

#? La base negativa con exponente PAR da como resultado un número positivo
print('(-2)**2 = ', (-2)**2)  #4

#? La base negativa con exponente IMPAR da como resultado un número negativo 
print('(-2)**3 = ', (-2)**3) #-8 

#TODO: OPERADORES DE ASIGNACION COMPUESTA EN PY
