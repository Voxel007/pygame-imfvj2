import pygame
from pygame.locals import *
from pygame.math import Vector2


class Character:
    def __init__(self, currentPosition, size): #why do we need self?
        self.currentPosition = currentPosition
        self.size = size

    def setPosition(self, newPosition):
        self.position = newPosition

    def draw(self, screen): # draws a circle
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.size)




class Target:
    def __init__(self, position, size):
        self.position = position
        self.size = size

    def setPosition(self, newPosition):
        self.position = newPosition

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), self.position, self.size)


def main():
    # Initialize pygame, with the default parameters
    pygame.init()

    # Define the size/resolution of our window
    res_x = 640
    res_y = 480


    dudePos = [300,100]



    # Create a window and a display surface
    screen = pygame.display.set_mode((res_x, res_y))

    dude = Character([100, 100], 15) # instanciate Character
    target = Target([600, 300], 5) # instanciate Target -

    #dude.setPosition([300,300]) #TODO Vector2 has to be declared in edgy brackets using 2 ints
    # dude.setPosition(100,100) #TODO unexpeted argument
    dude.setPosition(dudePos)

    #movementDirection = target.position-dudePos
    #movementDirection = target.position + [1,1]
    movementDirection = Vector2(target.position) - Vector2(dudePos) #TODO is not accepting a minus?



    dude.setPosition(dudePos)


    # Game loop, runs forever
    while (True):
        # Process OS events



        for event in pygame.event.get():
            # Checks if the user closed the window
            if (event.type == pygame.QUIT):
                # Exits the application immediately
                return
            elif event.type == pygame.MOUSEBUTTONDOWN: #TODO why does this one not need brackets?
                # print( pygame.mouse.get_pos())
                # x = pygame.mouse.get_pos()[0]
                # x, y = pygame.mouse.get_pos()
                # print(tuple(mousePos))
                # print(pygame.math.Vector2(mousePos))

                mousePos = pygame.mouse.get_pos()

                target.setPosition(mousePos)
                #dude.setPosition([100][400])
                #dude.setPosition([300, 300])
                #dude.setPosition(mousePos)

            elif (event.type == pygame.KEYDOWN):
                print("stop Error") #TODO without doing something python throws an identation error?
                #put here that the ball becomes slower
            elif (event.type == pygame.KEYUP):

                # put here that the ball becomes faster

                if (event.key == pygame.K_ESCAPE):
                    return

        # Clears the screen with a very dark blue (0, 0, 20)
        screen.fill((0, 0, 0))

        dude.setPosition(movementDirection)

        dude.draw(screen)
        target.draw(screen)

        # Swaps the back and front buffer, effectively displaying what we rendered
        pygame.display.flip()


main()

