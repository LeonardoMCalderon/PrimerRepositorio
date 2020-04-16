"""Calcular la velocidad de una llanta"""
Velocidad = int(input("¿Cual es la velocidad de la llanta?(en cms/seg)"))
Periodo = int (2*3.1416)/Velocidad
vueltas = int(Periodo * 100000)

print("la llanta en un kilometro a una velocidad de", Velocidad, "cms/seg hara", vueltas, "vueltas")