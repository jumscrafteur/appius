import pygame 
from const import*

class Button:
    
    def __init__(self,  x, y, height, width, image, text=""):
        self.x= x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text = text
        
    def draw(self, screen):
        font = pygame.font.SysFont('Bookman Old Style Std Regular', 60)
        if self.text !="":
            text = font.render(self.text, 1, (0,0,0))
            screen.blit(text, (screen_height/2 - self.height/2, screen_width/2))
        else:
            screen.blit(pygame.transform.scale(self.image, (self.height, self.width)), self.rect)
        

        