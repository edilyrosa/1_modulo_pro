

# * EJERCICIO: OPERADORES DE COMPARACIÓN E IGUALDAD 
# TODO: Hay de adelanto de condicionales y metodos: strip() y lower()

# & 🤸🏻🤸🏻‍♀️EJERCICIO: Comparador de Palabras: Pide 2 palabras por consola e imprime si son idénticas,
# & sin importar su mayusculas.
print('='*20)
print('COMPARANDO STR')
print('='*20)

# input # 1
text_1 = input('Ingrese el str 1: ').strip().lower()
# input # 2
text_2 = input('Ingrese el str 2: ').strip().lower()

if text_1 == text_2:
    print('Las cadenas son iguales 🥳')
else:
    print('Las cadenas NO son iguales ❌')


# & 💡UTILIDAD DE EJERCICIO: imagina desarrollar un programa que antes de permitir el acceso compare
# & contrasena y clave ingresada por usuario son identicas a las guardadas en la BBDD.

    
#& PROXIMA LECCION:
#?     OPERADORES LÓGICOS (and, or, not)