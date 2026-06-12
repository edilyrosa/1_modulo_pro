

# * EJERCICIO: OPERADORES DE COMPARACIÓN E IGUALDAD 
# TODO: Hay de adelanto de condicionales y metodos: strip() y lower()

# & 🤸🏻🤸🏻‍♀️EJERCICIO: Comparador de Palabras: Pide 2 palabras por consola e imprime si son idénticas,
# & sin importar su mayusculas.
print('='*20)
print('COMPARANDO STR')
print('='*20)
#* 1. solicitamos las palabras de usuario 
palabra_uno = input('Ingrese el primer str: ').strip().lower()
palabra_dos = input('Ingrese el segundo str: ').strip().lower()

#* 2. las comparamos 
if palabra_uno == palabra_dos:
#* 2.1 si sin iguales lo informamos
    print('🥳💃🏻🥳💃🏻Plabras digitadas son iguales')
#* 2.2 si sin diferentes lo informamos
else:
    print('❌❌❌❌Plabras digitadas NOOO son iguales')
    

# & 💡UTILIDAD DE EJERCICIO: imagina desarrollar un programa que antes de permitir el acceso compare
# & contrasena y clave ingresada por usuario son identicas a las guardadas en la BBDD.

    
#TODO:  OPERADORES LÓGICOS (and, or, not)