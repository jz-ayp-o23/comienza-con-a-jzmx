"""
Comienza con A
"""

# Entradas
palabra = input("Escribe una palabra: ")

# Proceso
if palabra[0].lower() in "aá":
    comienza = "comienza"
else:
    comienza = "no comienza"

# Salidas
print(f"'{palabra}' {comienza} con 'A'")
