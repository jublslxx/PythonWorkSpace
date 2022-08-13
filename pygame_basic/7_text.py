from numpy import char
import pygame

pygame.init() # reset process

# set size of screen
screen_width = 480 
screen_height = 619
screen = pygame.display.set_mode((screen_width, screen_height)) 

# set up title of screen
pygame.display.set_caption("Nado Game") 

# FPS
clock = pygame.time.Clock()

# call background image
background = pygame.image.load("/Users/jubls/Documents/python_workspace/pygame_basic/background.png")

# call sprite character
character = pygame.image.load("/Users/jubls/Documents/python_workspace/pygame_basic/astronaut.png")

# character will always move so we need to do some settings on character
character_size = character.get_rect().size # get image size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height # bottom of screen

# position to move
to_x = 0
to_y = 0

# moving speed: we only want to control how smooth the movement is
# we want the speed to be rather consistent
character_speed = 0.6

# creating enemy character
enemy = pygame.image.load("/Users/jubls/Documents/python_workspace/pygame_basic/enemy.png")

# character will always move so we need to do some settings on character
enemy_size = enemy.get_rect().size # get image size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width - enemy_width) / 2
enemy_y_pos = (screen_height - enemy_height) / 2 

# define font
game_font = pygame.font.Font(None, 40) # use default font with size 40

# total game time
total_time = 10

# start time information
start_ticks = pygame.time.get_ticks() # 시작 Tick을 받아옴


# event loop has to be running in order to keep screen
running = True # check if game is running
while running:
    dt = clock.tick(60) # input number == frame number

    # character has to move 100 per second
    # 10 fps: 1초동안 10번 동작 > 한번에 10만큼 이동 > 10*10 = 100
    # 20 fps: 1초동안 20번 동작 > 한번에 5만큼 이동 > 5*20 = 100

    # print("fps: " + str(clock.get_fps()))

    for event in pygame.event.get(): # 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생했는가?
            running = False # 게임이 진행 중이 아님

        if event.type == pygame.KEYDOWN: # check if key was clicked
            if event.key == pygame.K_LEFT: # character to left
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP: # character to go up
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            # if pressing left or right key after stepping out from keyboard
            if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT: 
                to_x = 0 # stop moving
            # else, handle other two cases
            elif event.key == pygame.K_UP or event.key ==pygame.K_DOWN: 
                to_y = 0 

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # make sure character stays within game window screen (x axis)
    if character_x_pos < 0:
        character_x_pos = 0 
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = (screen_width - character_width)
    
    # make sure character stays within game window screen (y axis)
    if character_y_pos < 0:
        character_y_pos = 0 
    elif character_y_pos > (screen_height - character_height):
        character_y_pos = (screen_width - character_width)

    # dealing with collision
    # update character rectangle info.
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # check for collision
    if character_rect.colliderect(enemy_rect): # collision with rectangle
        print("BOOM!!!!")
        running = False

    screen.blit(background, (0,0)) # draw background using input image
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # insert timer
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # converting ms to second

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    # render params: text to print, True, text color

    # print it in screen
    screen.blit(timer, (10, 10))

    if (total_time - elapsed_time) <= 0:
        print("Time out! End of game.")
        running = False

    pygame.display.update() # 게임화면 다시 그리기 > 필수

# 잠시 대기
pygame.time.delay(2000) # 2초정도 대기 (ms)

# end pygame 
pygame.quit()