
import pygame
from pygame.math import Vector2

#TODO starting Point week 3

# Define the size/resolution of our window
res_x = 800
res_y = 600
start_time=0
vFORWARD=Vector2(0.01,0)
HEADWIND_FORCE = float(-0.005)
MASS=4
bForcesAreActive=False


class Character:
    def __init__(self, currentPosition, size):
        self.position = Vector2(currentPosition)        
        self.size=size
        self.velocity=Vector2(0,0)
        self.acceleration = vFORWARD
        self.mass = MASS

    def draw (self, screen):         
         pygame.draw.circle(screen, (255,0,0), self.position, self.size)
        
    def move(self):
        global start_time, bForcesAreActive
        #self.velocity=vFORWARD
        #time in seconds - get_ticks() returns time in miliseconds
        elapsed_time=(pygame.time.get_ticks()-start_time)/1000
        print(str(bForcesAreActive))
        if(bForcesAreActive):
            headwind_force = Vector2(HEADWIND_FORCE,0)
            total_force=headwind_force + vFORWARD
            #calculate acceleration and speed
            self.acceleration=total_force/self.mass
            print(self.acceleration)

       
        #calculate new position
        #self.position += self.velocity 
        #calculate new position
        self.position += self.velocity * elapsed_time + 0.5 * self.acceleration* elapsed_time**2 #TODO ElapsedTime**2 means squared 2
   
        # print(str(elapsed_time) + " seconds")
        # print("---")

def showMessages(screen):
     myfont = pygame.font.SysFont("monospace", 15)
     WHITE = (255, 255, 255)
     label = myfont.render("Acceleration", 1, WHITE)
     screen.blit(label, (10, 400))

def main():
    global bForcesAreActive
    # Initialize pygame, with the default parameters
    pygame.init()
    clock=pygame.time.Clock()
    start_time=pygame.time.get_ticks()
    
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
                if (event.key == pygame.K_SPACE):
                    bForcesAreActive=True
                    # Draw path in Grey
                    pygame.draw.line(screen, (0, 125, 255), dude.position, dude.position + dude.velocity * 10, 1) #TODO not working yet
                    print("pressed space" + str(bForcesAreActive))

                elif (event.key == pygame.K_ESCAPE):
                    return

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0,0,0))
        
        dude.draw(screen)
        dude.move()

        showMessages(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()
main()

