import csv
from random import choice

lista = []

with open('C:/gustavo/datos_servicios_1.csv') as csvarchivo:
    entrada = csv.reader(csvarchivo)
    for reg in entrada:
        lista.append(reg[0])

csvarchivo.close()

def recuperaParValores(listaValores):
    elem1 = choice(listaValores)

    while True:
        elem2 = choice(listaValores)

        if(elem1 != elem2):
            break

    return [elem1, elem2]

#print lista

with open('C:/gustavo/grafo2.csv','w') as ficheroSalida:
    for ejec in xrange(10000):
        relacion = recuperaParValores(lista)
        ficheroSalida.write(relacion[0] + " " + relacion[1]+"\n")

#for ejec in xrange(25):
#    print recuperaParValores(lista)