import pygame
class SquareObject:
    photo = 'C:/Users/azula/OneDrive/תמונות/forProject/construction_barrier1.png'
    objectX = 0
    objectY = 0
    screen = ''
    def __init__ (self, objectX, objectY, screen):
        self.objectX = objectX
        self.objectY = objectY
        self.screen = screen
        # Loading image
        self.objectPhoto = pygame.image.load(self.photo)


    def draw(self):
        self.screen.blit(self.objectPhoto,(self.objectX, self.objectY))
        pygame.display.update()

 #   def delete(self, objectX, objectY, screen):
  #      color = (255,0,0)
   #     pygame.draw.rect(screen, color, pygame.Rect(objectX, objectY, 60, 60))
    #    self.screen.blit(screen, (objectX, objectY))
     #   pygame.display.update()

    def moveDown(self):
      #  self.delete(self.objectX, self.objectY, self.screen)
        self.objectY += 10
        self.draw()

