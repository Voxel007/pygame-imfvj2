
import pygame
from pygame.locals import *
class Character:
    def __init__(self, currentPosition, size):
        self.currentPosition = currentPosition        
        self.size=size

    def draw (self, screen):         
         pygame.draw.circle(screen, (255,0,0), self.currentPosition, self.size)
 
class Target:
    def __init__(self, position, size):
        self.position=position
        self.size=size
    def setPosition(self,newPosition):
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

    dude = Character( [100,100], 15)
    target = Target( [600,300], 5)

    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
               #print( pygame.mouse.get_pos())
               #x = pygame.mouse.get_pos()[0]
               #x, y = pygame.mouse.get_pos()
               #print(tuple(mousePos))
               #print(pygame.math.Vector2(mousePos))
              
               mousePos = pygame.mouse.get_pos()
               
               target.setPosition(mousePos)

            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    return

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,0))
        
        dude.draw(screen)
        target.draw(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()
        
main()

