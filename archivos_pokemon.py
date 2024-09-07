import pygame
import csv
from ajustes_programa import *
from clases import *


def cargar_pokemones(lista_gen):
    """
    Carga los nombres de los Pokémon en diferentes idiomas desde un archivo JSON para cada Pokémon en la lista.

    Args:
        lista_gen (list): Lista de objetos de tipo Pokémon sobre los cuales se cargarán los nombres en diferentes idiomas.
    """
    for pokemon in lista_gen:
        pokemon.cargar_nombres_idiomas("pokemones.json")


def mostrar_idiomas(ventana, lista_gen, indice_actual ):
    """
    Muestra los nombres de los Pokémon en diferentes idiomas en la ventana de Pygame.

    Args:
        ventana (pygame.Surface): Ventana de Pygame donde se mostrarán los nombres de los Pokémon.
        lista_gen (list): Lista de objetos de tipo Pokémon de donde se obtendrán los nombres en diferentes idiomas.
        indice_actual (int): Índice del Pokémon actual en la lista de Pokémon.
    """
    nombres_idiomas = lista_gen[indice_actual].obtener_nombres_idiomas()
    x = 155
    for idioma, nombre in nombres_idiomas.items():
        text = fuente_idiomas.render(f"{idioma} : {nombre}", True, NEGRO)
        ventana.blit(text, (x, 550))
        x += 120


archivo_csv = "puntajes_pokemon.csv"

def guardar_puntaje(numero_racha, pokemon_adivinado, tiempos):
    """
    Guarda un puntaje en un archivo CSV.

    Args:
        numero_racha (int): Número de la racha o intento en el juego.
        pokemon_adivinado (str): Nombre del Pokémon adivinado.
        tiempos (float): Tiempo en segundos que tomó adivinar el Pokémon.
        archivo_csv (str): Ruta al archivo CSV donde se guardará el puntaje.
    """
    with open(archivo_csv, "a", newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([numero_racha, pokemon_adivinado, tiempos])


def leer_puntajes(archivo_csv):
    """
    Lee los puntajes almacenados en un archivo CSV.

    Args:
        archivo_csv (str): Ruta al archivo CSV desde donde se leerán los puntajes.

    Returns:
        list: Lista de listas, donde cada sublista representa un puntaje guardado en el archivo CSV.
    """
    with open(archivo_csv, mode='r') as archivo:
        reader = csv.reader(archivo)
        puntajes = list(reader)

    return puntajes


def mostrar_puntajes(ventana, puntajes, fuente):
    """
    Muestra los puntajes en una ventana de Pygame.

    Args:
        ventana (pygame.Surface): Ventana de Pygame donde se mostrarán los puntajes.
        puntajes (list): Lista de puntajes, donde cada puntaje es una lista con al menos tres elementos (número de racha, Pokémon adivinado, tiempo).
        fuente (pygame.font.Font): Fuente a utilizar para renderizar los puntajes en la ventana.

    """
    y = 250
    for puntaje in puntajes:
        if len(puntaje) >= 3:
            texto = f"racha:{puntaje[0]} --- pokemon: {puntaje[1]} --- tiempo adivinado: {puntaje[2]}"
            texto_renderizado = fuente.render(texto, True, (255, 255, 255))
            ventana.blit(texto_renderizado, (50, y))
            y += 40
        else:
            print("error")


def limpiar_archivo_csv(archivo_csv):
    with open(archivo_csv, "w", newline='') as archivo:
        pass
