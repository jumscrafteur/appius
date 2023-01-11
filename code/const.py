# Fichier pour nos constantes
import pygame
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
TILE_SIZE = 40
event_types = {"LaunchGame": 100, "LoadName": 200}

scaleDelta = TILE_SIZE/60

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
LAND2A_095 = pygame.image.load("newland/Land2a_00095.png")
LAND3A_071 = pygame.image.load("newland/land3a_00071.png")
LAND3A_072 = pygame.image.load("newland/land3a_00072.png")
LAND3A_074 = pygame.image.load("newland/land3a_00074.png")
LAND3A_081 = pygame.image.load("newland/land3a_00081.png")
LAND3A_082 = pygame.image.load("newland/land3a_00082.png")


GRASS_IMAGE = pygame.image.load("newland/Land1a_00285.png")

#
TEMP_BUILD = pygame.image.load("fonction_render/house/Land2a_00001.png")
# fonction
HOUSE_01 = pygame.image.load(
    "fonction_render/house/Housng1a_00045.png")
ROAD = pygame.image.load(
    "fonction_render/road/Land2a_00044.png")
PERFECTURE = pygame.image.load(
    "fonction_render/house/Security_00001.png")
ENGINEER = pygame.image.load(
    "fonction_render/house/transport_00056.png")
WELL = pygame.image.load(
    "fonction_render/house/Utilitya_00001.png")

HOUSE_01 = pygame.transform.rotozoom(HOUSE_01, 0, scaleDelta)
ROAD = pygame.transform.rotozoom(ROAD, 0, scaleDelta)
PERFECTURE = pygame.transform.rotozoom(PERFECTURE, 0, scaleDelta)
GRASS_IMAGE = pygame.transform.rotozoom(GRASS_IMAGE, 0, scaleDelta)
WELL = pygame.transform.rotozoom(WELL, 0, scaleDelta)
ENGINEER = pygame.transform.rotozoom(ENGINEER, 0, scaleDelta)
TEMP_BUILD = pygame.transform.rotozoom(TEMP_BUILD, 0, scaleDelta)


TEMP_TILE = {
    "house": HOUSE_01, "shovel": GRASS_IMAGE, "road": ROAD, "sword": PERFECTURE,
    "hammer": ENGINEER, "water": WELL, "blank": TEMP_BUILD
}


thickarrow_strings = (  # sized 24x24
    "XX                      ",
    "XXX                     ",
    "XXXX                    ",
    "XX.XX                   ",
    "XX..XX                  ",
    "XX...XX                 ",
    "XX....XX                ",
    "XX.....XX               ",
    "XX......XX              ",
    "XX.......XX             ",
    "XX........XX            ",
    "XX........XXX           ",
    "XX......XXXXX           ",
    "XX.XXX..XX              ",
    "XXXX XX..XX             ",
    "XX   XX..XX             ",
    "     XX..XX             ",
    "      XX..XX            ",
    "      XX..XX            ",
    "       XXXX             ",
    "       XX               ",
    "                        ",
    "                        ",
    "                        ")
rail_strings = (  # sized 24x24
    "  X.X            X.X    ",
    "  X.X            X.X    ",
    "XXX.XXXXXXXXXXXXXX.XXX  ",
    "X....................X  ",
    "XXX.XXXXXXXXXXXXXX.XXX  ",
    "  X.X            X.X    ",
    "  X.X            X.X    ",
    "  X.X            X.X    ",
    "XXX.XXXXXXXXXXXXXX.XXX  ",
    "X....................X  ",
    "XXX.XXXXXXXXXXXXXX.XXX  ",
    "  X.X            X.X    ",
    "  X.X            X.X    ",
    "  X.X            X.X    ",
    "XXX.XXXXXXXXXXXXXX.XXX  ",
    "X....................X  ",
    "XXX.XXXXXXXXXXXXXX.XXX  ",
    "  X.X            X.X    ",
    "  X.X            X.X    ",
    "  X.X            X.X    ",
    "XXX.XXXXXXXXXXXXXX.XXX  ",
    "X....................X  ",
    "XXX.XXXXXXXXXXXXXX.XXX  ",
    "  X.X            X.X    ")
shovel_strings = (  # 32x32
    "XX                         XX   ",
    "XXX                       XXXX  ",
    "XXXX                     XX.XXX ",
    "XX.XX                    X...XXX",
    "XX..XX                   XX...XX",
    "XX...XX                 XXXX.XX ",
    "XX....XX               XX.XXXX  ",
    "XX.....XX             XX.XX     ",
    "XX.....XXX           XX.XX      ",
    "XX...XXXXXX         XX.XX       ",
    "XX..XX             XX.XX        ",
    "XX.X              XX.XX         ",
    "XX               XX.XX          ",
    "X               XX.XX           ",
    "               XX.XX            ",
    "              XX.XX             ",
    "             XX.XX              ",
    "       X    XX.XX               ",
    "      XXXX XX.XX                ",
    "     X..XXXX.XX                 ",
    "    X....XX.XX                  ",
    "   X....XX.XX                   ",
    "  X....X.XXXXX                  ",
    " X....X...X.XX                  ",
    " X...X...X...XX                 ",
    "X.......X....X                  ",
    "X......X....X                   ",
    "X..........X                    ",
    "X.........X                     ",
    "X........X                      ",
    " X.....XX                       ",
    "  XXXXX                         "
)

hammer_strings = (  # 32x32
    "XX                              ",
    "XXX                             ",
    "XXXX                            ",
    "XX.XX                           ",
    "XX..XX                          ",
    "XX...XX                         ",
    "XX....XX                        ",
    "XX.....XX                       ",
    "XX.....XXX                      ",
    "XX...XXXXXX                     ",
    "XX..XX                          ",
    "XX.X                            ",
    "XX            X......X          ",
    "      XXXXXXXXXXXXXXXXXXXXXX    ",
    "      XXXXXXXXXXXXXXXXXXXXXX    ",
    "      XXXXXXXXXXXXXXXXXXXXXX    ",
    "      XXXXXXXXXXXXXXXXXXXXXX    ",
    "      XXXXXXXXXXXXXXXXXXXXXX    ",
    "      XXXXXXXXXXXXXXXXXXXXXX    ",
    "      XXXXXXXXXXXXXXXXXXXXXX    ",
    "      XXXXXXXXXXXXXXXXXXXXXX    ",
    "             XXX..XXX           ",
    "               X..X             ",
    "               X..X             ",
    "               X..X             ",
    "               X..X             ",
    "               X..X             ",
    "               X..X             ",
    "               X..X             ",
    "               X..X             ",
    "               X..X             ",
    "              XXXXXX            "
)

arrow_strings = (  # 32x32
    " X                              ",
    " X.X                            ",
    " X.XX                           ",
    " X..XX                          ",
    " X...XX                         ",
    " X....XX                        ",
    " X.....XX                       ",
    " X......XX                      ",
    " X.......XX                     ",
    " X........XX                    ",
    " X.........XX                   ",
    " X..........XX                  ",
    " X...........XX                 ",
    " X............XX                ",
    " X.............XX               ",
    " X..............XX              ",
    " X...............XX             ",
    " X................XX            ",
    " X......XXXXXXXXXXXXX           ",
    " X.....XXXX                     ",
    " X....XX                        ",
    " X...X                          ",
    " X..X                           ",
    " X.X                            ",
    " XX                             ",
    " X                              ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                "
)
