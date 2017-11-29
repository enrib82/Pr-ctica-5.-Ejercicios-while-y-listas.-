# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 5 - Ejercicio 3 - Pràctica 5. Exercicis per resoldre amb bucle for."""

nota=float(raw_input("Escribe una nota "))
li=[]
while nota>=0 and nota<=10:
    li.append (nota)
    nota=float(raw_input("Escribe otra nota "))
print "Tus notas son:",li
