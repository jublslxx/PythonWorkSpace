import pygame

pygame.init() # reset process

# set size of screen
screen_width = 480 
screen_height = 619
screen = pygame.display.set_mode((screen_width, screen_height)) 

# set up title of screen
pygame.display.set_caption("Nado Game") 

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

# event loop has to be running in order to keep screen
running = True # check if game is running
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생했는가?
            running = False # 게임이 진행 중이 아님

        if event.type == pygame.KEYDOWN: # check if key was clicked
            if event.key == pygame.K_LEFT: # character to left
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP: # character to go up
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            # if pressing left or right key after stepping out from keyboard
            if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT: 
                to_x = 0 # stop moving
            # else, handle other two cases
            elif event.key == pygame.K_UP or event.key ==pygame.K_DOWN: 
                to_y = 0 

    character_x_pos += to_x
    character_y_pos += to_y  

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

    screen.blit(background, (0,0)) # draw background using input image

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임화면 다시 그리기 > 필수

# end pygame 
pygame.quit()