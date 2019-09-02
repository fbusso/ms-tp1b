import numpy as np
from cv2 import imwrite
from openpyxl import Workbook

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
    for i in range(1, len(segmentos)-1):
        arr = []
        for j in range(1, len(segmentos)-1):
            arr.append(E(i, j))
        #sacar comentario para redondear los valores
        #matriz.append(np.round_(arr, 3))
        matriz.append(arr)

    return matriz

# guarda la matriz de espectro en una hoja de calculo
def guardar(matriz, filename):
    wb = Workbook()
    ws = wb.active

    for fila in matriz:
        ws.append(fila)

    wb.save(filename)

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
    k = (2*np.pi)/5

    for i in range(0, 28):
        fila = []
        for j in range(0, 28):
            fila.append(np.sin(k*n))
            n += 0.1
        matriz.append(fila)

    e = espectro(matriz)
    guardarImagen(e, 'constante.jpg')
    #guardar(espectroConstante, "espectroConstante.xlsx")

def espectroVariable():
    matrizEspectroVariable = []
    n = 0.0
    k = (2*np.pi)/17.75

    for i in range(0, 29):
        fila = []
        for j in range(0, 29):
            fila.append(np.cos(k*n*n))
            n += 0.1
        matrizEspectroVariable.append(fila)

    e = espectro(matrizEspectroVariable)
    guardarImagen(e, 'variable.jpg')
    #guardar(espectroVariable, "espectroVariable.xlsx")

