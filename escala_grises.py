#se imprtan las librerias cv2
import cv2

#ruta de la imagen y tamben se visualiza la imagen en bits
imagen = cv2.imread('unnamed.png')

#se muestra la imagen original
cv2.imshow("ISC",imagen)

#se inserta la imagen a funcion de deteccion de bordes
imagenBorder= cv2.Canny(imagen,100,200)

#se pude observar la imagen con los bordes
cv2.imshow("imagen con bordes",imagenBorder)


cv2.waitKey(0)

