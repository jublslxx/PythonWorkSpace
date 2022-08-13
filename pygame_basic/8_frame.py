import pygame

###############################################################
# reset process (must do this)
pygame.init()

# set size of screen
screen_width = 480 
screen_height = 619
screen = pygame.display.set_mode((screen_width, screen_height)) 

# set up title of screen
pygame.display.set_caption("Nado Game") 

# FPS
clock = pygame.time.Clock()
###############################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

running = True # check if game is running
while running:
    dt = clock.tick(60) # input number == frame number

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생했는가?
            running = False # 게임이 진행 중이 아님

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update() # 게임화면 다시 그리기 > must have this

# end pygame 
pygame.quit()