
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
    
    def moveTo(self, target):
        direcaoTarget=Vector2(target.position) - Vector2(self.position)
        
        normalized=direcaoTarget.normalize()
        self.velocity=normalized*self.speed

        raioTravagem=self.size*10
        if(direcaoTarget.magnitude()<raioTravagem):
           self.velocity*=numpy.divide(direcaoTarget.magnitude(),raioTravagem)
        
        self.position=self.position+self.velocity
    
    
class Target:
    def __init__(self, position, size):
        self.position=Vector2(position)
        self.size=size
    def setPosition(self, newPosition):
        self.position=newPosition
    def draw(self, screen):
         pygame.draw.circle(screen, (0,0,255), self.position, self.size)
        



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
    speed=0.5
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
                elif (event.key == pygame.K_UP):
                    dude.speed+=0.01
                elif (event.key == pygame.K_DOWN):
                    dude.speed-=0.01
        # Clears the screen 
        screen.fill((0,0,0))

        #dude.move()
        dude.moveTo(target)

        dude.draw(screen)
        target.draw(screen)
        #print("Velocity" + velocityNormalized)
        #print("Speed"  + speed)
        myfont = pygame.font.SysFont("monospace", 15)
        WHITE = (255, 255, 255)
        label = myfont.render("Up/DOWN - accelerate/decellerate "  + str(dude.speed), 1, WHITE)
        screen.blit(label, (10, 400))
        label1 = myfont.render("Mouse - changes target location", 1, WHITE)
        screen.blit(label1, (10, 415))
       

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()
        
main()



