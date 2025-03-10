from classes.GameObject import GameObject
class Wall(GameObject):
    def __init__(self,game,x,y,w,h):
        self.color=(255,0,0)
        self.image=None
        self.game=game
        self.x=x
        self.y=y
        self.w=w
        self.h=h
