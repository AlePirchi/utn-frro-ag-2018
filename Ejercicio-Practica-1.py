import matplotlib
import math
import copy
import matplotlib.pyplot as plt
import random
import numpy

#INICIO CORE
def generarPoblacion(pobIn, longCrom):
    poblacion = []
    for _ in range(pobIn):
        intermedio  = []
        for _ in range(longCrom):
            intermedio.append(str(random.randrange(2)))    
        poblacion.append("".join(intermedio))    
    return poblacion

def crossover(padre1, padre2, longCrom):
    longCross = random.randrange(longCrom)
    hijo1a = padre1[0 : longCross]
    hijo2a = padre2[0 : longCross]
    hijo1b = padre2[longCross : longCrom]
    hijo2b = padre1[longCross : longCrom]
    hijo1 = hijo1a + hijo1b
    hijo2 = hijo2a + hijo2b
    hijos = hijo1a = padre1[1 : longCross]
    hijos = []
    hijos.append(hijo1)
    hijos.append(hijo2)
    return hijos

def mutacion(elementoPoblacion, probMutacion):
    elPob = list(elementoPoblacion)
    if (probMutacion >= random.uniform(0,1)) :
        bit = random.randrange(0, len(elPob))
        if elPob[bit] == '1':
            elPob[bit] = '0'
        else:
            elPob[bit] = '1'
        return ''.join(elPob)
    else:
        return ''.join(elPob)

def seleccion(poblacion, probCrossover, probMutacion, longCrom, fitness):
    padre1 = numpy.random.choice(poblacion, p=fitness)
    padre2 = numpy.random.choice(poblacion, p=fitness)
    if (probCrossover >= random.uniform(0,1)) :
        hijos = crossover(padre1, padre2, longCrom)
                
    else:
        hijos=[padre1,padre2]
    hijosFinal = [(mutacion((hijos[0]), probMutacion)), (mutacion((hijos[1]), probMutacion))]
    return hijosFinal   

def fObjetivo(num):
    coef = math.pow(2, 30) - 1
    return math.pow(num/coef, 2)

def fObjetvioBatch(valores):
    resultados = []
    for i in range(len(valores)):
        resultados.append(fObjetivo(valores[i]))
    return(resultados)


def getFitness(poblacion):
    valoresInd = []
    fitness = []
    valoresInd = poblacionDecimal(poblacion) 
    suma = sum(valoresInd)
    for j in range(len(poblacion)):
        fitness.append(valoresInd[j] / suma)    
    return(fitness)

def prom(valoresInt): 
    suma = sum(valoresInt)

    return(suma / len(valoresInt))

def poblacionDecimal(poblacion): #bien
    valoresInt = []
    for i in range(len(poblacion)):
        valorDec = int(poblacion[i],2)
        valoresInt.append(valorDec)       
    return(valoresInt)
#FIN CORE

#constantes 
probCrossover =  0.75
probMutacion = 0.05
cantPruebas = 2000
longCrom = 30
pobInicial = 10

#random.choice()

#Inicio del Ejercicio

poblacion = generarPoblacion(pobInicial,longCrom) #Inicializacion
print('Poblacion Inicial: ')
print(poblacion)
nuevaPoblacion = [] #se crea vacia la proxima generacion
maximos = [] #inicializacion de maximos, minimos y promedios
promedios = []
minimos = []
for i in range (cantPruebas): #ciclos de programa
    print('Corrida numero: ')
    print(i)
    fitness = getFitness(poblacion) #se obtiene la lista con el fitness de cada elemento
    for _ in range(len(poblacion)//2): #se seleccionan elementos de a 2
        hijos = seleccion(poblacion,probCrossover,probMutacion,longCrom, fitness)
        nuevaPoblacion.append(hijos[0]) #se añaden elementos a la nueva poblacion
        nuevaPoblacion.append(hijos[1])
    poblacion.clear() #se limpia la poblacion anterior
    poblacion = nuevaPoblacion[:]  #se reemplaza la poblacion
    nuevaPoblacion.clear() #se limpia para la nueva generacion 

    #se genera una lista para cada parametro a graficar
    maximos.append(max(fObjetvioBatch(poblacionDecimal(poblacion)))) 
    promedios.append(prom(fObjetvioBatch(poblacionDecimal(poblacion))))
    minimos.append(min(fObjetvioBatch(poblacionDecimal(poblacion))))

#se muestran las listas y los maximos, minimos y promedios absolutos
print('Maximo:')
print(max(maximos))
print('Maximos:')
print(maximos)
print('Promedio:')
print(prom(promedios))
print('Promedios:')
print(promedios)
print('Minimo:')
print(min(minimos))
print('Minimos:')
print(minimos)

#Graficos
generaciones = range(0,cantPruebas)
plt.figure()
plt.plot(generaciones, maximos, label='Maximos')
plt.plot(generaciones, promedios, label='Promedios')
plt.plot(generaciones, minimos, label='Minimos')
plt.title('Evolucion de la Poblacion')
plt.ylabel('Puntaje')
plt.xlabel('Generacion')
plt.xticks(range(cantPruebas))
plt.ylim(0, max(maximos))
plt.legend(loc='upper right')
plt.show()