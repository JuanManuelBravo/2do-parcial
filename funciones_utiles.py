import pygame
import time
import random


def mostrar_textos_en_ventana(ventana, textos, color, inicio_x, inicio_y, incremento, nombre_fuente, tamaño_fuente, incremento_en_x = True ):
    """_summary_ 
    Esta funcion muestra los textos en pantalla

    Args:
        ventana (surf): Recibe una superficie
        textos (string): Recibe un str
        color (tupla): Recibe una tupla
        inicio_x (int)): recibe int
        inicio_y (int): recibe int
        incremento (type): descriion
        nombre_fuente (font): Recibe una fuente
        tama (type): Recibe un int
        incremento_en_x (bool, optional): Recibe un bool
    """
    fuente = pygame.font.SysFont(nombre_fuente, tamaño_fuente)
    x = inicio_x
    y = inicio_y
    for texto in textos:
        texto_renderizado = fuente.render(texto, True, color)
        ventana.blit(texto_renderizado, (x, y))
        if incremento_en_x:
            x += incremento
        else:
            y += incremento


def dibujar_titulos(ventana, texto, fuente, color, referencia_x, referencia_y):
    """
    Dibuja un título en la ventana especificada.

    Args:
        ventana (pygame.Surface): La ventana de Pygame donde se dibujará el título.
        texto (str): El texto que se mostrará como título.
        fuente (pygame.font.Font): La fuente a utilizar para el título.
        color (tuple): El color del texto en formato RGB (e.g., (255, 0, 0) para rojo).
        referencia_x (int): La posición horizontal (en píxeles) donde se iniciará el título.
        referencia_y (int): La posición vertical (en píxeles) donde se iniciará el título.
    """
    texto_titulo = fuente.render(texto, True, color)
    ventana.blit(texto_titulo, (referencia_x, referencia_y))


def crear_titulos(ventana, fuente_titulo, titulos):
    """
    Crea y dibuja los títulos en la ventana especificada.

    Args:
        ventana: La ventana de Pygame donde se dibujarán los títulos.
        fuente_titulo: La fuente a utilizar para los títulos.
        titulos: Una lista de tuplas donde cada tupla contiene (texto, color, referencia_x, referencia_y).
    """
    for titulo in titulos:
        if len(titulo) >= 4:
            texto = titulo[0]
            color = titulo[1]
            referencia_x = titulo[2]
            referencia_y = titulo[3]
            dibujar_titulos(ventana, texto, fuente_titulo, color, referencia_x, referencia_y)
        else:
            print("error")


def mostrar_contador(ventana, fuente, contador, color, posicion):
    """_summary_
    esta funcion muestra el contador

    Args:
        ventana (surf): Recibe una superficie
        fuente (font): Recibe una fuente
        contador (type): description
        color (tupla): Recibe una tupla
        posicion (tupla): Recibe una tupla
    """
    contador_str = str(contador)
    contador_str = fuente.render(contador_str,0,color)
    ventana.blit(contador_str, posicion )


def dibujar_rectangulos(ventana, matriz, x, y, ancho, alto, espacio):
    """
    Dibuja una matriz de rectángulos en la ventana de pygame.

    Args:
        ventana (pygame.Surface): La ventana de pygame donde se dibujarán los rectángulos.
        matriz (list of list of tuple): Una matriz donde cada elemento representa el color RGB del rectángulo.
        x (int): La coordenada x del punto de inicio para dibujar la matriz de rectángulos.
        y (int): La coordenada y del punto de inicio para dibujar la matriz de rectángulos.
        ancho (int): El ancho en píxeles de cada rectángulo.
        alto (int): La altura en píxeles de cada rectángulo.
        espacio (int): El espacio en píxeles entre cada rectángulo.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    
    for i in range(filas):
        for j in range(columnas):
            color = matriz[i][j]
            cuadro = pygame.Rect(x + j * (ancho + espacio), y + i * (alto + espacio), ancho, alto)
            pygame.draw.rect(ventana, color, cuadro)


def manejar_activacion_input(evento, input_rect, activo):
    """
    
    Maneja la activación/desactivación de un input basado en la interacción del usuario.

    Args:
        evento (pygame.event.Event): El evento de Pygame que se está manejando.
        input_rect (pygame.Rect): El rectángulo del input que se quiere activar/desactivar.
        activo (bool): El estado actual de activación del input.

    Returns:
        bool: El nuevo estado de activación del input después de manejar el evento.
    """
    nuevo_estado = activo
    if input_rect.collidepoint(evento.pos):
        nuevo_estado = not activo
    else:
        nuevo_estado = False
    return nuevo_estado


def renderizar_texto_para_ajustar(texto, fuente, color, rect, superficie):
    """
    Renderiza un texto con la fuente y color dados, ajustando su tamaño para que se ajuste al rectángulo especificado.

    Args:
        texto (str): Texto a renderizar.
        fuente: Objeto fuente de pygame u otra biblioteca de renderizado de texto.
        color: Color del texto representado como tupla RGB o RGBA.
        rect (pygame.Rect): Rectángulo donde se ajustará el texto.
        superficie: Superficie donde se blit (pinta) el texto renderizado.
    """
    texto_surface = fuente.render(texto, True, color)
    while texto_surface.get_width() > rect.width - 5:
        texto = texto[:-1]
        texto_surface = fuente.render(texto, True, color)
        
    superficie.blit(texto_surface, (rect.x + 2.5, rect.y + 2.5))
    

def dibujar_boton(rect, texto, color, ventana):
    pygame.draw.rect(ventana, color, rect)
    fuente = pygame.font.Font(None, 36)
    texto_renderizado = fuente.render(texto, True, (255, 255, 255))
    text_rect = texto_renderizado.get_rect(center = rect.center)
    ventana.blit(texto_renderizado, text_rect)

verificar_palabra = lambda user_input, nombre_correcto: user_input == nombre_correcto

