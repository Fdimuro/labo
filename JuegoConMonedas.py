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


#---------------------------------------------- PERSONAJES ----------------------------------------------------------
jugador_imagen = pygame.image.load("./Assets/vayne2.png")
enemigo_imagen = pygame.image.load("./Assets/minion.png")
personaje_principal = crear_bloque (alto=100, ancho=70, imagen=jugador_imagen)
personaje_principal["rect"].center = CENTRO_PANTALLA
enemigo_1 = crear_bloque ( ancho = 60, alto = 60)
enemigo_1["rect"].top = 0

#---------------------------------------------- MONEDAS ----------------------------------------------------------
contador_monedas = 4
ancho_moneda = 30
alto_moneda = 30

monedas = []
for moneda in range(contador_monedas):
    monedas.append(crear_bloque(randint(0, ANCHO -  ancho_moneda), randint(0, ALTO - alto_moneda), ancho_moneda, alto_moneda, AMARILLO, 0 , 0, ancho_moneda // 2))

puntaje_monedas = 0
fuente = pygame.font.Font(None, 32)
texto_Monedas = fuente.render(f"Puntaje: {puntaje_monedas}", True, NEGRO)
#------------------------------------------------------------------------------------------------------------------
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


    
    for moneda in monedas[:]:
        if detectar_colision_circulos(moneda["rect"], personaje_principal["rect"]):
            monedas.remove(moneda)
            puntaje_monedas+= 1
            texto_Monedas = fuente.render(f"Puntaje: {puntaje_monedas}", True, NEGRO)
            if not monedas:
                for moneda in range(contador_monedas):
                    monedas.append(crear_bloque(randint(0, ANCHO -  ancho_moneda), randint(0, ALTO - alto_moneda), ancho_moneda, alto_moneda, AMARILLO, 0 , 0, ancho_moneda // 2))


    # Dibujo pantalla
    PANTALLA.fill(CUSTOM)
    PANTALLA.blit(personaje_principal["imagen"], personaje_principal["rect"])
    PANTALLA.blit(texto_Monedas,(0,0))
    # pygame.draw.rect(PANTALLA,personaje_principal["color"],personaje_principal["rect"], personaje_principal["borde"], personaje_principal["radio"])
    # PANTALLA.blit(enemigo_1["imagen"],enemigo_1["rect"])

    for moneda in monedas:
        pygame.draw.rect(PANTALLA,moneda["color"],moneda["rect"], moneda["borde"], moneda["radio"])
    


    # Acutalizo pantalla
    pygame.display.flip()
    

    
pygame.quit()