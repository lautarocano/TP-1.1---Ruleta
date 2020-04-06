import random as rnd
import matplotlib.pyplot as plt
import numpy as np

def ruleta():
	return rnd.randint(0,36)

def calcVP(results):
	c = 0
	for j in results:
		c += j
	return c/len(results)

iteraciones = 1000

results = []
frecRelativas = []
valoresProm = []
desvios = []
varianzas = []

x = rnd.randint(0,36)
for i in range(iteraciones):
	result = ruleta()
	results.append(result)
	frecRelativas.append(results.count(x)/len(results))
	valoresProm.append(calcVP(results))
	var = np.var(results)
	varianzas.append(var)
	desvios.append(var**(1/2))

plt.plot(frecRelativas)
plt.hlines(1/37,0,iteraciones)
plt.axis([0,iteraciones,0,0.4])
plt.title("Frecuencia Relativa")
plt.ylabel('Fr del numero '+ str(int))
plt.xlabel('n')
plt.show()

plt.plot(valoresProm)
plt.hlines(18,0,iteraciones)
plt.title("Valor Promedio")
plt.ylabel('Valor medio')
plt.xlabel('n')
plt.show()

plt.plot(varianzas)
plt.hlines(114,0,iteraciones)
plt.title("Varianza")
plt.ylabel('Varianza')
plt.xlabel('n')
plt.show()

plt.plot(desvios)
plt.hlines(114**(1/2),0,iteraciones)
plt.title("Desvío Estándar")
plt.ylabel('Desvío')
plt.xlabel('n')
plt.show()