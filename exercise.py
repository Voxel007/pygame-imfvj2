
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
    posOffset = [10,0]

    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    pos_init=[20, 70]
  #  pos_target=[600,300]
    vel=[0,0]

    speed=0.1
    dude = Character( pos_init, speed, vel, 15)
   # target = Target( pos_target, 5)

    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return
            #elif event.type == pygame.MOUSEBUTTONDOWN:

                #target.setPosition(pygame.mouse.get_pos())

            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    return
                elif (event.key == pygame.K_UP and dude.position.x < 620):
                    #distance += 1;
                    dude.position += posOffset
                elif (event.key == pygame.K_DOWN and dude.position.x > 20):
                    dude.position -= posOffset
        # Clears the screen
        if(dude.position.x > 300):
            dude.velocity = [0,1]
        if(dude.position.y > 450):
            dude.velocity = [0,0]
        screen.fill((0,0,0))

        #Draw path in Grey 
       # pygame.draw.line(screen,(125,125,125),dude.position, target.position,1)

        #Draw path in green
        pygame.draw.line(screen,(0,135,0),[0,100], [300,100],1)
        #Draw target in Blue 
        #direcaoTarget=numpy.subtract(target.position, dude.position)
        #direcaoTarget=Vector2(target.position) - Vector2(dude.position)
        #pygame.draw.line(screen, (0,0,255), [0,0], direcaoTarget, 1)
        #Draw normalized in green
       # normalized=direcaoTarget.normalize()
      #  velocityNormalized=normalized*dude.speed
       # pygame.draw.line(screen, (0,255,0), dude.position,
        #                 (Vector2(dude.position)+
        #                  Vector2(velocityNormalized)*dude.speed*1000), 4)

       # dude.velocity=velocityNormalized
        #dude.position += posOffset
        dude.move()

        dude.draw(screen)
       # target.draw(screen)
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



