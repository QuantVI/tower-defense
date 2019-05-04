import pygame
from game_paths import tutorial_game_path

class Enemy:
    imgs = []

    def __init__(self,x,y, width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.health = 1
        self.path = tutorial_game_path
        self.img = None

    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        self.animation_count += 1
        self.img = self.imgs[self.animation_count]

        if self.animation_count > len(self.imgs) :
            self.animation_count = 0
        win.blit(self.img, (self.x, self.y))
        self.move()

    
    def collide(self, X, Y):
        """
        Returns if position has hit enemy
        x: int
        y: int
        :return: Boolean
        """
        if X < self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False
    
    def move(self):
        """
        Move enemy
        :return: None
        """
        pass

    def hit(self, val = 1):
        """
        Returns if an enemy has died, and removes on health each call
        val: optional amount of health to remove
        """
        self.health -= val
        if self.health <= 0:
            return True

z_enemy = Enemy(1,1,100,100)

# check that importing path from an extra file I made, works
# print(z_enemy.path)
# print(z_enemy.path[10])
# print(type(z_enemy.path[10]))