# definicion de f(t)
f = [
     0.60399859,
     0.14554001,
    -0.32998835,
    -0.71633899,
    -0.94600828,
    -0.99577604,
    -0.88049313,
    -0.64042494,
    -0.32716454,
     0.00834848,
     0.32394707,
     0.59023391,
     0.79115710,
     0.92228396,
     0.98790357,
     0.99786530,
     0.96475061,
     0.90168212,
     0.82084795,
     0.73267495,
     0.64551246,
     0.56566882,
     0.49765584,
     0.44452514,
     0.40821154,
     0.38982733,
     0.38987337,
     0.40834847,
     0.44474907,
     0.49795939,
     0.56603985,
     0.64593243,
     0.73311717,
     0.82127608,
     0.90204934,
     0.96500018,
     0.99793332,
     0.98772459,
     0.92180010,
     0.79033070,
     0.58906280,
     0.32248027,
     0.00669853,
    -0.32881774,
    -0.64184468,
    -0.88141587,
    -0.99596217,
    -0.94530919,
    -0.71476724,
    -0.32776907,
     0.14796348,
     0.60602894,
     0.92219125,
     0.98940997,
     0.75933068,
     0.27571541,
    -0.31809185,
    -0.81158859,
    -0.99981338,
    -0.77589120,
    -0.20325046,
     0.47843661,
     0.93996354,
     0.92281285,
     0.39995632,
    -0.36392724,
    -0.92327895,
    -0.90901390,
    -0.29232950,
     0.53768427,
     0.99296838,
     0.70675762,
    -0.13929110,
    -0.88406775,
    -0.88766395,
    -0.10709139,
     0.78192808,
     0.93864831,
     0.17257156,
    -0.77827263,
    -0.91848508,
    -0.05864878,
     0.87574052,
     0.80094694,
    -0.23476314,
    -0.98908693,
    -0.49046021,
     0.65450841,
     0.92529413,
    -0.08443892,
    -0.98010495,
    -0.44757622,
     0.75953434,
     0.80296049,
    -0.42105150,
    -0.96872462,
     0.08690187,
     0.99839668,
     0.17920768,
    -0.96004668,
    -0.35879227,
     0.90887401,
     0.45588504,
    -0.87929677,
    -0.47886290,
     0.88597440,
     0.43041424,
    -0.92581961,
    -0.30519606,
     0.97748759,
     0.09479441,
    -0.99908350,
     0.19932632,
     0.92917412,
    -0.54524197,
    -0.70040510,
     0.85888317,
     0.27573818,
    -0.99999959,
     0.29327414,
     0.81602072,
    -0.81634673,
    -0.25406952,
     0.99255893,
    -0.49785336,
    -0.58956553,
     0.98176413,
    -0.26488678,
    -0.73336336,
     0.94806424,
    -0.19469962,
    -0.74135789,
     0.96236060,
    -0.30002217,
    -0.61786678,
     0.99894801,
    -0.55999568,
    -0.31082610,
     0.93434075,
    -0.87476242,
     0.21315460,
     0.57715455,
    -0.98941705,
     0.79956305,
    -0.15618263,
    -0.55870039,
     0.96929825,
    -0.89560500,
     0.40816829,
     0.24623716,
    -0.78204386,
     0.99904027,
    -0.84452028,
     0.40486034,
     0.15133290,
    -0.64464530,
     0.94218823,
    -0.98612970,
     0.79299258,
    -0.43267954,
    -0.00067983,
     0.41570924,
    -0.74241309,
     0.94063889,
    -0.99976987,
     0.93265359,
    -0.76700281,
     0.53686286,
    -0.27575166,
     0.01212864,
     0.23285632,
    -0.44578978,
     0.62020109,
    -0.75512297,
     0.85345772,
    -0.92044873,
     0.96241795,
    -0.98582333,
     0.99662008,
    -0.99987202,
     0.99954571,
    -0.99842195,
     0.99807060,
    -0.99884957,
     0.99990596,
    -0.99917419,
     0.99338329,
    -0.97810225,
     0.94786928,
    -0.89646401,
     0.81739059,
    -0.70463558,
     0.55374255,
    -0.36319497,
     0.13601449,
     0.11863985,
    -0.38423336,
     0.63648677,
    -0.84447918,
     0.97379232,
    -0.99202085,
     0.87644497,
    -0.62284290,
     0.25341990,
     0.17907228,
    -0.59430464,
     0.89696591,
    -0.99925437,
     0.84975472,
    -0.46068117,
    -0.07801548,
     0.60920063,
    -0.94964769,
     0.95578736,
    -0.59323260,
    -0.02228707,
     0.64402360,
    -0.98498785,
     0.85556006,
    -0.28487340,
    -0.45197932,
     0.94801540,
    -0.88965769,
     0.27485378,
     0.53103345,
    -0.98837627,
     0.74794339,
     0.05357345,
    -0.82615919,
     0.94268212,
    -0.26839017,
    -0.64973505,
     0.99083434,
    -0.40423484,
    -0.58356776,
     0.99377069,
    -0.37060724,
    -0.65930544,
     0.96410206,
    -0.16157197,
    -0.84015774,
     0.82151405,
     0.23381153,
    -0.99343569,
     0.43062208,
     0.72784591,
    -0.86540591,
    -0.25185587,
     0.99999006,
    -0.22367219,
    -0.90665101,
     0.58538793,
     0.70021521,
    -0.81034251,
    -0.47636947,
     0.92601453,
     0.29336323,
    -0.97400636,
    -0.17840480,
     0.98872230,
     0.14091646,
    -0.98838709,
    -0.18277581,
     0.97247472,
     0.30184862,
    -0.92176350,
    -0.48804909,
     0.80113073,
     0.71279498,
    -0.56905823,
    -0.91580079,
     0.19978458,
     0.99951572,
     0.27970226,
    -0.84940210,
    -0.75029356,
     0.39826932,
     0.99704709,
     0.27250225,
    -0.79671653,
    -0.86342240,
     0.11536309,
     0.94997500,
     0.69685389,
    -0.32057247,
    -0.98605008,
    -0.62948345,
     0.34866567,
     0.98051818,
     0.69733675,
    -0.20362622,
    -0.91747892,
    -0.86410112,
    -0.12658588,
     0.69571076,
     0.99720020,
     0.59704555,
    -0.19496540,
    -0.84797735,
    -0.97200057,
    -0.52937573,
]

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
