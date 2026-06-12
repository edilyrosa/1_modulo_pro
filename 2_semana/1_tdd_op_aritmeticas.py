
#* TIPOS DE DATOS DE PY: PRIMITIVOS
# Todo dato tiene debe ser asignado (=) o usado

edad = 20               # int
edad_actual = '21'      # str
nombre = 'Edily'        # str
saldo = 12.12           # float
mujer = True            # bool
casada  = False         # bool
peso = 78               # int
# luego los puedo llamar a tra de su identificados o variable: para modificarlos o usarlos 

#? cuandos anos tendra "Edily" dento de 10 anos mas?
#! edad_en_10_anios_se_puede = edad_actual + 10 → esto dio error porque los TDD son diferentes, cuando usas "+", debes saber que quieres hacer : concatennar o sumar 
edad_en_10_anios_se_puede = int(edad_actual) + 10

print('CUANTO DIO: ', edad_en_10_anios_se_puede) #→ si espera mas de 1 parametro debes separarlos con ','

edad_en_10_anios = str(edad+10) # int → str
quien_es_edily = nombre + ' tendra '+ edad_en_10_anios +  ' anios ' + ' en 10 anios ' + ' y pesa actualmente ' + '78 Kg.'
contatenacion_num = int('10') + int("10") # str → int NO SERA UNA SUMA MATH SERA UNA CONTANETRACION  → 1010; 20


#Metodo print() imprime en la terminar los datos o variables que deseas visualizar.
# los metodos tiene (), y pueden o no esperar parametros, si le pasas parametros debes separalos con ","
print(nombre, 'tendra ', edad_en_10_anios,  'anios', 'en 10 anios', 'y pesa actualmente ', '78 Kg') 
print(nombre, 'tendra ', edad_en_10_anios,  'anios', 'en 10 anios', 'y pesa actualmente ', peso, 'Kg') 


#? el simb de "+" en py es para: sumar (numeros (TDD: int, float, 👀bool (0, 1))) o contatenar (para TDD str)
print('que pasara')
print(quien_es_edily)
print(contatenacion_num)

#* CASTINGS
print('*********************CASTINGS********************')
print('casting a str()')
numero = 10 # → Es un int q deberias convertir o castear a  "str" porque hareas una concatenacion. E.g: 'Mi nono tiene numero'
print(type(numero)) # <class 'int'> 
numero_str = str(numero) #→ los medotos casting (int(), str(), bool(), float()...) retornan el dado ya caseado, entonces puedo gurdar el casting en una cariable para usarla despues
print(type(numero_str)) # <class 'str'> 
mensaje  = 'Mi nino tiene '+ numero_str
print(type(mensaje)) # <class 'str'> 
print(mensaje)
#? str == string == texto → debe estar entrecomillado.


print('casting a bool()')
numero_cero = 0 # TDD int → false
numero_uno = 1  # TDD int → true
print(numero_cero) # 0
print(bool(numero_cero)) # False
print(bool(numero_uno)) # True
print(bool(1)) # True
# 0 → Flase
# 1 → True

# Falsy= 0, [], {}, '', None
# Truely= 1, [1, 3], {'key': 'value'}, 'h'
print('Falsy y truely')
print(bool([1, 3])) #T
print(bool([]))     #F
print(bool(0))      #F
print(bool(20))     #T
print(bool(''))     #F
print(bool({'key': 'value'}))     #T
print(bool({}))     #F
print(bool('Edily'))     #T

# llamo a una BBDD = data → ✅[{}, {}, ...]
# llamo a una BBDD = data → ❌[] || {}

# data = fetch(url)

# if data == False:
#     print('❌No llego data')
# else:
#     print('la data es ... 💃🏻', data[0]["username"]) # → "Bret",


print('casting a float()')
#? CON LOS TDD NUMERICOS (int, float) haces operaciones aritmeticas (+, -, *, **, %, /, //)
peso = '60.60' # str → TDD Numerico: 
peso_2 = 60.60 # float
# peso_3 = 60,60 # tuple #?LOS FLOAT O DECIMALES ✅USAN EL '.' ❌NOOOOOOOOOOOO LA ","
print(type(peso)) # <class "str">
print(type(peso_2)) # <class "float">
# print(type(peso_3)) # <class "tuple">


peso_a_rebajar = 10.12 #float
# peso_ideal = peso - peso_a_rebajar #!TypeError: unsupported operand type(s) for -: 'str' and 'float'

peso_ideal = float(peso) - peso_a_rebajar #!TypeError: unsupported operand type(s) for -: 'str' and 'float'
print(peso_ideal) # 50.480000000000004

print(float(10)) # int a float → 10.0
print(float("10")) # str de int a float → 10.0
print(float("10.20")) # str de float a float → 10.20

