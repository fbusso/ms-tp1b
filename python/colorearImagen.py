import cv2
import cmapy #para instalar este paquete hay que instalar mathplot

imagen = cv2.imread("constante.jpg")

imagen_color = cv2.applyColorMap(imagen, cmapy.cmap('CMRmap'))
cv2.imwrite("constante_color.jpg", imagen_color)
