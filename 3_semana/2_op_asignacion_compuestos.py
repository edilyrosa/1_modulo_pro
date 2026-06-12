
# ******************Operadores de asignación compuestos
# Permiten realizar una operación con el valor actual de la variable y luego 
# asignar el resultado a esa misma variable. Son equivalentes a escribir la operación completa 
# con asignación, pero en forma abreviada.

#* ®️Resumen
# ✅El operador = asigna un valor directamente.
# ✅💡Los operadores compuestos (+=, -=, *=, etc.) 
# modifican la variable basándose en su valor actual.
# ✅Son útiles para escribir código más limpio y eficiente.


numero = 5
#! numero  = numero + 5
numero  += 5
print(numero) #10

numero *= 5
print(numero) #50

numero -=20
print(numero) #30


numero /=2
print(numero) #15.0



numero %= 2 
print(numero) # 1.0

numero += 5 
print(numero) # 6.0

numero //= 2 
print(numero) # 3.0


numero **= 2 
print(numero) # 9.0





print('**'*10 , 'EJERCICIO', '**'*10)
a = 7 
b = 2

x = a #7
x +=b
# Yo no se cuanto vale "x", lo que traiga acumulado +-/** * = valor
print(x) #9

x -=b
print(x) #7

x *=b
print(x) #14

# USO: EL VALOR ACUMULATIVO DE CARRITO
# total += precio_producto

#TODO:     OPERADORES DE COMPARACION.

