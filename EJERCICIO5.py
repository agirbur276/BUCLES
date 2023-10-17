# -*- coding: utf-8 -*-
"""EJERCICIO 5:
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
año que dura la inversión"""
cantidad_invertida = float(input("Introduce la cantidad a invertir: "))
interes_anual = float(input("Introduce el interés anual (en porcentaje): ")) / 100
num_anios = int(input("Introduce el número de años de la inversión: "))
for anio in range(1, num_anios + 1):
    capital_obtenido = cantidad_invertida * (1 + interes_anual) ** anio
    print(f"Año {anio}: {capital_obtenido:.2f}")

