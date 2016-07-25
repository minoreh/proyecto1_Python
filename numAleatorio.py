import random

#var1 = int(raw_input("Ingresa un numero entero entre (10-101): "))

mi_lista = []

for n in range(10, 101):
    mi_lista.append(random.randint(10, 101))


num_usuario = int(raw_input("Ingresa un numero entero entre (10-101): "))
if (num_usuario >10 ) or (num_usuario <101):
    print(" Debe digitar un numero en el rango(10-101)")

else:
    print("numero correcto")



print "Lista:", mi_lista
print "Maximo:", max(mi_lista)
print "Minimo:", min(mi_lista)

#imprimir un numero al azar
azar = random.sample(mi_lista, 1)
print (azar)

