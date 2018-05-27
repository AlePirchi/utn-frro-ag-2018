import matplotlib
import math

import random
import numpy

def generarPoblacion(pobIn, longCrom):
    poblacion = []
    for _ in range(pobIn):
        intermedio  = []
        for _ in range(longCrom):
            intermedio.append(str(random.randrange(2)))    
        poblacion.append("".join(intermedio))

    #return [["".join(l) for l in [str(random.randrange(2)) for j in range(longCrom)]] for _ in range(pobIn)]
    
    return poblacion

def crossoverLegacy(padre1,padre2,longCrom, probMutacion):
    hijo = []
    hijo2 = []
    hijos = []
    longCross = random.randrange(longCrom)
    for i in range(longCross):
        hijo.append(padre1[i])
        hijo2.append(padre2[i])
    for j in range(longCross, longCrom):
        hijo.append(padre2[j])
        hijo2.append(padre1[j])

    hijos.append("".join(str(hijo)))
    hijos.append("".join(str(hijo2)))

    return hijos

def crossover(padre1, padre2, longCrom):
    longCross = random.randrange(longCrom)
    hijo1a = padre1[1 : longCross]
    hijo2a = padre2[1 : longCross]
    hijo1b = padre2[longCross : longCrom]
    hijo2b = padre1[longCross : longCrom]
    hijo1 = hijo1a + hijo1b
    hijo2 = hijo2a + hijo2b
    hijos = hijo1a = padre1[1 : longCross]
    hijos = []
    hijos.append(hijo1)
    hijos.append(hijo2)
    return hijos

def mutacion(elemntoPoblacion, probMutacion):
    if (probMutacion >= random.uniform(0,1)) :
        bit = random.randrange(0, elemntoPoblacion.range())
        if elemntoPoblacion[bit] == 1:
            elemntoPoblacion[bit] = 0
        else:
            elemntoPoblacion[bit] = 1
        return elemntoPoblacion
    else:
        return elemntoPoblacion

def seleccion(poblacion, probCrossover, probMutacion, longCrom):
    padre1 = poblacion[random.randrange(0, poblacion.range())]
    padre2 = poblacion[random.randrange(0, poblacion.range())]
    if (probCrossover >= random.uniform(0,1)) :
        hijos = []
        hijos = crossover(padre1, padre2, longCrom)
        hijo1 = hijos[1]
        hijo2 = hijos[2]
    else:
        hijo1 = padre1
        hijo2 = padre2
    hijo1 = mutacion(hijo1, probMutacion)
    hijo2 = mutacion(hijo2, probMutacion)
    hijos = []
    return hijos

def fObjetivo(num):
    coef = math.pow(2, 30) - 1
    return math.pow(num/coef, 2)

def fitness(poblacion):
    valoresInd = []
    fitness = [] 
    for i in range(len(poblacion)):
        valorDec = fObjetivo(int(poblacion[i],2))
        valoresInd.append(valorDec)
    suma = sum(valoresInd)
    for j in range(len(poblacion)):
        fitness.append(valoresInd[j] / suma)    
    return(fitness)


#Inicio del Ejercicio

poblacion = generarPoblacion(30,10)
print(poblacion)
fitness = fitness(poblacion)
print(fitness)
print(sum(fitness))
