import pygame
from config import *
from funciones import *
from pygame import locals

pygame.init() 





reloj = pygame.time.Clock() 

#------------------------ Cargo imagenes --------------------------------------------------

jugador_imagen = pygame.image.load("./Assets/vayne2.png")


#------------------------ Configuración Pantalla Principal --------------------------------------------------
PANTALLA = pygame.display.set_mode(PANTALLA_TAM)
pygame.display.set_caption("Juego Pygame") 
# PANTALLA.fill(NEGRO)

bloque = crear_bloque(imagen=jugador_imagen, ancho= 85, alto= 85, color= CUSTOM, radio = 100)


mover_abajo = False
mover_arriba = False
mover_derecha = False
mover_izquierda = False



esta_Jugando = True

# PANTALLA.fill(NEGRO)

while esta_Jugando:
    reloj.tick(FPS)
    # detectamos los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            esta_Jugando = False

        if evento.type == locals.KEYDOWN:
            if evento.key == locals.K_RIGHT or evento.key == locals.K_d:
                mover_derecha = True
                mover_izquierda = False

            if evento.key == locals.K_DOWN or evento.key == locals.K_s:
                mover_abajo = True
                mover_arriba = False
                
            if evento.key == locals.K_LEFT or evento.key == locals.K_a:
                mover_izquierda = True
                mover_derecha = False

            if evento.key == locals.K_UP or evento.key == locals.K_w:
                mover_arriba = True
                mover_abajo = False

        if evento.type == locals.KEYUP:
            if evento.key == locals.K_RIGHT or evento.key == locals.K_d:
                mover_derecha = False

            if evento.key == locals.K_DOWN or evento.key == locals.K_s:
                mover_abajo = False

            if evento.key == locals.K_LEFT or evento.key == locals.K_a:
                mover_izquierda = False

            if evento.key == locals.K_UP or evento.key == locals.K_w:
                mover_arriba = False


        # Muevo el bloque de acuerdo a su dirección
    if mover_arriba and bloque["rect"].top >= 0:
        bloque["rect"].top -= VELOCIDAD
    if mover_abajo and bloque["rect"].bottom <= ALTO:
        bloque["rect"].top += VELOCIDAD
    if mover_izquierda and bloque["rect"].left >= 0:
        bloque["rect"].left -= VELOCIDAD
    if mover_derecha and bloque["rect"].right <= ANCHO:
        bloque["rect"].left += VELOCIDAD


    
    # dibujar pantalla
    PANTALLA.fill(NEGRO)
    PANTALLA.blit(bloque["imagen"], bloque["rect"])




    pygame.display.flip()
 


pygame.quit() 

