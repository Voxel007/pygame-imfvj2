
import pygame
from pygame.math import Vector2

#TODO starting Point week 2

# Define the size/resolution of our window
res_x = 800
res_y = 600

vFORWARD=Vector2(0.1,0)

class Character:
    def __init__(self, currentPosition, size):
        self.position = Vector2(currentPosition)        
        self.size=size
        self.velocity=Vector2(0,0)

    def draw (self, screen):         
         pygame.draw.circle(screen, (255,0,0), self.position, self.size)
        
    def move(self):
         self.velocity=vFORWARD
        
         #calculate new position
         self.position += self.velocity 

         print (str(self.position[0]) + " - x")
         print (str(self.position[1]) + " - y")
         print("---")

def showMessages(screen):
     myfont = pygame.font.SysFont("monospace", 15)
     WHITE = (255, 255, 255)
     label = myfont.render("Move left to right", 1, WHITE)
     screen.blit(label, (10, 400))

def main():
    # Initialize pygame, with the default parameters
    pygame.init()
    
    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    dude = Character( [10,100], 10)

    # Game loop, runs forever
    while (True):
        # Process OS events
        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    return

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,0))
        
        dude.draw(screen)
        dude.move()

        showMessages(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()
main()

