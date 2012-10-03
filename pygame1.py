#Greg Lutzke
#10-3-2012
#Pygamedef
#Changed the program into functions

import pygame
import flag
width, height = 640,480
def init():
    pygame.init()
    return pygame.display.set_mode((width,height))

def main(screen):
    flag1=flag.flag()
    flag2=flag.flag()
    flag2.left=100
    flag2.top=100
    baseball = pygame.image.load("baseball.jpg").convert_alpha()
    #inputs are: Surface, color, position(x,y), radius
    pygame.draw.circle(screen,(100,100,100),(20,20),15) #firstinput-screen orbb?
    baseball_rect = baseball.get_rect()
    #make the image smaller
    ball = pygame.transform.scale(baseball, (50,50))
    ball_rect = ball.get_rect()
    running = True
    horizontal = 1
    vertical = 3
    while running:
        screen.fill((0,0,255))
        #colors screen blue
##        screen.blit(ball,ball_rect)     #Draws ball on screen
##        ball_rect[0] += horizontal      #moves ball right
##        ball_rect[1] += vertical        #moves ball up

        #keeps ball on screen
##        if ball_rect.right >= width:
##            horizontal = -1
##        elif ball_rect.left <= 0:
##            horizontal = 1
##        if ball_rect.bottom >= height:
##            vertical = -3
##        elif ball_rect.top <= 0:
##            vertical = 3

        if flag2.left <= width:
            flag2.left += horizontal
        else:
            horizontal= -horizontal
            flag2.left+=horizontal
        if flag2.top <= height:
            flag2.top += vertical
        else:
            vertical= -vertical
            flag2.top+= vertical

        #rotates image
        #we are creating a new surface
##        spun = pygame.transform.rotate(ball,30)
##        spun_rect= spun.get_rect()
##
##        #draws the center of the image
##        shrink = ball_rect.width-spun_rect.width
##        spun_rect.inflate_ip(shrink,shrink)
##        ball.blit(spun,(0,0),spun_rect)
        flag1.draw(screen)
        flag2.draw(screen)
##        
##        #waits .25 milliseconds to redraw the baseball
        pygame.time.wait(50)

        #draws buffers into window
        pygame.display.flip()
        #quits program
        for event in pygame.event.get():
            if event.type ==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_q):
               running = False

screen = init()
main(screen)