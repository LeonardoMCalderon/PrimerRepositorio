"""Cantidad de meses que han transurrido desde el nacimiento de una persona"""
EDAD =int(input("Mencione cuantos años tiene"))
MESESTRANSCURRIDOS =int(input("Mencione cuantos meses han pasado después de su ultimo cumpleaños"))
TOTALMESES = (EDAD*12)+MESESTRANSCURRIDOS

print("Han transcurrido", TOTALMESES, "meses desde su nacimiento")