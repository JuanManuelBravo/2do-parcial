import pygame

from clases import *

pygame.init()
pygame.mixer.init()

pygame.mixer_music.load(r"recursos\musica_fondo.mp3")
pygame.mixer_music.play(-1)

#####AJUSTES_PANTALLA#####
alto_ventana = 600
ancho_ventana = 800
ventana = pygame.display.set_mode((ancho_ventana,alto_ventana))
titulo_programa = "ADIVINA EL POKEMON"
pygame.display.set_caption(titulo_programa)

#######BOTONES_INICIO#######
ancho_boton = 200
alto_boton = 50
boton_jugar = pygame.Rect(ancho_ventana // 2 - ancho_boton // 2, 200, ancho_boton, alto_boton)
boton_salir = pygame.Rect(ancho_ventana // 2 - ancho_boton // 2, 300, ancho_boton, alto_boton)

#####COLORES#####
GRIS_OSCURO = (50,55,76)
GRIS = (212,212,220)
GRIS_GEN = (89,109,134)
AZUL = (52,148,211)
BLANCO = (255,255,255)
NEGRO = (0,0,0)
VERDE = (0, 255, 255)

#####FUENTES#####
fuente_input = pygame.font.SysFont("arial",20)
fuente_titulo = pygame.font.SysFont("Comic Sans MS",34)
fuente_idiomas = pygame.font.SysFont("Absender",20)

#####RECT_INPUT######
input_rect = pygame.Rect(240, 450, 275, 35)

#######CARGAs_DE_IMAGENES_PANTALLA#################################
imagen_nose = pygame.image.load(r"recursos\NO_SE.PNG")

imagen_idiomas = pygame.image.load(r"recursos\imagen_idiomas.png")
imagen_idiomas = pygame.transform.scale(imagen_idiomas, (int(imagen_idiomas.get_width() * 0.55), int(imagen_idiomas.get_height() * 0.5)))

imagen_espera = pygame.image.load(r"recursos\imagen_espera.PNG")
imagen_espera = pygame.transform.scale(imagen_espera, (int(imagen_espera.get_width() * 0.55), int(imagen_espera.get_height() * 0.5)))

imagen_inicio = pygame.image.load(r"recursos\imagen_inicio.png")

reinicio = pygame.Rect(550, 200, 200, 50)
texto_reinicio = fuente_titulo.render("Reiniciar",True, BLANCO)


####AJUSTES_INPUT#####
color_activo = GRIS
color_inactivo = BLANCO
color = color_inactivo


######MATRIZ#########
matriz_colores = [
    [GRIS_OSCURO, GRIS_OSCURO], 
    [GRIS_OSCURO, GRIS_OSCURO]]


######POKEMONES######
lista_gen_uno = [
    pokemon(r"imagenes\pokemones\GEN1\Charmander.jpg",r"imagenes\pokemones\GEN1\GEN1_OCULTO\charmander_negro.png","Charmander",250,155),
    pokemon(r"imagenes\pokemones\GEN1\Abra.jpg",r"imagenes\pokemones\GEN1\GEN1_OCULTO\Abra.png","Abra",250,155),
    pokemon(r"imagenes\pokemones\GEN1\bulbasaur.jpg",r"imagenes\pokemones\GEN1\GEN1_OCULTO\bulbasur.png","Bulbasur",250,155),
    pokemon(r"imagenes\pokemones\GEN1\Gastly.jpg",r"imagenes\pokemones\GEN1\GEN1_OCULTO\Gastly.png","Gastly",250,155),
    pokemon(r"imagenes\pokemones\GEN1\Gengar.jpg",r"imagenes\pokemones\GEN1\GEN1_OCULTO\Gengar.png","Gengar",250,155),
    pokemon(r"imagenes\pokemones\GEN1\hitmonchan.jpg",r"imagenes\pokemones\GEN1\GEN1_OCULTO\Hitmonchan.png","Hitmonchan",250,155),
    pokemon(r"imagenes\pokemones\GEN1\Pikachu.jpg",r"imagenes\pokemones\GEN1\GEN1_OCULTO\Pikachu.png","Pikachu",250,155),
    pokemon(r"imagenes\pokemones\GEN1\Pidgey.jpg",r"imagenes\pokemones\GEN1\GEN1_OCULTO\pidgey.png","Pidgey",250,155),
    pokemon(r"imagenes\pokemones\GEN1\Voltorb.jpg",r"imagenes\pokemones\GEN1\GEN1_OCULTO\Voltorb.png","Voltorb",250,155),
    pokemon(r"imagenes\pokemones\GEN1\Vulpix.jpg",r"imagenes\pokemones\GEN1\GEN1_OCULTO\Vulpix.png","Vulpix",250,155),]


list_gen_dos = [ 
    pokemon(r"imagenes\pokemones\GEN2\Celebi.jpg",r"imagenes\pokemones\GEN2\GEN2_OCULTO\Celebi_oculto.png","Celebi",250,155),
    pokemon(r"imagenes\pokemones\GEN2\Chikorita.jpg",r"imagenes\pokemones\GEN2\GEN2_OCULTO\Chikorita_oculto.png","Chikorita",250,155),
    pokemon(r"imagenes\pokemones\GEN2\Cyndaquil.jpg",r"imagenes\pokemones\GEN2\GEN2_OCULTO\Cyndaquil_oculto.png","Cyndaquil",250,155),
    pokemon(r"imagenes\pokemones\GEN2\Entei.jpg",r"imagenes\pokemones\GEN2\GEN2_OCULTO\Entei_oculto.png","Entei",250,155),
    pokemon(r"imagenes\pokemones\GEN2\Marill.jpg",r"imagenes\pokemones\GEN2\GEN2_OCULTO\Marill_oculto.png","Marill",250,155),
    pokemon(r"imagenes\pokemones\GEN2\Pichu.jpg",r"imagenes\pokemones\GEN2\GEN2_OCULTO\Pichu_oculto.png","Pichu",250,155),
    pokemon(r"imagenes\pokemones\GEN2\Scizor.jpg",r"imagenes\pokemones\GEN2\GEN2_OCULTO\Scizor_oculto.png","Scizor",250,155),
    pokemon(r"imagenes\pokemones\GEN2\Skarmory.jpg",r"imagenes\pokemones\GEN2\GEN2_OCULTO\Skarmory_oculto.png","Skarmory",250,155),
    pokemon(r"imagenes\pokemones\GEN2\Togepi.jpg",r"imagenes\pokemones\GEN2\GEN2_OCULTO\Togepi_oculto.png","Togepi",250,155),
    pokemon(r"imagenes\pokemones\GEN2\Totodile.jpg",r"imagenes\pokemones\GEN2\GEN2_OCULTO\Totodile_oculto.png","Totodile",250,155),]


list_gen_tres = [ 
    pokemon(r"imagenes\pokemones\GEN3\Absol.jpg",r"imagenes\pokemones\GEN3\1.png","Absol",250,155),
    pokemon(r"imagenes\pokemones\GEN3\Bagon.jpg",r"imagenes\pokemones\GEN3\2.png","Bagon",250,155),
    pokemon(r"imagenes\pokemones\GEN3\Makuhita.jpg",r"imagenes\pokemones\GEN3\3.png","Makuhita",250,155),
    pokemon(r"imagenes\pokemones\GEN3\Poochyena.jpg",r"imagenes\pokemones\GEN3\4.png","Poochyena",250,155),
    pokemon(r"imagenes\pokemones\GEN3\Ralts.jpg",r"imagenes\pokemones\GEN3\5.png","Ralts",250,155),
    pokemon(r"imagenes\pokemones\GEN3\Sableye.jpg",r"imagenes\pokemones\GEN3\6.png","Sableye",250,155),
    pokemon(r"imagenes\pokemones\GEN3\Slaking.jpg",r"imagenes\pokemones\GEN3\7.png","Slaking",250,155),
    pokemon(r"imagenes\pokemones\GEN3\Torchic.jpg",r"imagenes\pokemones\GEN3\8.png","Torchic",250,155),
    pokemon(r"imagenes\pokemones\GEN3\Torkoal.jpg",r"imagenes\pokemones\GEN3\9.png","Torkoal",250,155),
    pokemon(r"imagenes\pokemones\GEN3\Treecko.jpg",r"imagenes\pokemones\GEN3\10.png","Treecko",250,155),]


######LISTAS_GEN#########
cuadros_gen = [
    {"rect": pygame.Rect(25,100,100,25), "activo": True, "color_inactivo": GRIS_OSCURO, "color_activo": BLANCO,"accion": lista_gen_uno},
    {"rect": pygame.Rect(25,126,100,25), "activo": False, "color_inactivo": GRIS_OSCURO, "color_activo": BLANCO,"accion": list_gen_dos},
    {"rect": pygame.Rect(25,152,100,25), "activo": False, "color_inactivo": GRIS_OSCURO, "color_activo": BLANCO,"accion": list_gen_tres},
    ]


cuadros_diff = [ 
    {"rect": pygame.Rect(25,250,90,25), "activo": False, "color_inactivo": GRIS_OSCURO, "color_activo": BLANCO,"accion": "color"},
    {"rect": pygame.Rect(25,277,90,25), "activo": False, "color_inactivo": GRIS_OSCURO, "color_activo": BLANCO,"accion": "negro"},
    {"rect": pygame.Rect(25,303,90,25), "activo": False, "color_inactivo": GRIS_OSCURO, "color_activo": BLANCO,"accion": "pixeleado"}]

######TEXTOS_GENERACION######
textos_generacion = ["Gen 1", "Gen 2", "Gen 3"]

######TEXTOS_DIFICULTAD########
textos_dificultad = ["Facil", "Medio", "Dificil"]

titulos = [
    ("¿Quién es ese Pokemon?", BLANCO, 180, 100),
    ("RACHA", GRIS_OSCURO, 650, 100),
    ("TIEMPO", GRIS_OSCURO, 650, 255) 
]




