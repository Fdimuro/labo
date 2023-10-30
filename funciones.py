import pygame
from config import *

#------------------------------- Funciones para crear objetos ----------------------------------------------

def crear_bloque(left = 0 ,top = 0 ,ancho = 50 ,alto = 50,color = (255,255,255), dir = 3 ,borde = 0,radio = -1,imagen = None):
    Rect = pygame.Rect(left,top,ancho,alto)
    if imagen:
        imagen = pygame.transform.scale(imagen, (ancho, alto))

    return {"rect" : Rect, "color" : color, "dir": dir, "borde" : borde, "radio" : radio, "imagen": imagen}

def cargar_monedas(lista, cantidad, imagen = None):
    from random import randint
    from config import TAM_MONEDAS,TAMANIO_MAX_MONEDAS,TAMANIO_MIN_MONEDAS, AMARILLO,ALTO,ANCHO
    for i in range(cantidad):
        TAM_MONEDAS = randint(TAMANIO_MIN_MONEDAS, TAMANIO_MAX_MONEDAS )
        lista.append(crear_bloque(left=randint(0, ANCHO - TAM_MONEDAS), top=randint(0, ALTO - TAM_MONEDAS), ancho=TAM_MONEDAS, alto=TAM_MONEDAS, color=AMARILLO, radio=TAM_MONEDAS // 2, imagen=imagen))

#------------------------------- Detectar Colisión ----------------------------------------------
def detectar_colision(rect_1, rect_2):
    for tupla in [(rect_1, rect_2),(rect_2, rect_1)]:
        r1,r2 = tupla
        return  punto_en_rectangulo(r1.topleft, r2) or \
                punto_en_rectangulo(r1.topright, r2) or \
                punto_en_rectangulo(r1.bottomleft, r2) or \
                punto_en_rectangulo(r1.bottomright, r2) 

def punto_en_rectangulo(punto, rect):   
    x,y = punto #tupla punto(x,y)
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom #return true o false


#----------------------------- DETECTAR COLISIÓN CIRCULO -------------------------------------------------

def calcular_radio(rect_1):
    return rect_1.height // 2

def distancia_entre_puntos(punto_1,punto_2):
    x1,y1 = punto_1
    x2,y2 = punto_2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def detectar_colision_circulo(rect_1,rect_2):
    colision = False
    r1 = calcular_radio(rect_1)
    r2 = calcular_radio(rect_2)

    distancia = distancia_entre_puntos(rect_1.center, rect_2.center)
    if distancia <= r1 + r2:
        colision = True
    
    return colision