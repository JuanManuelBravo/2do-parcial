import pygame
import time
import random

from ajustes_programa import *
from archivos_pokemon import *
from funciones_utiles import *

def mostrar_imagen_diff(accion, ventana, fuente, lista_gen, indice_actual, temporizador, color):
    """
    Muestra una imagen modificada según la acción especificada.

    Args:
        accion (str): Acción a realizar sobre la imagen. Puede ser "1", "2" o "3".
        ventana: La ventana donde se muestra la imagen.
        fuente: La fuente utilizada para mostrar el temporizador.
        lista_gen (list): Lista de objetos que contienen las imágenes generadas.
        indice_actual (int): Índice de la imagen actual dentro de lista_gen.
        temporizador: Objeto temporizador que muestra el tiempo transcurrido.
        color: Color del texto del temporizador.

    """
    if accion == "1":
        lista_gen[indice_actual].crear_imagen_color(ventana, 1.05)
    elif accion == "2":
        lista_gen[indice_actual].crear_imagen_negro(ventana, 0.3)
    elif accion == "3":
        lista_gen[indice_actual].aplicar_pixelado_y_escalar(ventana, 25, 0.3)
    
    temporizador.mostrar(ventana, fuente, 655, 220, color)


def mostrar_imagen_color_y_esperar(ventana, pokemon, segundos, lista_gen, pokemon_actual):
    """
    Muestra la imagen en color de un Pokémon en la ventana y espera el número de segundos especificado.

    Args:
        ventana: La ventana de pygame donde se muestra la imagen.
        pokemon: Objeto que representa al Pokémon con métodos para crear una imagen en color.
        segundos (float): Número de segundos que se espera después de mostrar la imagen.
        lista_gen (list): Lista que contiene los Pokémon de la generación actual.
        pokemon_actual (int): Índice del Pokémon actual en la lista de la generación.

    Returns:
        int: El nuevo índice del Pokémon actual después de la espera.
    """
    pokemon.crear_imagen_color(ventana, 1.2)
    pygame.display.update()
    time.sleep(segundos)
    pokemon_actual = (pokemon_actual + 1) % len(lista_gen)
    
    return pokemon_actual


def dibujar_input(ventana, input, activo, color_activo, color_inactivo):
    """
    Dibuja un cuadro de entrada (input) en la ventana de pygame según su estado activo o inactivo.

    Args:
        ventana: La ventana de pygame donde se dibuja el cuadro de entrada.
        input (pygame.Rect): Rectángulo que define la posición y tamaño del cuadro de entrada.
        activo (bool): Indica si el cuadro de entrada está activo o no.
        color_activo (tuple): Color del cuadro de entrada cuando está activo, representado como una tupla (R, G, B).
        color_inactivo (tuple): Color del cuadro de entrada cuando está inactivo, representado como una tupla (R, G, B).
    """
    if activo:
        color = color_activo
    else:
        color = color_inactivo
    
    pygame.draw.rect(ventana,color,input)


def dibujar_botones(ventana, conjuntos_de_cuadros):
    """
    Dibuja múltiples conjuntos de cuadros en la ventana de pygame según su estado activo o inactivo.

    Args:
        ventana: La ventana de pygame donde se dibujan los cuadros.
        conjuntos_de_cuadros (list): Lista de listas de diccionarios. Cada lista interior contiene diccionarios que representan los cuadros con las siguientes claves:
            - "activo" (bool): Indica si el cuadro está activo o no.
            - "color_activo" (tuple): Color del cuadro cuando está activo, representado como una tupla (R, G, B).
            - "color_inactivo" (tuple): Color del cuadro cuando está inactivo, representado como una tupla (R, G, B).
            - "rect" (pygame.Rect): Rectángulo que define la posición y tamaño del cuadro en la ventana.
    """
    for conjunto in conjuntos_de_cuadros:
        for cuadro in conjunto:
            if cuadro["activo"]:
                color = cuadro["color_activo"]
            else:
                color = cuadro["color_inactivo"]
            
            pygame.draw.rect(ventana, color, cuadro["rect"])


def contar_elementos_activos(cuadros):
    count = 0
    for cuadro in cuadros:
        if cuadro["activo"]:
            count += 1
    return count


def agregar_acciones(lista_gen, acciones):
    lista_gen.extend(acciones)


def remover_acciones(lista_gen, acciones):
    for accion in acciones:
        if accion in lista_gen:
            lista_gen.remove(accion)


def manejar_activacion_cuadros_gen(evento, cuadros, lista_gen):
    for cuadro in cuadros:
        if cuadro["rect"].collidepoint(evento.pos):
            if cuadro["activo"]:
                if contar_elementos_activos(cuadros) > 1:
                    cuadro["activo"] = False
                    remover_acciones(lista_gen, cuadro["accion"])
                    print("remuevo")
            else:
                cuadro["activo"] = True
                agregar_acciones(lista_gen, cuadro["accion"])
                print("agrego")
                cargar_pokemones(lista_gen)
            random.shuffle(lista_gen)
            break


def manejar_activacion_cuadros_diff(cuadros_diff, cuadro):
    if not cuadro["activo"]:
        for cuadros in cuadros_diff:
            cuadros["activo"] = False
        cuadro["activo"] = True
        print("activo cuadro diff")




def cambiar_difficultad(cuadro, evento, temporizador) -> str:
    accion_actual = None
    if cuadro["rect"].collidepoint(evento.pos) and cuadro["activo"]:
        temporizador.reiniciar()
        if cuadro["accion"] == "color":
            accion_actual = "1"
        elif cuadro["accion"] == "negro":
            accion_actual = "2"
        elif cuadro["accion"] == "pixeleado":
            accion_actual = "3"
    
    return accion_actual


