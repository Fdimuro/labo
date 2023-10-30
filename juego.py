from pygame import locals
from config import *
from sys import exit
from funciones import *
from random import *

pygame.init()
reloj = pygame.time.Clock() 
PANTALLA = pygame.display.set_mode((ANCHO,ALTO), pygame.SRCALPHA)
pygame.display.set_caption("Juego") 
PANTALLA.fill(CUSTOM)



mover_abajo = False
mover_arriba = False
mover_derecha = False
mover_izquierda = False

esta_Jugando = True

while esta_Jugando:
    reloj.tick(FPS)
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
                esta_Jugando = False
                exit()  
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
        
        
    
    if mover_arriba and personaje_principal["rect"].top >= 0:
        personaje_principal["rect"].top -= VELOCIDAD
    if mover_abajo and personaje_principal["rect"].bottom <= ALTO:
        personaje_principal["rect"].top += VELOCIDAD
    if mover_izquierda and personaje_principal["rect"].left >= 0:
        personaje_principal["rect"].left -= VELOCIDAD
    if mover_derecha and personaje_principal["rect"].right <= ANCHO:
        personaje_principal["rect"].left += VELOCIDAD

    if enemigo_1["rect"].right >= ANCHO:
        #Choco derecha
        if enemigo_1["dir"] == AD:
            enemigo_1["dir"] = AI
        elif enemigo_1["dir"] == BD:
            enemigo_1["dir"] = BI
    elif enemigo_1["rect"].left <= 0:
        #Choco izquierda
        if enemigo_1["dir"] == AI:
            enemigo_1["dir"] = AD
        elif enemigo_1["dir"] == BI:
            enemigo_1["dir"] = BD
    elif enemigo_1["rect"].bottom >= ALTO:
        #Choco abajo
        if enemigo_1["dir"] == BI:
            enemigo_1["dir"] = AI
        elif enemigo_1["dir"] == BD:
            enemigo_1["dir"] = AD
    elif enemigo_1["rect"].top <= 0:
            #Choco arriba
            if enemigo_1["dir"] == AI:
                enemigo_1["dir"] = BI
            elif enemigo_1["dir"] == AD:
                enemigo_1["dir"] = BD

    if enemigo_1["dir"] == BD:
        enemigo_1["rect"].top += VELOCIDAD
        enemigo_1["rect"].left += VELOCIDAD
    elif enemigo_1["dir"] == BI:
        enemigo_1["rect"].top += VELOCIDAD
        enemigo_1["rect"].left -= VELOCIDAD
    elif enemigo_1["dir"] == AI:
        enemigo_1["rect"].top -= VELOCIDAD
        enemigo_1["rect"].left -= VELOCIDAD
    else:
        enemigo_1["rect"].top -= VELOCIDAD
        enemigo_1["rect"].left += VELOCIDAD



    
    # if detectar_colision(personaje_principal["rect"], enemigo_1["rect"]):
    #     print("colision!!!")

    PANTALLA.fill(CUSTOM)
    PANTALLA.blit(personaje_principal["imagen"], personaje_principal["rect"])
    PANTALLA.blit(enemigo_1["imagen"],enemigo_1["rect"])
    
    pygame.display.flip()
    

    
pygame.quit()