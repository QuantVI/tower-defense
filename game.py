import pygame
import os

class Game:
    def __init__(self):
        self.width = 1000
        self.height = 600
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.towers = []
        self.lives = 20
        self.money = 100
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        # self.clicks = [] # used to record a click path for a map
    
    def run(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # used to get path list by clicking on a background
                    # self.clicks.append(pos)
                    # print(self.clicks)
                    pass


            self.draw()
        
        pygame.quit()
    
    def draw(self):
        self.win.blit(self.bg, (0,0))

        # used to get a display dots for a pth on the background
        #for p in self.clicks:
            #pygame.draw.circle(self.win, (255,0,0), (p[0], p[1]), 5, 0)

        pygame.display.update()

g = Game()
g.run()