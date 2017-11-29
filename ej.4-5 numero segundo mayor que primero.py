# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 5 - Ejercicio 4 - Pràctica 5. Exercicis per resoldre amb bucle for."""

numero1=int(input("Escribe un numero: "))
numero2=0

while numero2 <= numero1:
    numero2=int(input("Escribe un numero mayor que %d: " %numero1))
    if numero2 <= numero1:
        print numero2, " Es menor que " ,numero1
    else:

        print "Los numeros que has escrito son: ",numero1,numero2
