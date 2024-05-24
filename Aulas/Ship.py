import pygame
class Ship:
    
    def __init__(self,screen):
         """
    inicializa espaçamento define posição 
    """
         self.screen = screen
         self.image = pygame.image.load("imagens/space-ship.png")
         self.image_size =(70,70)
         self.image = pygame.transform.scalet(self.image, )
         self.rect = self.image.get_rect()
         self.screen_rect = screen.get_rect()
         self.rect.center = self.screen_react.senterx
         self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """
        desenha espaçonave posição inicial
        """

        self.screen.blit(self.images, self.rect)
