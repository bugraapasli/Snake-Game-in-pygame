import pygame
import random

# Bugra Pasli - SnakeGame - 02.01.2023

pygame.init() #initializing pygame 

white = (255, 255, 255) # color code for white.
black = (0, 0, 0)   # color code for black.
red = (255, 0, 0)  # color code for red.
blue = (0,0,255) #color code for blue.

disply_width = 800 
disply_height = 600
dis=pygame.display.set_mode((disply_width, disply_height))
pygame.display.set_caption('BUGRA - Snake Game')


snakeblock = 10

clock = pygame.time.Clock()

speed_s = 20
fnt = pygame.font.SysFont(None, 30) 

def snake__(snakeblock, snakelist):     # I create an function and I create an list for our snake. I needed to list because of adding some length for the snake when it eats food.
    for x in snakelist:
        pygame.draw.rect(dis, black, [x[0], x[1], snakeblock, snakeblock])

def message (mesg, color):        # Function for displaying message when the snake died.
    msg = fnt.render(mesg,True, color)
    dis.blit(msg, [disply_width / 4, disply_height / 4])
    
def Loop_Game(): # creating a function for game. 
    x_1 = disply_width / 2
    y_1 = disply_height / 2
    
    game_over = False
    game_close = False
    
    snake_list = []  # creating empty list.
    length__ = 1  # length for our snake for starting.
    
    x_change = 0
    y_change = 0
    
    food_X = round(random.randrange(0, disply_width - snakeblock)/10.0) * 10.0
    food_Y = round(random.randrange(0, disply_height - snakeblock)/10.0) * 10.0
    
    while not game_over:
        
        while game_close == True:
            dis.fill(white)
            message("You DIED! Please Press Q for Quit or Press R for Restart", red)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:   # if you press q after died, the game closes.
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:  # if you press R after died, the game restarts.
                        Loop_Game()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # I used pygame.QUIT here because the game wasn't closing. with this function when you hit the close button, the game is closing.
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:   ## Assigning the keys on the keyboard for moving to snake.
                    x_change = -snakeblock
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snakeblock
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snakeblock
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snakeblock
                    x_change = 0
                
        if x_1 >= disply_width or x_1 < 0 or y_1 >= disply_height or y_1 < 0 :  #If you try to cross the boundaries, you will die.
            game_close = True
        
        x_1 += x_change
        y_1 += y_change
    
        dis.fill(white)
        pygame.draw.rect(dis, blue, [food_X, food_Y, snakeblock, snakeblock])
        headofsnake = []                         ## Starting to write down how to increase our snake's length when it eats.
        headofsnake.append(x_1)
        headofsnake.append(y_1)
        snake_list.append(headofsnake)    
        if len(snake_list) > length__:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == headofsnake:
                game_close = True
        snake__(snakeblock, snake_list)
        pygame.display.update()
        if x_1 == food_X and y_1 == food_Y:
            food_X = round(random.randrange(0, disply_width - snakeblock)/ 10.0) * 10.0
            food_Y = round(random.randrange(0, disply_height - snakeblock)/ 10.0)* 10.0
            length__ += 1                    #If we eats, our snake will grow up.
             
            
        clock.tick(speed_s)
    

    pygame.display.update()
    pygame.quit()
    quit()

Loop_Game()

