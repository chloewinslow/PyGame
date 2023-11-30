"""
Snake Eater
Made with PyGame
"""

import pygame, sys, time, random


# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
difficulty = 25
print(difficulty)

game_condition = True

# Window size
frame_size_x = 720
frame_size_y = 560


# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')


# Initialise game window
pygame.display.set_caption('Snake Battle')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
purple = pygame.Color(127,0,127)


# FPS (frames per second) controller
fps_controller = pygame.time.Clock()



# Game variables
snake1_pos = [100, 50]
snake1_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

snake2_pos = [400, 100]
snake2_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_spawn = True

# starting directions
direction1 = 'RIGHT'
change_to1 = direction1

direction2 = 'LEFT'
change_to2 = direction2

score1 = 0
score2 = 0


# Game Over
def game_over(winner):
    my_font = pygame.font.SysFont('times new roman', 90)
    # If green snake wins
    if winner == 1:
        game_over_surface = my_font.render('PLAYER 1 WINS', True, red)
    # If purple snake wins
    if winner == 2:
        game_over_surface = my_font.render('PLAYER 2 WINS', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(1, red, 'times', 20)
    show_score(2, red, 'times', 20)
    pygame.display.flip()
    #time.sleep(5)
    #pygame.quit()
    #sys.exit()


# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    # Green Snake score
    if choice == 1:
        score_surface = score_font.render('Green Score : ' + str(score1), True, color)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (10+(frame_size_x/10), 10)
    # Purple Snake score
    elif choice == 2:
        score_surface = score_font.render('Purple Score : ' + str(score2), True, color)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (frame_size_x-(frame_size_x/7), 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()

while game_condition:

    my_font = pygame.font.SysFont(None, 60)
    start_surface = my_font.render('Play Snake Battle!', True, black)
    start_rect = start_surface.get_rect()
    start_rect.midtop = (frame_size_x/2, frame_size_y/4)
    cblue = pygame.Color(77,166,255)
    game_window.fill(cblue)
    game_window.blit(start_surface, start_rect)
    # Creating the instructions and levels buttons
    smallfont = pygame.font.SysFont('Corbel', 45)
    instr_text = smallfont.render('Instructions', True, white)
    text1 = smallfont.render('Easy', True, white)
    text2 = smallfont.render('Medium', True, white)
    text3 = smallfont.render('Hard', True, white)
    button_instr = pygame.draw.rect(game_window, black, pygame.Rect(280, 240, 200, 50))   
    button_background = pygame.draw.rect(game_window, black, pygame.Rect(270, 235, 220, 58))     
    #pygame.draw.rect(game_window, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    b1 = pygame.draw.rect(game_window, black, pygame.Rect(330, 320, 80, 40))        
    b2 = pygame.draw.rect(game_window, black, pygame.Rect(320, 380, 120, 40))        
    b3 = pygame.draw.rect(game_window, black, pygame.Rect(330, 440, 80, 40))    
        
    b1_background = pygame.draw.rect(game_window, black, pygame.Rect(320, 315, 100, 45))
    b2_background = pygame.draw.rect(game_window, black, pygame.Rect(310, 375, 140, 45))
    b3_background = pygame.draw.rect(game_window, black, pygame.Rect(320, 435, 100, 45))
   
    pygame.Surface.blit(game_window, instr_text, button_instr)
    threeDown = frame_size_y//2 + frame_size_y//4
    pygame.Surface.blit(game_window, text1, b1)
    pygame.Surface.blit(game_window, text2, b2)
    pygame.Surface.blit(game_window, text3, b3)

    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                #pygame.event.post(pygame.event.Event(pygame.QUIT))
                #game_condition = False
                pygame.quit()
                quit()
        else:
            if mouse_click:
                if mouse_pos_x > 320 and mouse_pos_x < 420 and mouse_pos_y > 315 and mouse_pos_y < 360:
                       difficulty = 10
                       game_condition = False
                elif mouse_pos_x > 310 and mouse_pos_x < 355 and mouse_pos_y > 375 and mouse_pos_y < 420:
                       difficulty = 25
                       game_condition = False
                elif mouse_pos_x > 320 and mouse_pos_x < 420 and mouse_pos_y > 435 and mouse_pos_y < 480:
                        difficulty = 40
                        game_condition = False
    

    pygame.display.flip()

    #pygame.quit()
    #sys.exit()

    #720x560

while game_condition == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:
            # Changing Direction
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP:
                change_to1 = 'UP'
            if event.key == ord('w'):
                change_to2 = 'UP'
            if event.key == pygame.K_DOWN:
                change_to1 = 'DOWN'
            if event.key == ord('s'):
                change_to2 = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to1 = 'LEFT'
            if event.key == ord('a'):
                change_to2 = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to1 = 'RIGHT'
            if event.key == ord('d'):
                change_to2 = 'RIGHT'
            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

        # Making sure the snake cannot move in the opposite direction instantaneously
        if change_to1 == 'UP' and direction1 != 'DOWN':
            direction1 = 'UP'
        if change_to1 == 'DOWN' and direction1 != 'UP':
            direction1 = 'DOWN'
        if change_to1 == 'LEFT' and direction1 != 'RIGHT':
            direction1 = 'LEFT'
        if change_to1 == 'RIGHT' and direction1 != 'LEFT':
            direction1 = 'RIGHT'
            
        # Making sure the snake cannot move in the opposite direction instantaneously
        if change_to2 == 'UP' and direction2 != 'DOWN':
            direction2 = 'UP'
        if change_to2 == 'DOWN' and direction2 != 'UP':
            direction2 = 'DOWN'
        if change_to2 == 'LEFT' and direction2 != 'RIGHT':
            direction2 = 'LEFT'
        if change_to2 == 'RIGHT' and direction2 != 'LEFT':
            direction2 = 'RIGHT'

        # Moving snake 1
        if direction1 == 'UP':
            snake1_pos[1] -= 10
        if direction1 == 'DOWN':
            snake1_pos[1] += 10
        if direction1 == 'LEFT':
            snake1_pos[0] -= 10
        if direction1 == 'RIGHT':
            snake1_pos[0] += 10

        # Moving snake 2
        if direction2 == 'UP':
            snake2_pos[1] -= 10
        if direction2 == 'DOWN':
            snake2_pos[1] += 10
        if direction2 == 'LEFT':
            snake2_pos[0] -= 10
        if direction2 == 'RIGHT':
            snake2_pos[0] += 10

        # Snake body growing mechanism
        snake1_body.insert(0, list(snake1_pos))
        if snake1_pos[0] == food_pos[0] and snake1_pos[1] == food_pos[1]:
            score1 += 1
            food_spawn = False
        else:
            snake1_body.pop()

        # Snake body growing mechanism
        snake2_body.insert(0, list(snake2_pos))
        if snake2_pos[0] == food_pos[0] and snake2_pos[1] == food_pos[1]:
            score2 += 1
            food_spawn = False
        else:
            snake2_body.pop()

        # Spawning food on the screen
        if not food_spawn:
            food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
        food_spawn = True

        # GFX
        game_window.fill(black)
        for pos in snake1_body:
            # Snake body
            # .draw.rect(play_surface, color, xy-coordinate)
            # xy-coordinate -> .Rect(x, y, size_x, size_y)
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        for pos in snake2_body:
            # Snake body
            # .draw.rect(play_surface, color, xy-coordinate)
            # xy-coordinate -> .Rect(x, y, size_x, size_y)
            pygame.draw.rect(game_window, purple, pygame.Rect(pos[0], pos[1], 10, 10))

        # Snake food
        pygame.draw.rect(game_window, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        # Game Over conditions
        # Getting out of bounds
        if snake1_pos[0] < 0 or snake1_pos[0] > frame_size_x-10:
            game_over(2)
        if snake2_pos[0] < 0 or snake2_pos[0] > frame_size_x-10:
            game_over(1)
        if snake1_pos[1] < 0 or snake1_pos[1] > frame_size_y-10:
            game_over(2)
        if snake1_pos[1] < 0 or snake1_pos[1] > frame_size_y-10:
            game_over(2)
        # Touching the snake body
        for block in snake1_body[1:]:
            if snake1_pos[0] == block[0] and snake1_pos[1] == block[1]:
                game_over(2)

        show_score(1, white, 'consolas', 10)
        show_score(2, white, 'consolas', 10)
        # Refresh game screen
        pygame.display.update()
        # Refresh rate
        fps_controller.tick(difficulty)
        #can have button to choose difficulty in a start page