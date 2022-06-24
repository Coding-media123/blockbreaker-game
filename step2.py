
import pygame
from pygame.locals import*
from pygame import mixer
import os 
import sys
#initialize pygame 
pygame.init()
# game variables
WIDTH = 600
HEIGHT = 600
screen = (WIDTH, HEIGHT)

# Color
bg = (234,218,184)
# block Color
block_red = (242, 85, 96)
block_green = (86,174,87)
block_blue = (69, 177, 232)

# PADLLE COLOR
padle_col = (142, 135, 123)
padle_outline = (100, 100,100)
# define game variables 
cols= 6
rows = 6
#define clock
clock = pygame.time.Clock()
fps = 60

#brick wall class
class Wall():
    def __init__(self):
        self.width = WIDTH // cols
        self.height = 50
    def create_wall(self):
        self.blocks = []
        # define an empty list for individual block
        block_individual = []
        for row in range(rows):
            # reset the block row list
            block_row = []
            # itererate through each column in that row
            for col in range(cols):
                #generate x anf=d y position for each blok and  create an rectangle from  that 
                block_x = col * self.width
                block_y = row * self.height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                # assigned block strength based on row 
                if row < 2:
                    strength = 3
                elif row < 4 :
                    strength = 2
                elif row < 6:
                    strength = 1
                # create a list at this point to store the rect and  colour data
                block_individual = [rect, strength]
                # append that individual block to block rows
                block_row.append(block_individual)
            #append the row to the full list of the blocks
            self.blocks.append(block_row)
    def draw_wall(self):
        for row in self.blocks:
            for block in row:
                # assign the color based on each block strength
                if block[1] == 3:
                    block_col = block_blue
                elif block[1] == 2:
                    block_col = block_green
                elif block[1] == 1:
                    block_col = block_red
                pygame.draw.rect(screen, block_col, block[0])
                pygame.draw.rect(screen,bg,(block[0]),2)
#Padlle class
class Padlle():
    def __init__(self):
        #define padlle variable
        self.height = 20
        self.weidth = int(WIDTH / cols)
        self.x = int((HEIGHT / 2) - (self.weidth / 2))
        self.y = HEIGHT-(self.height * 2)
        self.speed = 10
        self.rect = Rect(self.x, self.y, self.weidth, self.height)
        self.direction = 0
    def move(self):
        #reset movement direction
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        if key[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
            self.direction = 1
    def draw(self):
        pygame.draw.rect(screen, padle_col, self.rect)


# creting display 
screen= pygame.display.set_mode((screen))
pygame.display.set_caption("block breaker game")

# create a wall
wall = Wall()
wall.create_wall()
#create a padlle
player_padlle = Padlle()
run = True

while run :
    screen.fill(bg)
    #draw paddle
    player_padlle.draw()
    player_padlle.move()


    # draw wall 
    wall.draw_wall()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                run = False
    clock.tick(fps)
    pygame.display.update()
    
pygame.quit()
sys.exit()

