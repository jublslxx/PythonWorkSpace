import pygame

pygame.init() # reset process

# set size of screen
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) 

# set up title of screen
pygame.display.set_caption("Nado Game") 

# call background image
background = pygame.image.load("/Users/jubls/Documents/python_workspace/pygame_basic/background.png")

# event loop has to be running in order to keep screen
running = True # check if game is running
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생했는가?
            running = False # 게임이 진행 중이 아님
    #screen.fill((75, 125, 75)) # fill with color (R, G, B)
    screen.blit(background, (0,0)) # draw background using input image

    pygame.display.update() # 게임화면 다시 그리기 > 필수
# end pygame 
pygame.quit()