#? Regla de int()
# para que el convertidor int() funcione le pasas como parametro:
# ✅un dato str ENTERO o un 
# ✅float-float
# ❌pero NOOOOOOOOO le puedes pasar un srt-float
print(int("10")) # str a int → 10
# print(int("10.20")) # str de float a float → 10.20 #!ValueError: invalid literal for int() with base 10: '10.20'
que_soy = int(10.20) # float a int
print(que_soy) #10


print('*************************OPERACIONES ARITMETICAS****************************')
#? REGLA:
# las op aritmeticas (+, -, *, **, %, /, //) se realizan entre NUMEROOOOOOOOOOOOOOS (int y float), 
# en operaciones artmeticas los bool tienden a 0 y 1


# *******************SUMA, RESTA Y MULTI *********************
suma  =  10 + 120.232323
# suma  =  "10" + 120.232323 #!
print(suma) # 130.232323 → float
resta = suma - True # True == 1 en op aritmeticas
print(resta) # 129.232323
multi = resta * False
print(multi) # 0.0

# *******************POTENCIA *********************
#? REGLA POTENCIA-MATH: si la "base es 0" con cualquier exponente (que no sea 0) el resulta es 0
pow =  multi ** 3         # → 0^3 == 0
potencia_base_0 =  0 ** 5 # → 0^5 == 0
print(pow)                # 0.0
print(potencia_base_0)    # 0


# #? REGLA POTENCIA-MATH: si la base cualquier con "exponente 0", el resulta es 1
pow_2 = 3 ** pow # 1.0
pow_3 = 10 ** 0  # 1
print(pow_2)
print(pow_3)

# #? REGLA POTENCIA-MATH: si la base 0 con "exponente 0". En matematicas es un error, una indeterminacion matematica en programacion es == 1
print(0 ** 0) # 1


# *******************DIV *********************
# la div float con "/"
div = 10 / 5 
print(div) # 2.0

# la div int con "//"
div = 10 // 5 
print(div) # 2


# la div int con "//", si alguno de los datos es float, el resultado sera float aun usando el "//"
div = 10.0 // 5 

print(div) # 2.0 → float
print(int(div)) # 2 

#******************************** VARIABLES Y CONSTANTES
# # afecto el valor de la variable, con el simb del '=', yo puedo usar la variable sin afectar su balor, 
# SOLO SE AFECTA EL VALOR CUANDO LE ASIGNO O REASIGNO VALOR CON EL '='
nombre  = 'Edily'
nombre_completo = 'Edily Mora'
nombre_completo = nombre + 'Mora'
print(nombre) # 'Edily'

nombre_usuario  = 'Hanna' #Gana la ultimia declaracion !!🥇 #sk esto es cvn en PY
nombreUsuario  = 'Hanna' #Gana la ultimia declaracion !!🥇 # cammelcase esto es conv en JS
# peso = 100
# .....
# peso = 100 + 2.0
# peso = 'Maria'

print(nombre) # Hanna

#******** CONSTANTES EN PY
# las constantes en py no tienen una regulacion, pueden ser modificadas, 
# a diferencia de otros jeng de programacion. o sea si reasignas el valor de una constante
# no te dara error. Existe la conven de escribirlaqs en mayuscula para qye se entenda que NO DEBES
# MODIFICAR SU VALOR
PI = 3.14
PI = 3.15
print(PI)


#* VARIABLES: o identificadores: Usa snake_case.
# Etiquetas con las que se ocupa espacios en memoria para guardar el valor asignado, representándolo.
#! Caracteres Prohibidos @, #, $, %, &, *, ( ), [ ], { }, +, =, empezar con numero, espacios.
# La declaracion NO requiere establecer su TDD, dado que PY NO es tipado. El interprete lo entenderá por el valor

# @peso = 12.12
# #peso = 12.12
# (peso = 12.12
# peso@ = 12.12
# 23_Edily = 'edil'
if True:
    for e in [1,3,]:
        print('Todo bn', e)
# gl      
# if true{
#     local
# }
# else{
    
# }
# TODO METODOS SEGUN TIPOS DE DATOS: str.upper(), round(float, precision)
# int, str, bool, float
raro = -12
decimal = 3.14151617
# esto es un metodo que hace algo, imrpime en consola los datos que le pase separados por coma como parametros
print('hola', nombreUsuario, peso_ideal, False, raro) #TODOS ESTOS SON PARAMETEOS: 'hola', nombreUsuario, peso_ideal, False, raro
print('CAPITALIZANDO, ', 'hola'.upper(), 'HOLAAAAAAAAAAA EDILY'.lower(), decimal, round(decimal, 2), "\n\n\n")
# hay metodos para cada TIpo de Dato PTRIMITIVOS (int, str, bool, float) 
# los metodos pueden o no esperar matametros,
# los metodo spueden o no RETORNAN (return) datos
# los metodos son funciones