def aumentar_indice(indice_actual, cuadro, evento, lista_gen):
    if cuadro["rect"].collidepoint(evento.pos) and cuadro["activo"]:
        indice_actual = (indice_actual + 1) % len(lista_gen)
        
    return indice_actual


def inicializar_lista_gen(cuadros):
    random.shuffle(lista_gen_uno)
    random.shuffle(list_gen_dos)
    random.shuffle(list_gen_tres)
    lista_gen = []
    for cuadro in cuadros:
        if cuadro["activo"]:
            lista_gen.extend(cuadro["accion"])
    
    return lista_gen


def mostrar_final(ventana, fuente, contador):
    """
    Muestra la pantalla final del juego con el contador de respuestas correctas.

    Args:
        ventana: La ventana de pygame donde se muestra el mensaje final.
        fuente: Fuente utilizada para renderizar el texto del mensaje.
        contador (int): Número de respuestas correctas obtenidas durante el juego.

    """
    pygame.mixer_music.stop()
    ventana.fill(NEGRO)
    mensaje = f"Juego terminado. Respuestas correctas: {contador}"
    texto = fuente.render(mensaje, True, BLANCO)
    ventana.blit(texto, (50, 100))
    pygame.draw.rect(ventana, AZUL, reinicio)
    ventana.blit(texto_reinicio,( reinicio.x + 25, reinicio.y + 3) )


def manejar_evento_cerrar(evento, bandera):
    if evento.type == pygame.QUIT:
        bandera = False
    return bandera

def reproducir_musica_y_actualizar_pokemon(lista_gen, pokemon_actual, temporizador):
    """
    Reproduce la música en bucle, actualiza el índice del Pokémon actual y reinicia el temporizador.

    Args:
        musica (pygame.mixer.Sound): Objeto de música de pygame que se reproducirá en bucle.
        lista_gen (list): Lista que contiene los Pokémon de la generación actual.
        pokemon_actual (int): Índice del Pokémon actual en la lista de la generación.
        temporizador (Timer): Objeto de temporizador que tiene un método `reiniciar`.

    Returns:
        int: El nuevo índice del Pokémon actual después de la actualización.
    """
    pygame.mixer_music.play(-1)
    pokemon_actual = (pokemon_actual + 1) % len(lista_gen)
    temporizador.reiniciar()
    
    return pokemon_actual

def dibujar_interfaz_inicio(ventana, boton_jugar, boton_salir, funcion):
    """
    Dibuja la interfaz de inicio en la ventana especificada.

    Args:
    - ventana (Surface): La ventana de Pygame donde se dibujará la interfaz.
    - boton_jugar (Rect): El rectángulo del botón "Jugar".
    - boton_salir (Rect): El rectángulo del botón "Salir".
    - funcion (func): Función utilizada para dibujar los botones.

    """
    ventana.fill(GRIS_OSCURO)
    funcion(boton_jugar, "Jugar", AZUL, ventana)
    funcion(boton_salir, "Salir", AZUL, ventana)
    pygame.display.update()

def dibujar_elementos_estaticos(ventana, cuadros_gen, cuadros_diff):
    """
    Dibuja elementos estáticos en la ventana del juego.

    Args:
    - ventana (Surface): La ventana de Pygame donde se dibujarán los elementos.
    - cuadros_gen (list): Lista de rectángulos para los cuadros de generación.
    - cuadros_diff (list): Lista de diccionarios con información de cuadros de dificultad.

    """
    dibujar_botones(ventana, [cuadros_gen, cuadros_diff])
    dibujar_rectangulos(ventana, matriz_colores, 650, 150, 60, 50, 5)
    crear_titulos(ventana, fuente_titulo, titulos)
    mostrar_textos_en_ventana(ventana, textos_generacion, GRIS_GEN, 40, 102, 26, "Cambria", 15, False)
    mostrar_textos_en_ventana(ventana, textos_dificultad, GRIS_GEN, 40, 252, 26, "Cambria", 15, False)

def dibujar_input_y_texto(ventana, user_font, fuente_input, cuadro_input, input_activo, color_activo, color_inactivo):
    """
    Dibuja un campo de entrada de texto en la ventana y renderiza el texto ingresado.

    Args:
    - ventana (Surface): La ventana de Pygame donde se dibujará el campo de entrada.
    - user_font (str): El texto ingresado por el usuario.
    - fuente_input (Font): La fuente de Pygame para el texto de entrada.
    - cuadro_input (Rect): El rectángulo del campo de entrada.
    - input_activo (bool): Indica si el campo de entrada está activo o no.
    - color_activo (tuple): Color del borde cuando el campo está activo.
    - color_inactivo (tuple): Color del borde cuando el campo está inactivo.

    """
    dibujar_input(ventana, cuadro_input, input_activo, color_activo, color_inactivo)
    renderizar_texto_para_ajustar(user_font, fuente_input, NEGRO, cuadro_input, ventana)

def mostrar_contadores(ventana, fuente_input, racha, tiempo_anterior, best_racha):
    """
    Muestra contadores en la ventana para la racha actual, tiempo anterior y mejor racha.

    Args:
    - ventana (Surface): La ventana de Pygame donde se mostrarán los contadores.
    - fuente_input (Font): La fuente de Pygame para el texto de los contadores.
    - racha (int): La racha actual de Pokémon correctos.
    - tiempo_anterior (float): El tiempo anterior registrado.
    - best_racha (int): La mejor racha registrada.
    """
    mostrar_contador(ventana, fuente_input, racha, BLANCO, (675, 160))
    mostrar_contador(ventana, fuente_input, tiempo_anterior, BLANCO, (725, 220))
    mostrar_contador(ventana, fuente_input, best_racha, BLANCO, (735, 160))
    

