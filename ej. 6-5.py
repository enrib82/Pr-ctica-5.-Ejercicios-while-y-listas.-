# -*- coding: cp1252 -*-
"""Enrique Ibáñez Orero - 1º DAW - Practica 5 - Ejercicio 6 - Pràctica 5."""

lista=[]

num1=input("Introduce un numero: ")
print "Introduce un numero mayor que" ,num1,":",
num2=input()

while num1>num2 or num2-num1==1:
    if num2-num1==1:
        print "Introduce un numero con al menos un numero entre ellos:",
        num2=input()
    else:
        print num2,"no es mayor que",num1,". Vuelve a probarlo:",
        num2=input()

print "Introduce un numero entre",num1,"y",num2,":",
entre=input()

if entre>num1 and entre<num2:
    lista.append(entre)
    while entre>num1 and entre<num2:
        print "Introduce otro numero entre",num1,"y",num2,":",
        entre=input()
        if not entre>num1 or not entre<num2:
            print "Los numeros introducidos entre",num1,"y",num2,"son:",lista
            break
        else:
            lista.append(entre)
else:
    print "El usuario no introdujo ningun numero entre",num1,"y",num2
