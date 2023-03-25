import pygame

class Player:
    photo = 'C:/Users/azula/OneDrive/תמונות/forProject/player.png'

    def __init__(self, rightX, leftX, objectY, screen):
        self.rightX = rightX
        self.leftX = leftX
        self.objectY = objectY  # למטה, מיקום סופי ולא משתנה
        self.screen = screen
        # Loading image
        self.playerPhoto = pygame.image.load(self.photo)
        self.startingX = (rightX+leftX)/2 #באמצע

    def first_draw(self):
        self.screen.blit(self.playerPhoto,(self.startingX, self.objectY))
        pygame.display.update()


    def moveRight(self):
        self.draw(self.rightX)

    def moveleft(self):
        self.draw(self.leftX)

    def draw(self, where_to_draw):
        self.objectX = where_to_draw
        self.screen.blit(self.playerPhoto,(self.objectX, self.objectY))
        pygame.display.update()
