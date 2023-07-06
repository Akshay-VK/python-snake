import pygame
import random
import math

grid_size = 32
cell_size = 16

player_pos = [[grid_size//2,grid_size//2]]
player_vel=[1,0]
died=False
apple=0

def newapple():
    apple=player_pos[0]
    while apple in player_pos:
        apple=[math.floor(random.random()*grid_size),math.floor(random.random()*grid_size)]
    return apple

def init():
    player_pos = [[grid_size//2,grid_size//2]]
    player_vel=[1,0]
    died=False
    apple=newapple()
    return (player_pos,player_vel,died,apple)

init()
state=0

# pygame setup
pygame.init()
screen = pygame.display.set_mode((grid_size*cell_size, grid_size*cell_size))
pygame.display.set_caption('Snake====<)-<')
clock = pygame.time.Clock()
running = True
dt = 0

img_title = pygame.image.load("SNAKETITLE.png").convert()



apple=newapple()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if state==0:
        screen.blit(img_title,(0,0))
    else:
        
    
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
      
        pygame.draw.rect(screen,"red",pygame.Rect(apple[0]*cell_size,apple[1]*cell_size,cell_size,cell_size))
    
        #check if player turned itself inside out/went into itself
        if player_pos[0] in player_pos[1:]:
            died=True
        for c in range(len(player_pos)):
            pygame.draw.rect(screen,"white",pygame.Rect(player_pos[c][0]*cell_size,player_pos[c][1]*cell_size,cell_size,cell_size))
    

    keys = pygame.key.get_pressed()
    if not state==0:
        #key presses
        if keys[pygame.K_w]:
            player_vel = [0,-1]
        elif keys[pygame.K_s]:
            player_vel = [0,1]
        elif keys[pygame.K_a]:
            player_vel = [-1,0]
        elif keys[pygame.K_d]:
            player_vel = [1,0]
        #update new position of snake head
        newpos=[player_vel[0]+player_pos[0][0],player_vel[1]+player_pos[0][1]]
        player_pos=[newpos]+player_pos
        if player_pos[0]==apple:
            #dont shorten as snake ate apple
            apple=newapple()
        else:
            #shorten snake length
            player_pos.pop()
    
        #check if snake out of bounds
        if player_pos[0][0]==-1 or player_pos[0][1]==-1 or player_pos[0][0]==grid_size or player_pos[0][1] == grid_size:
            died=True
       
        if died==True:
            screen.fill("red")
            state=0
            #init()

    else:
        #if we press space on home screen, change state to game and reset data
        if keys[pygame.K_SPACE]:
            state=1
            (player_pos,player_vel,died,apple)=init()
            
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(6) / 1000

pygame.quit()


