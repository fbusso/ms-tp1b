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

def diferencia(funcionOriginal, funcionTransformada):
	N = np.min([len(funcionOriginal), len(funcionTransformada)])
	diferencia = []
	energiaTotal= 0
	for i in range(0,N):
		diferencia.append(funcionOriginal[i]-funcionTransformada[i])
	return diferencia




N = 30
y = antitransformada(transformada(f,N),300)
#print(compararResultados(f, y))
x = f


# plt.plot(range(0,301), y, color='C0')
# plt.title("Gráfica de la función transformada, discretizando w en 300 valores")
# plt.axis([0,300,-1.2,1.2])
# plt.savefig("3000valores.jpg")
t = []
for i in range(0,300):
	t.append(i*0.1)
# plt.figure(figsize=(20,5))

# markerline, stemlines, baseline = plt.stem(
    # t, y, linefmt='grey', markerfmt='.', bottom=0, use_line_collection=True)
# markerline.set_markerfacecolor('none')
# plt.tight_layout(pad=2)
# plt.title("Señal antitransformada a partir de w discretizada en " + str(N) + " valores")
# plt.xlabel("Tiempo [s]")
# plt.show()

fig, [ax1, ax3, ax2] = plt.subplots(3, 1, sharex=True, figsize=(20,8))
ax1.title.set_text("Señal antitransformada a partir de '$\omega$' discretizada en " + str(N) + " valores")
markerline1, stemlines1, baseline1 = ax1.stem(t, y, linefmt='grey', markerfmt='.', bottom=0, use_line_collection=True)
markerline1.set_markerfacecolor('none')
markerline3, stemlines3, baseline3 = ax3.stem(t, x[0:-1], linefmt='grey', markerfmt='.', bottom=0, use_line_collection=True)
markerline1.set_markerfacecolor('none')
markerline2, stemlines2, baseline2 = ax2.stem(t, diferencia(x,y) , linefmt='black', markerfmt='none', bottom=0, use_line_collection=True)
ax2.grid(True)
ax1.grid(True)
ax3.grid(True)
#ax2.axis([0,30,-1.2, 1.2])
#ax1.axis([0,30,-1.2, 1.2])
plt.xlabel("Tiempo [s]")
ax2.title.set_text("Correlación entre las señales")
ax3.title.set_text("Señal original")
ax1.title.set_text("Señal antitransformada a partir de w discretizada en " + str(N) + " valores")
plt.tight_layout(pad=2)
plt.savefig(str(N) + "valores.jpg")

		



