# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 5 - Ejercicio 2 - Pràctica 5. Exercicis per resoldre amb bucle for."""

numero=raw_input("Escribe un numero ")
li=[]
while numero <>"":
    li.append(numero)
    numero=raw_input("Escribe otro numero ")
print "Los numeros que has escrito son: ",li
