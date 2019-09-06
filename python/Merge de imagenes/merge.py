import cv2
from matplotlib import pyplot as plt
import numpy as np
img = []
img.append(cv2.cvtColor(cv2.imread('constante_color_30.jpg',1), cv2.COLOR_BGR2RGB))
img.append(cv2.cvtColor(cv2.imread('variable_color_30.jpg',1), cv2.COLOR_BGR2RGB))
img.append(cv2.cvtColor(cv2.imread('color_img_color_30.jpg',1), cv2.COLOR_BGR2RGB))
img.append(cv2.cvtColor(cv2.imread('constante_color_300.jpg',1), cv2.COLOR_BGR2RGB))
img.append(cv2.cvtColor(cv2.imread('variable_color_300.jpg',1), cv2.COLOR_BGR2RGB))
img.append(cv2.cvtColor(cv2.imread('color_img_color_300.jpg',1), cv2.COLOR_BGR2RGB))
img.append(cv2.cvtColor(cv2.imread('constante_color_3000.jpg',1), cv2.COLOR_BGR2RGB))
img.append(cv2.cvtColor(cv2.imread('variable_color_3000.jpg',1), cv2.COLOR_BGR2RGB))
img.append(cv2.cvtColor(cv2.imread('color_img_color_3000.jpg',1), cv2.COLOR_BGR2RGB))

fig, ax  = plt.subplots(3, 3, sharex=True, figsize=(20,20))


ax[0][0].imshow(img[0]),ax[0][0].set_title('Frecuencia constante (30 valores)')

ax[1][0].imshow(img[1]),ax[1][0].set_title('Frecuencia variable (30 valores)')
ax[2][0].imshow(img[2]),ax[2][0].set_title('Señal en estudio (30 valores)')
plt.yticks([])
ax[0][1].imshow(img[3]),ax[0][1].set_title('Frecuencia constante (300 valores)')
ax[1][1].imshow(img[4]),ax[1][1].set_title('Frecuencia variable (300 valores)')
ax[2][1].imshow(img[5]),ax[2][1].set_title('Señal en estudio (300 valores)')
ax[0][2].imshow(img[6]),ax[0][2].set_title('Frecuencia constante (3000 valores)')
ax[1][2].imshow(img[7]),ax[1][2].set_title('Frecuencia variable (3000 valores)')
ax[2][2].imshow(img[8]),ax[2][2].set_title('Señal en estudio (3000 valores)')


for i in range(0,3):
	for j in range(0,3):
		ax[i][j].set_yticks([])
		ax[i][j].set_xticks([])


plt.savefig("merge.jpg")
