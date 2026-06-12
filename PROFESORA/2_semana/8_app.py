
# Corre en la termina:
#? pip install streamlit
#* streamlit run 8_app.py

import streamlit as st

#credenciales que llamamos de la BBDD
CORREO_CORRECTO = 'admin@gmail.com'
PASS_CORRECTO = '1234'

#Titulo 
st.title('Login de usuario 👤') # <h1>

#formulario
correo = st.text_input('Digite su Correo electrónico')
passw = st.text_input('Digite su Clave', type='password')

if st.button('Iniciar sesión'): # si es verdad q se hizo clic sobre el btn
    if correo == CORREO_CORRECTO and passw == PASS_CORRECTO:
        st.success('Bienvenido al sistema 🎉')
    else:
        st.error('Correo o contraseña incorrectos ❌')
        
        
    
    
# TODO PROXIMO_TEMA:
    # TIPOS DE DATOS ESTRUCTURALES: LISTAS, TUPLAS, DICCIONARIOS, SETS
    # CILCLOS: FOR, WHILE, BREAK, CONTINUE, RANGE()