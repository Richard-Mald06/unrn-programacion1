nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
num=0
nombres_limpios=[]
for i in nombres:
    nombre = nombres[num].strip().capitalize()
    nombres_limpios.append(nombre)
    num+=1
print(nombres_limpios)