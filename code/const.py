# Fichier pour nos constantes
import pygame
from Building import *
pygame.init()

# font scene Pre_Menu
font0 = pygame.font.SysFont('JSL ANCIENT', 24, True)
# font scene Menu
font1 = pygame.font.SysFont('JSL ANCIENT', 48, True)

# foot scene New_game
font2 = pygame.font.SysFont('JSL ANCIENT', 46, True)

# foot scene Load_game
font_button = pygame.font.SysFont('JSL ANCIENT', 48, True)

font_save = pygame.font.SysFont('JSL ANCIENT', 48, True)

screen_height = 1024
screen_width = 768

MAP_SIZE = (40, 40)
TILE_SIZE = 60
event_types = {"LaunchGame": 100, "LoadName": 200}

scaleDelta = .5

LAND1A_078 = pygame.image.load("newland/Land1a_00078.png")
LAND1A_035 = pygame.image.load("newland/Land1a_00035.png")
LAND1A_036 = pygame.image.load("newland/Land1a_00036.png")
LAND1A_049 = pygame.image.load("newland/Land1a_00049.png")
LAND1A_057 = pygame.image.load("newland/Land1a_00057.png")
LAND1A_058 = pygame.image.load("newland/Land1a_00058.png")
LAND1A_060 = pygame.image.load("newland/Land1a_00060.png")
LAND1A_061 = pygame.image.load("newland/Land1a_00061.png")
LAND1A_120 = pygame.image.load("newland/Land1a_00120.png")
LAND1A_128 = pygame.image.load("newland/Land1a_00128.png")
LAND1A_133 = pygame.image.load("newland/Land1a_00133.png")
LAND1A_139 = pygame.image.load("newland/Land1a_00139.png")
LAND1A_143 = pygame.image.load("newland/Land1a_00143.png")
LAND1A_147 = pygame.image.load("newland/Land1a_00147.png")
LAND1A_148 = pygame.image.load("newland/Land1a_00148.png")
LAND1A_152 = pygame.image.load("newland/Land1a_00152.png")
LAND1A_159 = pygame.image.load("newland/Land1a_00159.png")
LAND1A_170 = pygame.image.load("newland/Land1a_00170.png")
LAND1A_171 = pygame.image.load("newland/Land1a_00171.png")
LAND1A_172 = pygame.image.load("newland/Land1a_00172.png")
LAND1A_173 = pygame.image.load("newland/Land1a_00120.png")
LAND1A_234 = pygame.image.load("newland/Land1a_00234.png")
LAND1A_235 = pygame.image.load("newland/Land1a_00235.png")
LAND1A_285 = pygame.image.load("newland/Land1a_00285.png")
LAND2A_095 = pygame.image.load("newland/Land2a_00095.png")
LAND3A_071 = pygame.image.load("newland/land3a_00071.png")
LAND3A_072 = pygame.image.load("newland/land3a_00072.png")
LAND3A_074 = pygame.image.load("newland/land3a_00074.png")
LAND3A_081 = pygame.image.load("newland/land3a_00081.png")
LAND3A_082 = pygame.image.load("newland/land3a_00082.png")

# fonction
HOUSE_01 = pygame.image.load("fonction_render/house/Housng1a_00045.png")

TEMP_TILE = {
    "house": HOUSE_01, "shovel": LAND1A_285
}
