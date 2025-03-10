from classes.GameObject import GameObject
class Wall(GameObject):
    def __init__(self,game,x,y,w,h,image):
        super().__init__(game, x, y, w, h, image)
        self.color=(255,0,0)
        self.image=None

