#Greg Lutzke
#9-19-2012
#Pygame1

import pygame

pygame.init()

#Screen Size
width, height = 640,480
screen = pygame.display.set_mode((width,height))

running = True
while running:
    #colors screen blue
    screen.fill((0,0,255))
    #(color), (left coordinate, top, right, bottom)
    pygame.draw.rect(screen,(255,255,255),(173,185,305,170))
    pygame.draw.circle(screen,(0,0,255), (225, 240), 50,10)
    pygame.draw.circle(screen,(255,255,0), (275, 300), 50,10)
    pygame.draw.circle(screen,(0,0,0), (325, 240), 50,10)
    pygame.draw.circle(screen,(34,139,34), (375, 300), 50,10)
    pygame.draw.circle(screen,(255,0,0), (425, 240), 50,10)
    #draws buffers into window
    pygame.display.flip()
    #quits program
    for event in pygame.event.get():
        if event.type ==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_q):
            running = False
    

    
