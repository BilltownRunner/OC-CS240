#Greg Lutzke
#9-25-2012
#Pygame2
#add a rotating baseball

import pygame

pygame.init()

#Screen Size
width, height = 640,480
screen = pygame.display.set_mode((width,height))

baseball = pygame.image.load("baseball.jpg").convert_alpha()
#inputs are: Surface, color, position(x,y), radius
pygame.draw.circle(screen,(100,100,100),(20,20),15) #firstinput-screen orbb?
baseball_rect = baseball.get_rect()

#make the image smaller
ball = pygame.transform.scale(baseball, (20,20))
ball_rect = ball.get_rect()


horizontal = 1
vertical = 3

running = True
while running:
    #colors screen blue
    screen.fill((0,0,255))
    screen.blit(ball,ball_rect) #Draws ball on screen
    ball_rect[0] += horizontal      #moves ball right
    ball_rect[1] += vertical        #moves ball up

    #keeps ball on screen
    if ball_rect.right >= width:
        horizontal = -1
    elif ball_rect.left <= 0:
        horizontal = 1
    if ball_rect.bottom >= height:
        vertical = -3
    elif ball_rect.top <= 0:
        vertical = 3
        
    #(color), (left coordinate, top, right, bottom)
    pygame.draw.rect(screen,(255,255,255),(173,185,305,170))
    pygame.draw.circle(screen,(0,0,255), (225, 240), 50,10)
    pygame.draw.circle(screen,(255,255,0), (275, 300), 50,10)
    pygame.draw.circle(screen,(0,0,0), (325, 240), 50,10)
    pygame.draw.circle(screen,(34,139,34), (375, 300), 50,10)
    pygame.draw.circle(screen,(255,0,0), (425, 240), 50,10)
    
    #rotates image
    #we are creating a new surface
    spun = pygame.transform.rotate(ball,30)
    spun_rect= spun.get_rect()
    #draws the center of the image
    shrink = ball_rect.width-spun_rect.width
    spun_rect.inflate_ip(shrink,shrink)
    ball.blit(spun,(0,0),spun_rect)

    #waits .25 milliseconds to redraw the baseball
    pygame.time.wait(25)

    #draws buffers into window
    pygame.display.flip()
    #quits program
    for event in pygame.event.get():
        if event.type ==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_q):
            running = False
