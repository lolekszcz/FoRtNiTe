import pygame
class GameObject():
    def __init__(self,game,x,y,w,h,image,color=(255,255,255)):
        self.game=game
        self.x=x
        self.y=y
        self.w=w
        self.h=h

        self.game.objects.append(self)

        self.image = image
        self.rect=pygame.Rect((x,y,w,h))
        self.color = color
        if self.image!=None:
            pygame.transform.scale(self.image,self.rect)
    def update(self):
        self.rect = pygame.Rect((self.x, self.y,self. w, self.h))
        if self.image!=None:
            pygame.transform.scale(self.image,self.rect)
    def render(self):
        if self.image != None:
            self.window.blit(self.image,self.rect)
        else:

            pygame.draw.rect(self.game.window,self.color,self.rect)