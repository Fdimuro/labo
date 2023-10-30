from pygame import locals
from config import *
from sys import exit
from funciones import *
from random import *
from pygame.locals import *

pygame.init()
reloj = pygame.time.Clock() 
PANTALLA = pygame.display.set_mode((ANCHO,ALTO), pygame.SRCALPHA)
pygame.display.set_caption("Juego") 
PANTALLA.fill(CUSTOM)
#---------------------------------------------- SONIDOS ----------------------------------------------------------
moneda_sonido = pygame.mixer.Sound("./Assets/moneda.mp3")
moneda_sonido.set_volume(0.1)
game_over_sonido = pygame.mixer.Sound("./Assets/gameover.mp3")
game_over_sonido.set_volume(0.1)

victoria_sonido = pygame.mixer.Sound("./Assets/victoria.mp3")
victoria_sonido.set_volume(0.1)

pygame.mixer_music.load("./Assets/fondo.mp3")
pygame.mixer_music.play(-1) #-1 loop
pygame.mixer_music.set_volume(0.01)

musica_activa = True

#---------------------------------------------- PERSONAJES ----------------------------------------------------------
jugador_imagen = pygame.image.load("./Assets/vayne2.png")
enemigo_imagen = pygame.image.load("./Assets/minion.png")
enemigo_imagen2 = pygame.image.load("./Assets/minion2.png")
fondo_imagen = pygame.transform.scale(pygame.image.load("./Assets/fondo.jpg"), PANTALLA_TAM)

personaje_principal = crear_bloque (alto=RECT_ALTO, ancho=RECT_ANCHO, imagen=jugador_imagen)
personaje_principal["rect"].center = CENTRO_PANTALLA
enemigo_1 = crear_bloque ( ancho = 60, alto = 60)
enemigo_1["rect"].top = 0

#---------------------------------------------- MONEDAS ----------------------------------------------------------
contador_monedas = 5
lista_monedas = []
cargar_monedas(lista_monedas, contador_monedas, enemigo_imagen)
puntaje_monedas = 0
fuente = pygame.font.Font(None, 32)
texto_Monedas = fuente.render(f"Puntaje: {puntaje_monedas}", True, NEGRO)
rect_puntaje = texto_Monedas.get_rect() # Obtengo el rectangulo de la surface
rect_puntaje.center = ((ANCHO // 2), 50)


contador_comer = 0

#----------------------------- CONFIGURO LA DIRECCIÓN -------------------------------------------------------------------------------------
mover_abajo = False
mover_arriba = False
mover_derecha = False
mover_izquierda = False

#--------------------------------------- EVENTOS --------------------------------------------------------------------------------
Nuevo_evento = pygame.USEREVENT + 1
pygame.time.set_timer(Nuevo_evento, 3000) #CADA 3 SEGUNDOS VA A LANZAR EL EVENTO

esta_Jugando = True

while esta_Jugando:
    reloj.tick(FPS)
    for evento in pygame.event.get(): 
        if evento.type == QUIT:
                esta_Jugando = False
                exit()  
        if evento.type == KEYDOWN:
            if evento.key == K_RIGHT or evento.key == K_d:
                mover_derecha = True
                mover_izquierda = False

            if evento.key == K_DOWN or evento.key == K_s:
                mover_abajo = True
                mover_arriba = False
                
            if evento.key == K_LEFT or evento.key == K_a:
                mover_izquierda = True
                mover_derecha = False

            if evento.key == K_UP or evento.key == K_w:
                mover_arriba = True
                mover_abajo = False

            if evento.key == K_m:
                if musica_activa:
                    pygame.mixer_music.pause()
                else:
                    pygame.mixer_music.unpause()

                musica_activa = not musica_activa
                
        if evento.type == KEYUP:
            if evento.key == K_RIGHT or evento.key == K_d:
                mover_derecha = False

            if evento.key == K_DOWN or evento.key == K_s:
                mover_abajo = False

            if evento.key == K_LEFT or evento.key == K_a:
                mover_izquierda = False

            if evento.key == K_UP or evento.key == K_w:
                mover_arriba = False

        
        if  evento.type == Nuevo_evento:
            lista_monedas.append(crear_bloque(randint(0,ANCHO - TAM_MONEDAS), randint(0, ALTO - TAM_MONEDAS), TAM_MONEDAS, TAM_MONEDAS, VIOLETA, 0,0, TAM_MONEDAS // 2))

        if evento.type == MOUSEBUTTONDOWN:
            if evento.button == 1:
                lista_monedas.append(crear_bloque(evento.pos[0] - TAM_MONEDAS // 2, evento.pos[1] - TAM_MONEDAS // 2, TAM_MONEDAS, TAM_MONEDAS, NEGRO, 0,0, TAM_MONEDAS // 2))
            if evento.button == 3:
                personaje_principal["rect"].center = (evento.pos[0],evento.pos[1])
                
#----- Movemos hasta que detectamos que choca ------------------------------------------------------
    if mover_arriba and personaje_principal["rect"].top >= 0:
        personaje_principal["rect"].top -= VELOCIDAD
    if mover_abajo and personaje_principal["rect"].bottom <= ALTO:
        personaje_principal["rect"].top += VELOCIDAD
    if mover_izquierda and personaje_principal["rect"].left >= 0:
        personaje_principal["rect"].left -= VELOCIDAD
    if mover_derecha and personaje_principal["rect"].right <= ANCHO:
        personaje_principal["rect"].left += VELOCIDAD


#----- Cargamos monedas y puntaje ------------------------------------------------------
    for moneda in lista_monedas[:]: #crea una nueva lista con los elementos. Desde el primero hasta el ultimo
        if detectar_colision(moneda["rect"], personaje_principal["rect"]):
            lista_monedas.remove(moneda)
            lista_monedas
            puntaje_monedas+= 1
            texto_Monedas = fuente.render(f"Puntaje: {puntaje_monedas}", True, NEGRO)
            contador_comer = 20 
            if  musica_activa:
                moneda_sonido.play()
        
    if len(lista_monedas) == 0:
        victoria_sonido.play()
        cargar_monedas(lista_monedas, contador_monedas, enemigo_imagen2)
    
        
    # if contador_comer >= 0:
    #     contador_comer -= 1
    #     personaje_principal["rect"].width = 120
    #     personaje_principal["rect"].height = 200
    # else:
    #     personaje_principal["rect"].width = RECT_ANCHO
    #     personaje_principal["rect"].height = RECT_ALTO



#----- Dibujo Pantalla ------------------------------------------------------
    PANTALLA.blit(fondo_imagen, (0,0))
    PANTALLA.blit(personaje_principal["imagen"], personaje_principal["rect"])
    PANTALLA.blit(texto_Monedas,rect_puntaje)
    for moneda in lista_monedas:
        if moneda["imagen"]:
            PANTALLA.blit(moneda["imagen"], moneda["rect"])
        else:
            pygame.draw.rect(PANTALLA,moneda["color"],moneda["rect"], moneda["borde"], moneda["radio"])
    


    # Acutalizo pantalla
    pygame.display.flip()
    

    
pygame.quit()