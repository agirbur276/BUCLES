'''EJERCICIO 4:
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas.'''
numero=int(input("Dime un número entero positivo: "))
if numero>=0:
    for i in range(numero, -1, -1):
        print(i, end=",")
        
elif numero==0:
        print(i, end=",")
