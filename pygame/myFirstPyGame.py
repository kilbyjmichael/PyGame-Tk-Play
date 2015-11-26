import os, sys
import pygame
from pygame.locals import *

class PyGameMain:

    def __init__(self, width=600, height=500):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("I'm bouncy!")
        
        self.clock = pygame.time.Clock()
        
        self.black = (0,0,0)
        self.speed = [4, 4]

        self.ball = pygame.image.load("ball.gif").convert_alpha()
        self.ball_size = self.ball.get_rect()

        self.myfont = pygame.font.SysFont("monospace", 115)
        self.label = self.myfont.render("You win!", 1, (255,255,255))

    def MainLoop(self):
        self.placement = self.screen.blit(self.ball, self.ball_size)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.pos = pygame.mouse.get_pos()
                if self.placement.collidepoint(self.pos):
                    self.screen.blit(self.label, (300, 300))
                    pygame.quit()
                    #raise SystemExit, "You won!"
                    
            self.ball_size = self.ball_size.move(self.speed)
            if self.ball_size.left < 0 or self.ball_size.right > self.width:
                self.speed[0] = -self.speed[0]
            if self.ball_size.top < 0 or self.ball_size.bottom > self.height:
                self.speed[1] = -self.speed[1]

            self.msElapsed = self.clock.tick(60)
            self.screen.fill(self.black)
            self.placement = self.screen.blit(self.ball, self.ball_size)
            pygame.display.flip()


if __name__ == "__main__":
    MainWindow = PyGameMain() #init the class
    MainWindow.MainLoop() #run the quit loop
