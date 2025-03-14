import pygame
import math
from classes import GameObject

class Bullet(GameObject.GameObject):
    def __init__(self, game,x,y,w,h,image, speed, caliber, dx, dy, color=(255,255,255),server=True,visible=True,isLocal=False):
        super().__init__(game,x,y,w,h,image,color=color,server=server,visible=visible,isLocal=isLocal)
        self.speed = speed
        self.caliber = caliber
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.dx, self.dy = self.calculate_direction(self.game.player.x, self.game.player.y, mouse_x, mouse_y)


    def update(self):
        """
        Update the position of the bullet based on its speed and direction (dx, dy).
        This is called every frame.
        """

        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

        # Optionally, check if the bullet is out of bounds and should be destroyed.
        if self.x < 0 or self.x > self.game.width or self.y < 0 or self.y > self.game.height:
            self.visible = False  # Make the bullet invisible (destroy it)

        self.rect = pygame.Rect((self.x, self.y, self.w, self.h))
        if self.image != None:
            pygame.transform.scale(self.image, self.rect)

    def render(self):
        """
        Render the bullet on the screen.
        You can use the parent class `render()` if the bullet is drawn using an image or shape.
        """
        if self.visible:
            if self.image != None:
                self.window.blit(self.image, self.rect)
            else:

                pygame.draw.rect(self.game.window, self.color, self.rect)

    def detect_collision(self, other_objects):
        """
        Detect collisions with other objects (like players or walls).
        This function would need more logic for actual collision detection, depending on how your GameObject class works.
        """
        for obj in other_objects:
            if self.collides_with(obj):  # Assuming collides_with is a method from the parent class GameObject
                self.handle_collision(obj)

    def handle_collision(self, obj):
        """
        Handle the collision with another object (e.g., reduce health, destroy the bullet, etc.).
        """
        if obj.is_damageable:  # Assuming `is_damageable` is an attribute of the object (e.g., player or building)
            obj.take_damage(self.caliber)  # Assuming take_damage exists in the GameObject or related class
        self.visible = False  # Destroy the bullet after the collision

    def calculate_direction(self, player_x, player_y, mouse_x, mouse_y):
        """
        Calculate the direction (dx, dy) from the player to the mouse position.
        This will return a normalized vector scaled by the bullet speed.
        """
        # Calculate the difference in coordinates
        dx = mouse_x - player_x
        dy = mouse_y - player_y

        # Calculate the distance (magnitude) between the player and the mouse
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # Avoid division by zero if the player and mouse are at the same position
        if distance == 0:
            return 0, 0

        # Normalize the direction (make it a unit vector)
        dx = dx / distance
        dy = dy / distance

        # Scale by bullet speed
        dx *= self.speed
        dy *= self.speed

        return dx, dy

