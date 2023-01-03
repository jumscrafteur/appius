# Fichier pour nos constantes
import pygame

pygame.init()

#font scene Pre_Menu
font0= pygame.font.SysFont('JSL ANCIENT', 24, True)
#font scene Menu
font1 = pygame.font.SysFont('JSL ANCIENT', 48, True)

#foot scene New_game
font2 = pygame.font.SysFont('JSL ANCIENT', 46, True)

#foot scene Load_game
font_button = pygame.font.SysFont('JSL ANCIENT', 48, True)

font_save = pygame.font.SysFont('JSL ANCIENT', 48, True)

screen_height = 1024
screen_width = 768

MAP_SIZE = (40, 40)

event_types = {"LaunchGame": 100, "LoadName": 200}
