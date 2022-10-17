import pygame 

class Button:
    
    def __init__(self,  x, y, image):
        self.x= x
        self.y = y
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
    def show(self, screen):
        screen.blit(pygame.transform.scale(self.image, (200, 100)), self.rect)
        

        
    