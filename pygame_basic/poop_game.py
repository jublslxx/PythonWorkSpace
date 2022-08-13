import pygame
import random

###############################################################
# reset process 
pygame.init()

# set size of screen
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) 

# set up title of screen
pygame.display.set_caption("PooP Game") 

# FPS
clock = pygame.time.Clock()
###############################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
# background
background = pygame.image.load("/Users/jubls/Documents/python_workspace/pygame_basic/poop_back.png")

# game characters
character = pygame.image.load("/Users/jubls/Documents/python_workspace/pygame_basic/char.png")
enemy = pygame.image.load("/Users/jubls/Documents/python_workspace/pygame_basic/enemy.png")

char_size = character.get_rect().size
char_width = char_size[0]
char_height = char_size[1]
char_x = (screen_width - char_width) / 2
char_y = (screen_height - char_height)

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x = random.randint(0,screen_width-enemy_width)
enemy_y = 0

# position to move
char_to_x = 0

character_speed = 0.1
enemy_speed = 10

# define font
game_font = pygame.font.Font(None, 40) # use default font with size 40

# total game time
total_time = 50

# start time information
start_ticks = pygame.time.get_ticks() # 시작 Tick을 받아옴

running = True # check if game is running
while running:
    dt = clock.tick(30) # input number == frame number

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생했는가?
            running = False # 게임이 진행 중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                char_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                char_to_x += character_speed
            else:
                char_to_x += 0
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT: 
                char_to_x = 0 

    char_x += char_to_x * dt

    # make sure character stays within game window screen (x axis)
    if char_x < 0:
        char_x = 0
    elif (char_x + char_width) >= screen_width:
        char_x = screen_width - char_width

    enemy_y += enemy_speed

    # create new enemy after previous enemy is fully dropped
    if enemy_y > screen_height:
        enemy_y = 0
        enemy_x = random.randint(0,screen_width-enemy_width)

    # 4. 충돌 처리
    char_rec = character.get_rect()
    char_rec.left = char_x
    char_rec.top = char_y

    enemy_rec = enemy.get_rect()
    enemy_rec.left = enemy_x
    enemy_rec.top = enemy_y

    if char_rec.colliderect(enemy_rec):
        print("BOOM! YOU LOSE")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (char_x,char_y))
    screen.blit(enemy, (enemy_x,enemy_y))

    # insert timer
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # converting ms to second

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))

    # print it in screen
    screen.blit(timer, (10, 10))

    if (total_time - elapsed_time) <= 0:
        print("Time out! End of game.")
        running = False

    pygame.display.update() # 게임화면 다시 그리기 > must have this

# end pygame 
pygame.quit()