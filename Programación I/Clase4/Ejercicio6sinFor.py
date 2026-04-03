# Ejercicio 6
# Escribir un programa que:
# Tenga una lista ya cargada.
# Pida al usuario un elemento.
# Indique si ese elemento esta en la lista.
# Si esta, mostrar en que posicion aparece.
lista=["muñe","fufi","nemo","pochoclo"]
mascota=input("ingrese una mascota: ")
i=0
encontrado=False
while i<len(lista):
    if lista[i]==mascota:
        print(f"{mascota} esta en el lugar{i}")
        encontrado=True
    i+=1
if encontrado==False:
        print("esa mascota no esta")