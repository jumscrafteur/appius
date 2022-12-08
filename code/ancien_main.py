import pygame
from Button import *
from const import*

pygame.init()

# Ouverture de la fenêtre Pygame
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
[(screen_width, screen_height)] = pygame.display.get_desktop_sizes()
# Chargement et collage du fond et préfond
fond = pygame.image.load("assets/0_fired_00001.png").convert()


class Game():
    def __init__(self) -> None:
        self.start_menu = True

    def action(self):
        self.start_menu = False


g = Game()
# BOUCLE INFINIE
button = Button_text(screen_width/2, screen_height/2,
                     lambda: print("ok"), "Je veux lancer le jeu")
running = True
button_start = Button_img(screen_width/2, screen_height/2,
                          g.action, "assets/C3title_00001.png")
while running:

    pygame.time.Clock().tick(60)
    # Test d'un bouton simple avec son décor
    if g.start_menu:
        button_start.show(screen)
    else:
        screen.blit(pygame.transform.scale(
            fond, (screen_width, screen_height)), (0, 0))
        button.show(screen, True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_start.MouseonButton(event.pos)
            button.MouseonButton(event.pos)
        if event.type == pygame.USEREVENT:
            event.action()
    pygame.display.flip()
