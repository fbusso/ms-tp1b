import numpy as np
from cv2 import imwrite
from funcion import f

# muestrea una funcion f
def muestrear(funcion, inicio, longitud):
    muestreo = []
    for i in range(inicio, inicio + longitud):    
        try:    
            muestreo.append(funcion[i])
        except IndexError:
            muestreo.append(0)

    return muestreo

# calcula los segmentos
def segmentos(funcion):
    segmentos = []
    inicio = 0
    longitud = 30
    distancia = 10

    r = np.empty(15)
    r.fill(1)

    #determina g[n]
    conv = np.convolve(r, r, mode='full')
    maximo = max(conv)

    g = []
    for valor in conv:
        g.append(valor/maximo)

    mitad = int(len(g)/2)

    #while (inicio + longitud) <= len(funcion):
    while inicio <= len(funcion):
        aux = muestrear(funcion, inicio, longitud)
        muestra = []

        for i in range(0, mitad+1):
            muestra.append(aux[i]*g[i+mitad])

        segmentos.append(muestra)
        inicio += distancia
    
    return segmentos

# evalua la transformada discreta de fourier en un valor o
def fourier(f, k):
    X = 0
    N = len(f)
    for n in range(0, N-1):
        X += (f[n]*np.e**((-1j*k*n)))
    return X

# calcula la matriz de espectro
def espectro(segmentos):
    def E(i, j):
        return 0.1*abs(fourier(segmentos[i-1], j)) + 0.8* abs(fourier(segmentos[i], j)) + 0.1*abs(fourier(segmentos[i+1], j))

    matriz = []
    n = -np.pi
    N = len(segmentos)-1
    for i in range(1, N):
        arr = []
        for j in range(0, N):
            arr.append(E(i, n))
            n += 2*np.pi/N

        #sacar comentario para redondear los valores
        #matriz.append(np.round_(arr, 3))
        matriz.append(arr)

    return matriz

def expandir(matriz):
    matriznp = np.matrix(matriz)
    maxValue = np.amax(matriznp)
    minValue = np.amin(matriznp)

    matrizExpandida = []

    for fila in matriz:
        filaExpandida = []
        for valor in fila:
            filaExpandida.append(int(((valor-minValue)/(maxValue-minValue))*255))
        matrizExpandida.append(filaExpandida)

    return matrizExpandida

def reescalar(matriz, factor):
    matrizAux = np.repeat(np.matrix(matriz), factor, axis=1)
    return np.repeat(matrizAux, factor, axis=0)

def guardarImagen(matriz, filename):
    matriz = reescalar(expandir(matriz), 100)
    imwrite(filename, matriz)

def espectroConstante():
    matriz = []
    n = 0.0
    k = (2*np.pi)/1

    for i in range(0, 29):
        fila = []
        for j in range(0, 29):
            fila.append(np.sin(k*n))
            n += 0.1
        matriz.append(fila)

    e = espectro(matriz)
    guardarImagen(e, 'constante.jpg')
    #guardar(espectroConstante, "espectroConstante.xlsx")

def espectroVariable():
    matrizEspectroVariable = []
    n = 0.0
    k = ((2*np.pi)/17.75)

    for i in range(0, 29):
        fila = []
        for j in range(0, 29):
            fila.append(np.sin(k*n*n))
            n += 0.1
        matrizEspectroVariable.append(fila)

    e = espectro(matrizEspectroVariable)
    guardarImagen(e, 'variable.jpg')
    #guardar(espectroVariable, "espectroVariable.xlsx")

# calculo de los segmentos
segmentos = segmentos(f)

# calculo de la matriz de espectro
matriz = espectro(segmentos)
# guardado de la matriz en una imagen
guardarImagen(matriz, 'color_img.jpg')

# calculo y guardado de las matrices 
# para señales de frecuencia constante
# y variable
espectroConstante()
espectroVariable()
