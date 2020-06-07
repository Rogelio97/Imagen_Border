#se imprtan las librerias cv2
import cv2
import numpy as np

#ruta de la imagen
imagen = cv2.imread('unnamed.png')

#funcion para convertir la imagene a escala de grises
gray = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

_,th = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)

#introduciendo los contornos de la imagen 
contornos,hierarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print ('hierarchy=',hierarchy)
for i in range (len(contornos)):
  #se escribe los contornos de la imagen
  cv2.drawContours(imagen, contornos, i, (0,255,0), 3)
  #aqui se visualiza la imagen con los bordes
  cv2.imshow('imagen',imagen)
  cv2.waitKey(0)
cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
