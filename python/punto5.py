import numpy as np
from funcion import f
import matplotlib
import matplotlib.pyplot as plt


def fourier(f, k):
    X = 0
    N = len(f)
    for n in range(0, N-1):
        X += (f[n]*np.e**((-1j*k*n)))
    return X
#

def transformada(f, N): #N es la cantidad de valores a discretizar
	X = []
	w = -np.pi
	for i in range(0, N-1):
		X.append(fourier(f,w))
		w += 2*np.pi/N
	return X
#

def antitransformada(f, NroPulsos):
	resultado = []
	for n in range(0, NroPulsos):
		x = 0.0
		w = -np.pi
		N = len(f)
		for W in range(0, N-1):
			x += f[W]*np.e**(1j*n*w)
			w += 2*np.pi/N
		x = x/N
		resultado.append(np.real(x))
	return resultado
#

def compararResultados(funcionOriginal, funcionTransformada):
	N = np.min([len(funcionOriginal), len(funcionTransformada)])
	diferencia = 0
	energiaTotal= 0
	for i in range(0,N-1):
		diferencia += abs(funcionOriginal[i]-funcionTransformada[i])
		energiaTotal += abs(funcionOriginal[i])
	return diferencia/energiaTotal

print("Diferencia de energia proporcional a la energia de la señal original: ")
y = antitransformada(transformada(f,30000),301)
#print(compararResultados(f, y))
x = f


plt.plot(range(0,301), y, color='C0')
plt.title("Gráfica de la función transformada, discretizando w en 30000 valores")
plt.axis([0,300,-1.2,1.2])
plt.savefig("3000valores.jpg")

		
