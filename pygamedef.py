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
    flag1=flag.flag1()
    flag2=flag.flag2()
    flag2.left=100
    flag2.top=100
    flag3=flag.flag3()
    flag3.left=300
    flag3.top=150
    baseball = pygame.image.load("baseball.jpg").convert_alpha()
    
    #inputs are: Surface, color, position(x,y), radius
    pygame.draw.circle(screen,(100,100,100),(20,20),15) #firstinput-screen orbb?
    baseball_rect = baseball.get_rect()
    
    #make the image smaller
    ball = pygame.transform.scale(baseball, (50,50))
    ball_rect = ball.get_rect()
    running = True
    while running:
        screen.fill((0,0,255))

	#Flag1
		flag1.update(screen)
		flag2.update(screen)
		flag3.update(screen)
	
    	flag1.draw(screen)
    	flag2.draw(screen)
		flag3.draw(screen)
       
        ###waits .25 milliseconds to redraw the baseball
        pygame.time.wait(50)

        #draws buffers into window
        pygame.display.flip()
        #quits program
        for event in pygame.event.get():
            if event.type ==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_q):
               running = False

screen = init()
main(screen)
