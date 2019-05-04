import pygame

class Enemy:
    imgs = []

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.animation_count = 0
        self.health = 1
        self.path = []

    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        pass
    
    def collide(self, x, y):
        """
        Returns if position has hit enemy
        x: int
        y: int
        :return: Boolean
        """
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