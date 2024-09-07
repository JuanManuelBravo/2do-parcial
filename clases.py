import pygame
import time
import json



class pokemon:
    """
    Clase para representar un Pokémon en un juego.
    """
    def __init__(self, nombre_imagen_color: str ,nombre_imagen_negro: str, nombre_pokemon: str, x: int, y: int):
        """
        

        Args:
            nombre_imagen_color (str): Nombre del archivo de imagen a color del Pokémon.
            nombre_imagen_negro (str): Nombre del archivo de imagen en blanco y negro del Pokémon.
            nombre_pokemon (str): Nombre del Pokémon.
            x (int): Posición horizontal inicial del Pokémon en la pantalla.
            y (int): Posición vertical inicial del Pokémon en la pantalla.
        """
        self.nombre_imagen_color = nombre_imagen_color
        self.nombre_imagen_negro = nombre_imagen_negro
        self.nombre_pokemon = nombre_pokemon
        self.x = x
        self.y = y
        self.idiomas = {}
    
    
    def crear_imagen_color(self, ventana, escala: float):
        """
        Carga la imagen a color del Pokémon, la escala y la dibuja en la ventana.


        Args:
            ventana (pygame.Surface): La ventana de Pygame donde se dibujará la imagen.
            escala (float): El factor de escala para ajustar el tamaño de la imagen.
        """
        img = pygame.image.load(self.nombre_imagen_color)
        img = pygame.transform.scale(img, (int(img.get_width() * escala), int(img.get_height() * escala)))        
        rect = img.get_rect()
        rect.center = (self.x, self.y)
        
        ventana.blit(img, rect.center)
    
    
    def crear_imagen_negro(self, ventana, escala: float):
        """
        Carga la imagen en blanco y negro del Pokémon, la escala y la dibuja en la ventana.


        Args:
            ventana (pygame.Surface): La ventana de Pygame donde se dibujará la imagen.
            escala (float): El factor de escala para ajustar el tamaño de la imagen.
        """
        img = pygame.image.load(self.nombre_imagen_negro)
        img = pygame.transform.scale(img, (int(img.get_width() * escala), int(img.get_height() * escala)))
        rect = img.get_rect()
        rect.center = (self.x, self.y)
        
        ventana.blit(img, rect.center)


    def aplicar_pixelado_y_escalar(self, ventana, tamaño_pixel, escala_final):
        """
        Aplica pixelado y escala a la imagen en blanco y negro del Pokémon y la dibuja en la ventana.

        Args:
        ventana (pygame.Surface): La ventana de Pygame donde se dibujará la imagen.
        tamaño_pixel (int): Tamaño del pixel para aplicar el efecto de pixelado.
        escala_final (float): El factor de escala final para ajustar el tamaño de la imagen pixelada.
        """
        img = pygame.image.load(self.nombre_imagen_negro)
        imagen_pequeña = pygame.transform.scale(img, (img.get_width() // tamaño_pixel, img.get_height() // tamaño_pixel))
        imagen_pixeleada = pygame.transform.scale(imagen_pequeña, (img.get_width(), img.get_height()))
        img_final = pygame.transform.scale(imagen_pixeleada, (int(img.get_width() * escala_final), int(img.get_height() * escala_final)))
        rect = img_final.get_rect()
        rect.center = (self.x, self.y)
        
        ventana.blit(img_final, rect.center)


    def cargar_nombres_idiomas(self, ruta_json: str):
        """
        Carga los nombres del Pokémon en diferentes idiomas desde un archivo JSON.


        Args:
            ruta_json (str): Ruta al archivo JSON que contiene los nombres en diferentes idiomas.
        """
        with open(ruta_json, 'r') as archivo:
            datos = json.load(archivo)
            if self.nombre_pokemon in datos:
                self.idiomas = datos[self.nombre_pokemon]
            else:
                print(f"No se encontró información para {self.nombre_pokemon}")


    def obtener_nombres_idiomas(self):
        """
        Obtiene el diccionario de nombres del Pokémon en diferentes idiomas.

        Returns:
            dict: Diccionario con los nombres del Pokémon en diferentes idiomas.
        """
        return self.idiomas




class temporizador:
    def __init__(self):
        """
        Inicializa un objeto temporizador con el tiempo de inicio actual en milisegundos.
        """
        self.inicio_ticks = pygame.time.get_ticks()


    def reiniciar(self):
        """
        Reinicia el temporizador y devuelve el tiempo transcurrido desde el reinicio en segundos.

        Returns:
            float: Tiempo transcurrido desde el reinicio en segundos.
        """
        tiempo_anterior = (pygame.time.get_ticks() - self.inicio_ticks) / 1000
        self.inicio_ticks = pygame.time.get_ticks()
        
        return tiempo_anterior


    def mostrar(self, ventana, fuente, x, y, color):
        """
        Muestra el tiempo transcurrido en segundos en la ventana de Pygame en la posición especificada.

        Args:
            ventana (pygame.Surface): Ventana de Pygame donde se mostrará el temporizador.
            fuente (pygame.font.Font): Fuente a utilizar para renderizar el texto del temporizador.
            x (int): Coordenada x de la posición donde se mostrará el temporizador.
            y (int): Coordenada y de la posición donde se mostrará el temporizador.
            color (tuple): Color del texto en formato RGB (e.g., (255, 0, 0) para rojo).

        Returns:
            float: Tiempo transcurrido en segundos.
        """
        segundos = (pygame.time.get_ticks() - self.inicio_ticks) / 1000
        segundos_str = str(segundos)
        contador = fuente.render(segundos_str, 0, color)
        ventana.blit(contador, (x, y))

        return segundos

