# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 5 - Ejercicio 1 - Pràctica 5."""

palabra=raw_input("Escribe una palabra ")
li=[]
while palabra <>"":
    li.append (palabra)
    palabra=raw_input("Escribe una palabra ")
print "Los numeros que has escrito son: ",li
