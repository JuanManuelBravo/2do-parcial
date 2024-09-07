import pygame
from clases import *
from funciones_utiles import *
from funciones_programa import *
from ajustes_programa import *

pygame.init()

temporizador = temporizador()
clock = pygame.time.Clock()
racha = 0
best_racha = 0
tiempo_anterior = 0
pokemon_actual = 0
input_activo = False
pokemon_correcto = False
accion_dificultad = None
fin_juego = False
puntajes = leer_puntajes(archivo_csv)
lista_gen = inicializar_lista_gen(cuadros_gen)
bandera = True
bandera_inicio = True
user_font = ""

while bandera:
    
    while bandera_inicio:
        dibujar_interfaz_inicio(ventana, boton_jugar, boton_salir, dibujar_boton)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bandera_inicio = False
                bandera = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(event.pos):
                    bandera_inicio = False
                    limpiar_archivo_csv(archivo_csv)
                    cargar_pokemones(lista_gen)
                
                if boton_salir.collidepoint(event.pos):
                    bandera_inicio = False
                    bandera = False

    ventana.fill(GRIS)
    cuadro_azul = pygame.draw.rect(ventana, AZUL, (125,0,500,600))
    boton_no_se = ventana.blit(imagen_nose, (310,490))
    rect_idioma = ventana.blit(imagen_idiomas,(380,0))
    cuadro_input = pygame.draw.rect(ventana, color, input_rect)
    
    for evento in pygame.event.get():
        bandera = manejar_evento_cerrar(evento, bandera)

        if evento.type == pygame.KEYDOWN:
            if input_activo:
                if evento.key == pygame.K_BACKSPACE:
                    user_font = user_font[:-1]
                elif evento.key == pygame.K_RETURN:
                    if verificar_palabra(user_font.capitalize(), lista_gen[pokemon_actual].nombre_pokemon):
                        pokemon_correcto = True
                        user_font = ""
                        racha += 1
                        tiempo_anterior = temporizador.reiniciar()
                        guardar_puntaje(racha, lista_gen[pokemon_actual].nombre_pokemon, tiempo_anterior )
                        puntajes = leer_puntajes(archivo_csv)
                    else:
                        user_font = ""
                        fin_juego = True
                else:
                    user_font += evento.unicode

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            input_activo = manejar_activacion_input(evento, input_rect, input_activo)
            manejar_activacion_cuadros_gen(evento, cuadros_gen, lista_gen)
            for cuadro in cuadros_diff:    
                if cuadro["rect"].collidepoint(evento.pos):                
                    manejar_activacion_cuadros_diff(cuadros_diff,cuadro)
                    accion_dificultad = cambiar_difficultad(cuadro, evento, temporizador)
                    pokemon_actual = aumentar_indice(pokemon_actual, cuadro, evento, lista_gen)
                    
            if boton_no_se.collidepoint(evento.pos):
                pokemon_correcto = True
                temporizador.reiniciar()
            
            if reinicio.collidepoint(evento.pos):
                fin_juego = False
                pokemon_actual = reproducir_musica_y_actualizar_pokemon(lista_gen, pokemon_actual, temporizador)
                racha = 0

    dibujar_elementos_estaticos(ventana, cuadros_gen, cuadros_diff)
    dibujar_input_y_texto(ventana, user_font, fuente_input, cuadro_input, input_activo, color_activo, color_inactivo)
    mostrar_contadores(ventana, fuente_input, racha, tiempo_anterior, best_racha)
    mostrar_imagen_diff(accion_dificultad, ventana, fuente_input, lista_gen, pokemon_actual, temporizador, BLANCO)
    
    if pokemon_correcto:
        mostrar_idiomas(ventana, lista_gen, pokemon_actual )
        pokemon_actual = mostrar_imagen_color_y_esperar(ventana, lista_gen[pokemon_actual], 2, lista_gen, pokemon_actual)
        pokemon_correcto = False

    if fin_juego:
        limpiar_archivo_csv(archivo_csv)
        mostrar_final(ventana, fuente_titulo, racha)
        mostrar_puntajes(ventana, puntajes, fuente_input)
        if racha > best_racha:
            best_racha = racha

    clock.tick(30)
    pygame.display.update()

pygame.quit()