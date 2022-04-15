author = "pratik majee"

import pygame
import random
import os

pygame.init()
pygame.mixer.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 215, 0)
blue = (30, 144, 255)

# creating game window
screen_width = 800
screen_height = 600

gameWindow = pygame.display.set_mode((screen_width, screen_height))


# creating game title
pygame.display.set_caption("snakes by pratik")
pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont('harrington',35)

# creating text screen


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

# creating a welcome page


def welcome():
    bg_img = pygame.image.load("screen/snakess.jpeg")
    bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height))

    exit_game = False
    while not exit_game:
        gameWindow.blit(bg_img, (0, 0))
        text_screen("welcome to snakes", black, 200, 100)
        text_screen("press space bar to play", red, 170, 200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('music/bgm.mp3')
                    pygame.mixer.music.play(loops=-1)
                    gameLoop()
        pygame.display.update()
        clock.tick(60)


def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# creating a game loop

def gameLoop():

    # creating game specific variables
    exit_game = False
    game_over = False

    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0

    snake_list = []
    snake_length = 1

    food_x = random.randint(20, screen_width/2)
    food_y = random.randint(20, screen_height/2)

    gameOverPic = pygame.image.load("screen/gameover.png")
    gameOverPic = pygame.transform.scale(
        gameOverPic, (screen_width, screen_height))

    mainFieldPic = pygame.image.load("screen/bgpic.jpg")
    mainFieldPic = pygame.transform.scale(
        mainFieldPic, (screen_width, screen_height))

    snake_size = 7
    fps = 30
    score = 0
    # check if the file exist:
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:

        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.blit(gameOverPic, (0, 0))
            text_screen("game over ! press ENTER to continue !", red, 50, 300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('music/bgm.mp3')
                        pygame.mixer.music.play()
                        gameLoop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if velocity_x ==-3 and velocity_y==0:

                            velocity_x=-3
                            velocity_y=0
                        else:    

                            velocity_x = 3
                            velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        if velocity_x==3 and velocity_y==0:

                            velocity_x = 3
                            velocity_y = 0
                        else:
                            velocity_x=-3
                            velocity_y=0    


                    if event.key == pygame.K_UP:
                        if velocity_y==3 and velocity_x==0:

                            velocity_y = 3
                            velocity_x = 0
                        else:
                            velocity_y=-3
                            velocity_x=0    

                    if event.key == pygame.K_DOWN:
                        if velocity_y==-3 and velocity_x==0:
                            velocity_y = -3
                            velocity_x = 0
                        else:
                            velocity_y=3
                            velocity_x=0         

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
           
            if snake_x <= 0:
                snake_x = 800
            elif snake_x >= 800:
                snake_x = 0
    
            if snake_y <= 0:
                snake_y = 600 
            elif snake_y >= 600:
                snake_y = 0

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 10
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snake_length += 3
                fps+=2
                if score > int(hiscore):
                    hiscore = score

            gameWindow.blit(mainFieldPic, (0, 0))
            text_screen("score :"+str(score)+"  hiscore :" +
                        str(hiscore), yellow, 5, 5)
            pygame.draw.rect(gameWindow, white, [
                             food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('music/gameover.mp3')
                pygame.mixer.music.play()

            plot_snake(gameWindow, red, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
