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


imagen=0
for i in range(0,10,10):
	N = 30
	x1 = 0
	x2 = 30
	y1 = antitransformada(transformada(f[x1:x2+1],30),x2-x1)
	y2 = antitransformada(transformada(f[x1:x2 +1 ],300),x2-x1)
	y3 = antitransformada(transformada(f[x1:x2 +1 ],3000),x2-x1)
	#print(compararResultados(f, y))
	x = f
	t = []
	for it in range(0,x2-x1):
		t.append((i*0.1)+(it*0.1))

	fig, [[ax11, ax12, ax13], [ax21, ax22, ax23], [ax31, ax32, ax33]] = plt.subplots(3, 3, sharex=True, figsize=(20,7))
	ax11.stem(t, y1, linefmt='grey', markerfmt='.', bottom=0, use_line_collection=True)
	ax12.stem(t, y2, linefmt='grey', markerfmt='.', bottom=0, use_line_collection=True)
	ax13.stem(t, y3, linefmt='grey', markerfmt='.', bottom=0, use_line_collection=True)
	
	ax21.stem(t, x[x1:x2], linefmt='grey', markerfmt='.', bottom=0, use_line_collection=True)
	ax22.stem(t, x[x1:x2], linefmt='grey', markerfmt='.', bottom=0, use_line_collection=True)
	ax23.stem(t, x[x1:x2], linefmt='grey', markerfmt='.', bottom=0, use_line_collection=True)


	ax31.stem(t, diferencia(y1,x) , linefmt='black', markerfmt='none', bottom=0, use_line_collection=True)
	ax32.stem(t, diferencia(y2,x[x1:x2+1]) , linefmt='black', markerfmt='none', bottom=0, use_line_collection=True)
	ax33.stem(t, diferencia(y3,x[x1:x2+1]) , linefmt='black', markerfmt='none', bottom=0, use_line_collection=True)

	# ax2.grid(True)
	# ax1.grid(True)
	# ax3.grid(True)
	inicio = i*0.1
	ax12.axis([-0.1+inicio,3+inicio,-1.2, 1.2])
	ax11.axis([-0.1+inicio,300+inicio,-1.2, 1.2])
	ax13.axis([-0.1+inicio,3+inicio,-1.2, 1.2])
	ax22.axis([-0.1+inicio,3+inicio,-1.2, 1.2])
	ax21.axis([-0.1+inicio,300+inicio,-1.2, 1.2])
	ax23.axis([-0.1+inicio,3+inicio,-1.2, 1.2])
	# ~ ax32.axis([-0.1+inicio,3+inicio,-1.2, 1.2])
	# ~ ax31.axis([-0.1+inicio,300+inicio,-1.2, 1.2])
	# ~ ax33.axis([-0.1+inicio,3+inicio,-1.2, 1.2])

	ax31.title.set_text("Correlación entre las señales")
	ax21.title.set_text("Señal original")
	ax11.title.set_text("Señal reconstruida (discretización: 30 valores)")
	ax32.title.set_text("Correlación entre las señales")
	ax22.title.set_text("Señal original")
	ax12.title.set_text("Señal reconstruida (discretización: 300 valores)")
	ax33.title.set_text("Correlación entre las señales")
	ax23.title.set_text("Señal original")
	ax13.title.set_text("Señal reconstruida (discretización: 3000 valores)")
	#plt.savefig(str(N) + "valores (cada 30 pulsos).jpg")
	plt.savefig("./photo(" + str(x1) +"-"+ str(x2) + ").jpg")
	plt.show()
	plt.close()
	imagen +=1
		



