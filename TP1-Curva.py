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
numSim = 5

fr = []
vp = []
v = []
de = []
promedio= [[],[],[],[]]
for i in range(iteraciones):
	promedio[0].append(0)
	promedio[1].append(0)
	promedio[2].append(0)
	promedio[3].append(0)

for j in range(numSim):
	x = rnd.randint(0,36)
	results = []
	frecRelativas = []
	valoresProm = []
	desvios = []
	varianzas = []
	for i in range(iteraciones):
		result = ruleta()
		results.append(result)
		frecRelativas.append(results.count(x)/len(results))
		promedio[0][i]=promedio[0][i]+results.count(x)/len(results)/numSim
		valoresProm.append(calcVP(results))
		promedio[1][i]=promedio[1][i]+calcVP(results)/numSim
		var = np.var(results)
		varianzas.append(var)
		promedio[2][i]=promedio[2][i]+var/numSim
		desvios.append(var**(1/2))
		promedio[3][i]=promedio[3][i]+var**(1/2)/numSim
	fr.append(frecRelativas)
	vp.append(valoresProm)
	v.append(varianzas)
	de.append(desvios)

for i in range(numSim):
	plt.plot(fr[i], color='black')
plt.plot(promedio[0], color='red')
plt.hlines(1/37,0,iteraciones)
plt.axis([0,iteraciones,0,0.4])
plt.title("Frecuencia Relativa")
plt.ylabel('Fr del numero')
plt.xlabel('n')
plt.show()

for i in range(numSim):
	plt.plot(vp[i], color='black')
plt.plot(promedio[1], color='red')
plt.hlines(18,0,iteraciones)
plt.title("Valor Promedio")
plt.ylabel('Valor medio')
plt.xlabel('n')
plt.show()

for i in range(numSim):
	plt.plot(v[i], color='black')
plt.plot(promedio[2], color='red')
plt.hlines(114,0,iteraciones)
plt.title("Varianza")
plt.ylabel('Varianza')
plt.xlabel('n')
plt.show()

for i in range(numSim):
	plt.plot(de[i], color='black')
plt.plot(promedio[3], color='red')
plt.hlines(114**(1/2),0,iteraciones)
plt.title("Desvío Estándar")
plt.ylabel('Desvío')
plt.xlabel('n')
plt.show()