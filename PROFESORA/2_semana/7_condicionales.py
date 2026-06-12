
# #& 1. IF
# #Se ejecuta un bloque si la condición es verdadera.
# # Sintaxis: 
# # if condición lógica a evaluar :
# #   indentación →  código py a ejecutar
# #?Sentencia else
# # Se usa para definir qué sucede si la condición del if es falsa. 
# # Por eso NO LE SIGUE NINGUNA condición lógica a evaluar.  
# # Se Ejecuta si ninguna condición previa es verdadera.
# #? Ejercicio: Determine si un número es par o impar, 💡solo existen esas 2 posibilidades.
# # print('Veamos si un número es par o impar')
# # num = int(input('Ingrese el num a evaluar: ')) #*👀
# # if num % 2 == 0:
# #     print(f'{num} es PAR')
# # else:   
# #     print(f'{num} es INPAR')
    
    

    
# #& 2. ELIF
# # Es la forma de intercalar múltiples condiciones a una sentencia if-else. 
# #? Ejercicio: catalogue a un estudiante según su calificación, 
# # con rangos de {
# # +90,  -> # Excelente 🥳
# # +80,  -> # Muy bien 👏
# # +70,  -> # Bien 👍
# # +60,  -> # Suficiente 👌
# # else -> # Insuficiente 😞
# # }
# print('\nDeterminando calificacion de estudiante')


# calificacion = int(input('Digite la nota del estudiante: '))

# if calificacion < 1 or calificacion >100:
#     print('Nota invalida ❌')
# elif calificacion >= 90 and calificacion <=100:
#     print('Excelente 🥳')
# elif calificacion >= 80 and calificacion <90 :
#     print('Muy bien 👏')
# elif calificacion >= 70 and calificacion <80 :
#     print('bien 👏')
# elif calificacion >= 60 and calificacion <70 :
#     print('Suficiente 👌')
# else:
#     print('Insuficiente 😞')
    


# #& IF - ANIDADOS
# # # Determine si usuario puede Conducir?
# # # condicion: debe tener licencia (si/no) y ( (ser mayor de edad (>=18)  o estar emancipado (si/no) )
# licencia = 'si'
# emcp = 'si'
# edad = 17
# if licencia == 'si':
#     if edad >=18 or emcp == 'si':
#         print('Usuario puede conducir 🚗')
#     else:
#         print('Usuario no puede conducir 🚫 pq no tienes mayoridad ni estas emp')  
# else:
#     print('Usuario no puede conducir 🚫 pq no tienes licencia')    
# # print('\nDeterminando si usuario puede Conducir?')


# #? TERNARIO
# Es una forma corta de escribir una sentencia if-else en una sola línea.
# Sintaxis: valor_si_verdadero if condición else valor_si_falso
# print('\nAsignamos a una variable bandera de usuario autenticado o no')

autentiado = input('esta autorizado para entrar 1/0: ')
# quiero un bool de la var autenticado
bool_auth = bool(int(autentiado))
print(bool_auth) # 0 → 
# print(bool(autentiado)) # 0 → 
# print(bool('')) #F
# print(bool('a')) #T
# print(bool('0')) #T
# print(bool([])) #F
# print(bool({})) #F
# input == 0 → False
# int(), str(), bool(), float(), list(), tuple()...

bool_auth 
mensaje = '✅ Usuario autenticado' if bool_auth else '❌ Usuario NO autenticado'
print(mensaje) # 'Hola' → 




# TODO PROXIMO_TEMA:
#  EJERCICIO WEB LOGIN CONDICIONALES Y OPERADORES COMPARACION

    # TIPOS DE DATOS ESTRUCTURALES: LISTAS, TUPLAS, DICCIONARIOS, SETS
    # CILCLOS: FOR, WHILE, BREAK, CONTINUE, RANGE()
