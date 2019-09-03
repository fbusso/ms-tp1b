import cv2
import cmapy #para instalar este paquete hay que instalar mathplot

imagen = cv2.imread("constante.jpg")

imagen_color = cv2.applyColorMap(imagen, cmapy.cmap('CMRmap'))
cv2.imwrite("constante_color.jpg", imagen_color)


imagen = cv2.imread("variable.jpg")

imagen_color = cv2.applyColorMap(imagen, cmapy.cmap('CMRmap'))
cv2.imwrite("variable_color.jpg", imagen_color)

imagen = cv2.imread("color_img.jpg")

imagen_color = cv2.applyColorMap(imagen, cmapy.cmap('CMRmap'))
cv2.imwrite("color_img_color.jpg", imagen_color)
