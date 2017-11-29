# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 5 - Ejercicio 5 - Pràctica 5.
Exercicis per resoldre amb bucle for."""

actual=input("Escribe un numero: ")
anterior=0
li=[]
while actual > anterior:
    li.append(actual)
    anterior=actual
    actual=input("Escribe un numero mayor que %d: " %actual)
print "Los numeros que has escrito son: ",li
