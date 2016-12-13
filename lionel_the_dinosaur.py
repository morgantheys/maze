# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 1000
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
DINO_GREEN = (0, 61, 26)
PINK = (255, 0, 157)
SKY_BLUE = (189, 236, 252)

#image
img = pygame.image.load('splashscreen.png') 


# Make a player
player =  [200, 150, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 5

# make walls
#wall1 =  [300, 275, 200, 25]
#wall2 =  [400, 450, 200, 25]
wall3 =  [100, 190-110, 25, 75]
wall4 = [100, 301-110, 100, 25]
wall5 = [199, 301-110, 25, 320]
wall6 = [100, 170-110, 180, 25]
wall7 = [277, 170-110, 25, 280]
wall8 = [278, 328, 370, 25]
wall9 = [198, 511, 450, 25]
wall10 = [647, 328, 25, 130]
wall11 = [647, 500, 25, 36]
wall12 = [274, 536, 25, 50]
wall13 = [528, 536, 25, 50]
wall14 = [277, 330, 15, 140]
wall15 = [277, 460, 100, 15]
wall16 = [374, 440, 15, 35]
wall17 = [439, 400, 15, 130]
wall18 = [319, 435, 70, 15]
wall19 = [319, 400, 15, 45]
wall20 = [320, 400, 30, 5]
wall21 = [400, 400, 50, 5]
#wall22 = [335, 350, 15, 52]
wall23 = [400, 385, 15, 15]
wall24 = [400, 380, 80, 5]
wall25 = [525, 381-3, 50, 5]
wall26 = [560, 382, 15, 40]
wall27 = [488, 420, 87, 5]
wall28 = [574, 396, 60, 5]
wall29 = [222, 228, 30, 5]
wall30 = [250, 281, 30, 5]
wall31 = [220, 330, 30, 5]
wall32 = [251, 377, 30, 5]
wall33 = [220, 422, 30, 5]
wall34 = [255, 470, 30, 5]
wall35 = [489, 420, 15, 40]
wall36 = [489, 455, 110, 5]
wall37 = [453, 491, 20, 5]
wall38 = [513, 491, 50, 5]
wall39 = [595, 455, 5, 20]
wall40 = [558, 492, 5, 25]
wall41 = [629, 400, 5, 75]
wall42 = [382, 390, 30, 5]
wall43 = [416, 406, 5, 75]


walls = [wall3, wall4, wall5, wall6, wall7,
         wall8, wall9, wall10, wall11, wall12, wall13,
         wall14, wall15, wall16, wall17, wall18, wall19,
         wall20, wall21, wall23, wall24, wall25,
         wall26, wall27, wall28, wall29, wall30, wall31,
         wall32, wall33, wall34, wall35, wall36, wall37,
         wall38, wall39, wall40, wall41, wall42, wall43]

# Make coins
coin1 = [337, 408, 25, 25]
coin2 = [301, 363, 25, 25]
coin3 = [517, 428, 25, 25]
coin3 = [530, 386, 25, 25]

coins = [coin1, coin2, coin3]

# Make switch
switch = [172, 107, 25, 25]


# Make doors
door1 = [647, 457, 25, 50]
door2 = [335, 350, 15, 52]

doors = [door1, door2]

# Make collidables
collidables = walls + doors

# Splashscreen
started = False
def splashscreen():
    if started == False:
        screen.blit (img,(0,0))
        font = pygame.font.Font(None, 48)
        text = font.render("Press Space to Play", 1, PINK)
        text_rect = text.get_rect(center=(465, 240))
        screen.blit(text, text_rect)
    
# Game loop
win = False
doors_open = False
score = 0

done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            print(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not started:
                    started = True
            
            

    pressed = pygame.key.get_pressed()

    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    if started:
        
        if up:
            player_vy = -player_speed
        elif down:
            player_vy = player_speed
        else:
            player_vy = 0
            
        if left:
            player_vx = -player_speed
        elif right:
            player_vx = player_speed
        else:
            player_vx = 0


        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player[0] += player_vx

    ''' resolve collisions horizontally '''
    for c in collidables:
        if intersects.rect_rect(player, c):        
            if player_vx > 0:
                player[0] = c[0] - player[2]
            elif player_vx < 0:
                player[0] = c[0] + c[2]
    ''' move the player in vertical direction '''
    player[1] += player_vy
    
    for c in collidables:
        if intersects.rect_rect(player, c):                    
            if player_vy > 0:
                player[1] = c[1] - player[3]
            if player_vy < 0:
                player[1] = c[1] + c[3]


    ''' here is where you should resolve player collisions with screen edges '''
    top = player[1]
    bottom = player[1] + player[3]
    left = player[0]
    right = player[0] + player[2]
    
    if top < 0:
        player[1] = 0
    elif bottom > HEIGHT:
        player[1] = HEIGHT - player[3]

    if left < 0:
        player[0] = 0
    elif right > WIDTH:
        player[0] = WIDTH - player[2]



    ''' get the coins '''
     #coins = [c for c in coins if not intersects.rect_rect(player, c)]

    '''
    hit_list = []

    for c in coins:
        if intersects.rect_rect(player, c):
            hit_list.append(c)
    '''
    
    hit_list = [c for c in coins if intersects.rect_rect(player, c)]

    for hit in hit_list:
        coins.remove(hit)
        score += 1
        


    if len(coins) == 0:
        win = True


    ''' open door on switch contact '''
    if intersects.rect_rect(player, switch):
        doors_open = True

        collidables = [c for c in collidables if c not in doors]
        
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(SKY_BLUE)

    pygame.draw.rect(screen, BLACK, player)
    
    for w in walls:
        pygame.draw.rect(screen, DINO_GREEN, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)

    pygame.draw.rect(screen, DINO_GREEN, switch)

    if not doors_open:
        for d in doors:
            pygame.draw.rect(screen, DINO_GREEN, d)


    splashscreen()
     
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, PINK)
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(text, text_rect)

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
