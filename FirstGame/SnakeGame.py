import pygame
import random

#pygame.mixer.init()

pygame.init()

# Colours
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

#Creating Window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))

# Background image
bgimage = pygame.image.load("Snakebgimage.jpg")
bgimage = pygame.transform.scale(bgimage, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Snakes")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# Welcome window before starting of the game
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(( 235, 250, 232))
        text_screen("Welcome To Snakes Game", black, 230, 250)
        text_screen("Press Space Bar to Continue", blue, 210, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            
            # Starting the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)


# Game Loop 
def gameloop():
    
    # Game Specific Variables
    exit_game = False
    game_over = False
    snake_x = 50
    snake_y = 65
    Food_x = random.randint(20, screen_width / 2)
    Food_y = random.randint(20, screen_height / 2)
    snake_size = 13

    # with open("highscore.txt", "r") as f:
    #     high_score = f.read()
    
    velocity_x = 0
    velocity_y = 0
    init_velocity = 3.5
    score = 0
    fps = 60
    snake_list = []
    snake_length = 1

    
    
    while not exit_game:

        if game_over:
                gameWindow.fill(white)
                text_screen("Game Over!! Press Enter to continue", red, 100, 250)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True 

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - Food_x)<6 and abs(snake_y - Food_y)<6:
                score = score + 10
                Food_x = random.randint(20, screen_width / 2)
                Food_y = random.randint(20, screen_height / 2)
                snake_length = snake_length + 2
                
                # if score> int(high_score):
                #    high_score = score



            gameWindow.fill(white)
            gameWindow.blit(bgimage, (0, 0))
            text_screen("Score: " + str(score), red, 5,5)
            pygame.draw.rect(gameWindow, red, [Food_x, Food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                #pygame.mixer.music.load('gameover.wav')
                #playgame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                #pygame.mixer.music.load('gameover.mp3')
                #playgame.mixer.music.play()
                # print("GAME OVER")
            # pygame.draw.rect(gameWindow, blue, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, blue, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

welcome()
