# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 5 - Ejercicio 8 - Pràctica 5.
Escribe un programa que te pida primero un número y luego te pida números hasta que la suma de los números introducidos coincida con el número inicial. El programa termina escribiendo la lista de números."""

print 'Escriba el numero limite:'
nNlimite=int(input())
print 'Escriba otro numero, menor que %s:'% str(nNlimite)
nN=int(input())

while nN > nNlimite:
    print 'El numero es demasiado grande, intentelo de nuevo:'
    nN=int(input())
lLista=[]
suma=nN
while suma<=nNlimite:
    lLista+=[nN]
    print 'Escriba otro numero:'
    nN=int(input())
    suma+=nN
print 'La suma de estos numeros, %s, es menor o igual a %s' % (str(lLista), str(nNlimite))
