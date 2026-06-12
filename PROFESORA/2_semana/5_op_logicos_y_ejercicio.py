
# ***************Los operadores lógicos en Python CON PALABRAS, NO SIMBOLOS (and, or, not) 
# se utilizan para combinar expresiones booleanas (que son True o False). 
# Para tomar una decision o camino, basadas en varias condiciones al mismo tiempo.

print('')

# ***************Operador and (Y lógico):
# Devuelve True sólo si "ambas" condiciones son verdaderas.
# Si alguna es False, el resultado es False.

# ***************Operador or (O lógico):
# Devuelve True si "al menos una" condición es verdadera.
# Sólo devuelve False si todas las condiciones son falsas.

# ***************Operador not (Negación lógica):
# Invierte el valor booleano de una condición.
# Si la condición es True, not la convierte en False, y viceversa.


print('Operadores Logicos 🤓')
print('True and False =', True and False)  # F
print('True or False =', True or False)    # T 
print('not False =', not False)            # T          

#* Ejemplos prácticos, que resulta de...
autorizado = True
edad = 16
pago = False
print(autorizado and edad>18) #F
print(autorizado or pago)     #T
print(not autorizado)         #F

print('*********************🤸🏻🤸🏻‍♀️EJERCICIOS**************************')
#? ⭐ si hace mas de 20 grados (AND) hace sol, sera: "¡Día perfecto para un picnic!"
temperatura = 20
hace_sol = True
if temperatura > 20 and hace_sol: #ambas tiene que ser True para que pase lo siguiente
    print("¡Día perfecto para un picnic! 🌞")
else:
    print('Mejor nos quedamos en 🏠') #*

#? ⭐ si tienes paraguas (OR) hace sol, sera: "¡Vamos a pasear!"
tiene_paraguas = False

#& ⛹🏽⛹🏽 TAREA 1: como puedo expresar que: si es NO hace_sol: "Quizás deberíamos quedarnos en 🏠."
#& utilizando el operador not

#& PROXIMA LECCION:
#?     PRECEDENCIA DE OPERADORES

