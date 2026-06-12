
#* TIPOS DE DATOS PRIMITIVOS
entero  = 123
flotante  = 123.1
texto  = 'Edily'
texto  = "Edily"
texto  = """Edily
Mora"""
is_auth = False
is_auth = True
#*CASTING Y REASIGNACION CON TIPADO DEBIL
contasena = '1234'
contasena = int('1234')

#*CONOCER EL TIPO DE DATO
print(type(contasena))

#* OPERACIONES ARITMETICAS CON NUMBERS
num_1 = 10
num_2 = 20.11
num_3 = '30'

suma_num = num_1 + num_2
suma_num = num_1 - num_2
suma_num = num_1 * num_2
suma_num = num_1 / num_2
suma_num = num_1 // num_2
suma_num = num_1 ** num_2
print(suma_num)

#* OPERACIONES ARITMETICAS CON NUMBERS Y STR
suma_str = num_1 * num_3
suma_str = str(num_1) + num_3
#! suma_str = num_1 + num_3
#! suma_str = num_1 -, /, **... num_3
print(suma_str)






print('25 % 4 = ', 25 % 4)
print('10 % 3 = ', 10 % 3)


print('10 % 2 = ', 10 % 2) # x es par si su % 2 == 0
print('10 % 2 = ', 11 % 2) # x es par si su % 2 == 1
# print('10 % 2 = ', 11 % 0) # x es par si su % 2 == 1




if 21 % 2 == 0:
    print('num es par')
    
contatenacion  = 'hola' + ' Adrian'
saludo = 'como estas'
print(contatenacion)
print(f'{contatenacion}, {saludo}')
print(f'{contatenacion}, {saludo}')
print(contatenacion* 8)



entero =  2500 
rulstado = 2.5*1000
nptacion = 2.5E-3
print(nptacion)


print(5**1)
print(5**0)
print(0**0)
print(5**2)

import math

print(math.pow(5, 2))



x = 5
x += 5 
x -= 2 
x *= 10 
x //= 4 
x %=4
x **=0
print(x)

print('a' != 34 )
print(ord('a'))
print(ord('A'))
print(ord('a') == 97 )

print('hola'.upper())
print('   hola   '.upper())
print('   hola   '.strip())
print('   HOLA   '.strip().lower())