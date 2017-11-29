# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 5 - Ejercicio 9 - Pràctica 5.
Escribe un programa que te pida nombres de personas y sus números de teléfono. Para terminar de escribir números y numeros debe pulsar Intro cuando te pida el nombre. El programa termina escribiendo nombres y números de teléfono. Nota: La lista en la que se guardan los nombres y números de teléfono es [[nombre1, telef1], [nombre2, telef2], [nom3, telef3], etc]"""

print'Escriba un nombre:'
nN=str(input())
lLista=[]

while nN!='':
    print'Escriba un telefono:'
    nT=int(input())
    lLista+=[[nN,nT]]
    print'Escriba un nombre:'
    nN=str(input())
print 'El directorio de contactos es: '

for i in lLista:
    print(i)
