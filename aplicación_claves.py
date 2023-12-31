# -*- coding: utf-8 -*-
"""Aplicación Claves.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13JtilmU3BPl2XPlShJrF4eFYQQp3arC6
"""

!pip install streamlit

!pip install pyngrok

!pip install imcrypt

def is_prime(num):
  if num == 2:
    return True
  if num < 2 or num % 2 == 0:
    return False
  for n in range(3, int(num**0.5)+2, 2):
    if num % n == 0:
      return False
  return True

is_prime(13441)

#Algoritmo extendido de Euclides 
#para encontrar el inverso multiplicativo de dos números

def multiplicative_inverse(a, m):
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

#Algoritmo de Euclides 
#para determinar el máximo común divisor

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import imcrypt
# import random
# st.title('Claves')
# 
# 
# def is_prime(num):
#   if num == 2:
#     return True
#   if num < 2 or num % 2 == 0:
#     return False
#   for n in range(3, int(num**0.5)+2, 2):
#     if num % n == 0:
#       return False
#   return True
# 
# def multiplicative_inverse(a, m):
#     a = a % m; 
#     for x in range(1, m) : 
#         if ((a * x) % m == 1) : 
#             return x 
#     return 1
# 
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
# 
# 
# def main():
#   st.text('Ejercicio de encriptación de claves.')
#   input1 = st.text_input('Número Primo 1:')
#   #e_type = st.selectbox('Choose One:', ('Encryption', 'Decryption'))
#   input2 = st.text_input('Número Primo 2:')
#   submit = st.button('Realizar')
#   
#   if submit:
#     #Ambos campos deben ser primos
#     prime1 = int(input1)
#     prime2 = int(input2)
# 
#     if not (is_prime(prime1) and is_prime(prime2)):
#       st.error("No son números primos")
#     elif prime1 == prime2:
#       st.error("No pueden ser números iguales")
#     else:
#       #if Encryption is choosen
#       
#       n = prime1 * prime2
#       phi = (prime1-1)*(prime2-1)
#       e = random.randrange(1, phi)
#       
#       g = gcd(e, phi)
#       while g !=1:
#         e = random.randrange(1, phi)
#         g = gcd(e, phi)
# 
#       d = multiplicative_inverse(e, phi)
# 
#       st.text_input('Clave Pública', f'{(e,n)}')
#       st.text_input('Clave Privada', f'{(d,n)}')    
# 
# if __name__ == "__main__":
#     main()

!ls

!ngrok authtoken 1nP0IMngrGd6jzsuqUgM3iZqu2Y_4kE8Fv2GirivdQZRQcdcj

from pyngrok import ngrok

!streamlit run app.py &>/dev/null&

!pgrep streamlit

public_url = ngrok.connect('8501')

print(public_url)

#ngrok.kill()