#TODO COMO DEFINIMOS STR

primer_nombre = 'Hanna'
primer_nombre = "Hanna"

# TODO ESCAPAR A LAS COMILLAS (\n, \t, )
linea1 = 'hola soy linea 1 \nhola soy linea 2' # \n es un salto de linea, si usas solo 1 comilla no puedes div en 2 o mas limineas, debes escribirlaqs secuencialmente 

linea2 = '''hola soy linea 3 
hola soy linea 4'''

linea3 = """hola soy linea 5 


hola soy linea 6
hola soy linea 7"""

texlizar = "la nina se llama 'Edily'"
#!texlizar = 'la nina se llama 'Edily' '
texlizar1 = 'la nina se llama "Edily" '

print("\n\n\n", linea1,"\n\n\n")
print(linea2)
print(linea3)
print(texlizar)
print(texlizar1)


print('ESTO ES UNA TABLA')
print('ID\t nombre\t\t edad\t')
print('1\t Edi\t\t 30\t')
print('2\t Hanna\t\t 22\t')



# TODO: LA OEPACION ART: MODULO
# Devuelve el residuo de la división entre dos números.
# Se expresa como: 10 modulo 4 → dividendo modulo divisor → 10 % 4
print('MODULOOOOOOOOOO', 10 % 4) # 2
print(10 % 5) # 0
print(5 % 10) # 5


# TODO LA MULTIPLICACION DE STR * INT
print('TODO LA MULTIPLICACION DE STR * INT')
#* +, -, *, **, //, / → Simb Aritmeticas int, float, bool (0, 1) pPARA HACER MATEMATICA.
print(10 // 5) #entera siempre q los 2 sean enteros o sea int
print(10.0 // 5) #*
print(10 / 5) #decimal

numero_entero = 15
print(type(numero_entero)) #<class int >
print("10" + str(numero_entero)) #*1015

#* int('15'), str(), bool() medotos de casting o convertidores de tipo de dato

#* LA MULTIPLICACION DE STR * INT
print('Edily '+ "5") #CONCATENACION
print('Edily '*5)
# print('Edily '*5.5) #!
# print('Edily '/5) #!
# print('Edily '-5) #!
# print('Edily '*5.5) #!



#TODO: Notación Científica “E” o notación exponencial. 
# Es una forma de expresar números muy grandes o muy pequeños de manera abreviada, 
# usando un coeficiente (generalmente entre 1 y 10) multiplicado por una potencia de base 10.
# Coeficiente = 3.7
# Base = 10
# Exponente = 4 → E || e
print('Notación Científica “E” o notación exponencial.')
print(3.7e4) # → 3.7 * 10^4 → 3.7 * 10000 = 37000
print(3.5E5) # → 3.7 * 10^4 → 3.7 * 10000 = 37000

# Significado: El exponente (positivo o negativo) indica cuántas posiciones se debe desplazar la coma decimal 
# del coeficiente para obtener el número original.

#? E || e El valor se guardará como TDD float.

#? ➕E Positiva: El punto se mueve los dígitos E a la derecha y agregas 0 si es necesario.
print(3.7e4) # → 3.7 * 10^4 → 3.7 * 10000 = 37000


#? ➖E Negativa: El punto se mueve los dígitos E a la izquierda y agregas 0 si es necesario.

print(3.7e-4) # 0.00037

#******************** Propiedades de las Potencias
# base con exponente positivo, se multiplica por sí mismo tantas veces como indique el exponente.
print('2**3 = ', 2**3)
#? REGLA: cualquier base con exponente 0, el resultado es 1
print('2**0 = ', 2**0)  
#? REGLA: base 0 con exponente cualquier, el resultado es 0
print('0**3 = ', 0**3)  
#*EXCEPCION:💡 base y exponente es 0, es una indeterminacion matematica, pero en contextos discretos como  
# álgebra o programación se define convencionalmente como 1 
print('0**0 = ', 0**0)  
#? El exponente negativo indica el inverso multiplicativo de la base elevada al exponente positivo. 
print('2**-3 = ', 2**-3) 
print('(1/3)**-2 = ', (1/3)**-2)

#* ejemplo con notacion cientifica
print('ejemplo con notacion cientifica')
print(3.5e-3)             #0.0035
# Coeficiente = 3.5
# Base = 10
# Exponente = -3 → E || e
#? Hazlo con una expresion math: 3.5 × 10^(-3) = Pero el exponente es negativo... que hacemos?


#? La base negativa con exponente PAR da como resultado un número positivo
print('(-2)**2 = ', (-2)**2)  #4

#? La base negativa con exponente IMPAR da como resultado un número negativo 
print('(-2)**3 = ', (-2)**3) #-8 

#TODO: OPERADORES DE ASIGNACION COMPUESTA EN PY
