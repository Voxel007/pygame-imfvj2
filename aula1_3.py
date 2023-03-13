
import pygame
import numpy
from pygame.locals import *
from pygame.math import Vector2


class Character:
    def __init__(self, position, speed, velocity, size):
        self.position = Vector2(position)        
        self.size=size
        self.velocity=velocity 
        self.speed = speed 
        
    def draw (self, screen):         
         pygame.draw.circle(screen, (255,0,0), self.position, self.size, 1)
       
    def move(self):
        self.position=self.position+self.velocity
        
class Target:
    def __init__(self, position, size):
        self.position=Vector2(position)
        self.size=size
    def setPosition(self, newPosition):
        self.position=newPosition
    def draw(self, screen):
         pygame.draw.circle(screen, (0,0,255), self.position, self.size, 1)
        



def main():
    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res_x = 640
    res_y = 480

    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    pos_init=[100,100]
    pos_target=[600,300]
    vel=[0,0]
    speed=0.1
    dude = Character( pos_init, speed, vel, 15)
    target = Target( pos_target, 5)

    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:               
               target.setPosition(pygame.mouse.get_pos())

            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    return

        # Clears the screen 
        screen.fill((0,0,0))

        #Draw path in Grey 
        pygame.draw.line(screen,(125,125,125),dude.position, target.position,1)        
        #Draw target in Blue 
        #direcaoTarget=numpy.subtract(target.position, dude.position)
        direcaoTarget=Vector2(target.position) - Vector2(dude.position)
        pygame.draw.line(screen, (0,0,255), [0,0], direcaoTarget, 1)
        #Draw normalized in green
        normalized=direcaoTarget.normalize()
        velocityNormalized=normalized*dude.speed
        pygame.draw.line(screen, (0,255,0), dude.position, 
                         (Vector2(dude.position)+
                          Vector2(velocityNormalized)*dude.speed*1000), 4)

        dude.velocity=velocityNormalized
        #direcaoNormalizada=direcaoTarget.normalize() 
        #pygame.draw.polygon(screen, (0, 0, 0), ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        #pygame.draw.line(screen, (250,125,125), pos_init, post_init.add(direcaoNormalizada), 1)
        dude.move()
        dude.draw(screen)
        target.draw(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()
        
main()


