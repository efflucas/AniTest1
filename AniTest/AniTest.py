
import sys # import sys module
import pygame # import pygame module
from pygame.locals import * #

pygame.init() # initialize pygame



# set up the pygame window
DISP_WIDTH = 800 # display width in pixels
DISP_HEIGHT = 600 # display heigth in pixels



DISPLAYSURF = pygame.display.set_mode((DISP_WIDTH, DISP_HEIGHT))
pygame.display.set_caption('Animation Test') # sets window title to "Animation Test"




WHITE = (255, 255, 255)
    
class Bubblegum(): # bubblegum class

    # __init__ applies variables to entire class
    # test.png is 15x15 pixels, therefore we use minus 15 later on in the code
    def __init__(self, image = "test.png", x = DISP_WIDTH / 2, y = DISP_HEIGHT / 2, direction = 'right'): # default values
        self.image = pygame.image.load(image) #
        self.x = x
        self.y = y
        self.direction = direction

    def update(self): # update functions only uses self. this is what the code does every 'tick'

        if self.direction == 'right':
            self.x += 1
            if self.x == DISP_WIDTH - 15: # 785
                self.direction = 'down' # if self.x is 785 change direction to 'down'

        elif self.direction == 'down':
            self.y += 1
            if self.y == DISP_HEIGHT - 15: # 585
                self.direction = 'left' # if self.y is is 585 change direction to left

        elif self.direction == 'left':
            self.x -= 1
            if self.x == 10: # i
                self.direction = 'up' # if self.x is 10 change direction to 'up'

        elif self.direction == 'up':
            self.y -= 1
            if self.y == 10:
                self.direction = 'right' # if self.y is 10 change direction to 'right'

    def draw(self):
        DISPLAYSURF.blit(self.image, (self.x, self.y))




bubblegum = Bubblegum() # creates a bubblegum objects from the Bubbmelgum class called "bubblegum"



while True: # main loop of the game
    DISPLAYSURF.fill(WHITE) # fill display with white color
    
    bubblegum.update()
    bubblegum.draw()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()







            
        



        
    
 
        
      

                                
    