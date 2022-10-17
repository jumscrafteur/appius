from ast import PyCF_ALLOW_TOP_LEVEL_AWAIT
import pygame
from Button import Button
from const import*

pygame.init()



#Ouverture de la fenêtre Pygame
screen = pygame.display.set_mode((screen_height, screen_width))

#Chargement et collage du fond et préfond 
waitingscreen = pygame.image.load("C3title_00001.png")
fond = pygame.image.load("0_fired_00001.png").convert()

#BOUCLE INFINIE
button = Button(screen_height/4, screen_width/2, "paneling_00231.png")

running = True
screen.blit(waitingscreen, (0,0))
while running:
    # Test d'un bouton simple avec son décor
    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(fond, (0,0))
            screen.fill((245,245,220), (100, 200, screen_height-100, screen_width-200))
            button.show(screen) 
            pygame.display.flip()
