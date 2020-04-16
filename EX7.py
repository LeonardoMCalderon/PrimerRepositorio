"""Calcular la longitud de una sombra"""
CA = 20
A = 22
B = 68
import math

hyp = int(abs(math.cos(math.degrees(22))*CA))
print("La hipotenusa tiene un valor de", hyp)
CO = int(abs(math.sqrt(hyp**2) - math.sqrt(CA**2)))


print ("Miientras que la sombra tiene un valor de" CO)