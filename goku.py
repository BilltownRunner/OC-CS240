#Greg Lutzke
#11/26/12
#Goku tries to take out the villain: Frieza

import pygame
import random

class Goku(object):
    def __init__(self):
        self.image = pygame.image.load('goku.jpg').convert()
        width,height = self.image.get_size()
        #shrinks the image by 1/5
        self.image = pygame.transform.scale(self.image,(width/5,height/5))
        #Gets the color at (0,0) on the image and makes everything at that color transparent
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.x = 60
        self.y = 100
        #Empty list because attacks are added to the list on command
        self.kamehameha = []

        self.frame = 0
        self.velocity = 0

    def draw(self,screen):
        screen.blit(self.image, (self.x, self.y))
        for attack in self.kamehameha:
            #Shape of the attack (circle)
            pygame.draw.circle(screen, (230,230,230),(attack[0], attack[1]),11)

    def update(self,screen):
        self.frame +=1

        remove = False
        for attack in self.kamehameha:
            #Controls movement speed of attack
            attack[0] += 10
            if attack[0] > screen.get_width():
                remove = True

        if remove:
            del self.kamehameha[0]
        
        #Move Goku
        self.y += self.velocity
        #Controls what happens once the image is off-screen
        if self.y >screen.get_height() and self.velocity >0:
            self.y = -self.image.get_height() + 70
        if self.y <-self.image.get_height() and self.velocity < 0:
            self.y = screen.get_height() - 70
           
        
        #Attack
    def shoot(self):
        #Number of attacks that can appear on screen at once
        if len(self.kamehameha) < 3:
            y_loc = self.y + 100
            self.kamehameha.append([self.x+50, y_loc])

    #Movement speed of Goku when going down           
    def move_down(self):
        self.velocity = 10
  
    #Movement speed of Goku when going up  
    def move_up(self):
        self.velocity = -10

class Villain(object):
    def __init__(self,x,y):
        self.image = pygame.image.load('frieza.jpg').convert()
        width,height = self.image.get_size()
        self.image = pygame.transform.scale(self.image,(width/3,height/3))
        self.x = x
        self.y = y
        self.frame = 0
        self.velocity = 0
        
    def draw(self,screen):
        screen.blit(self.image, (self.x, self.y))
       
    def update(self,screen):
        #The higher the screen input the more frequently the villian will change direction
        if random.randint(1,20) == 1:
            #The scalar that the villian will change direction
            self.velocity *= -1
        
        #Gives movement to Villian
        self.y = self.velocity +self.y
        
        self.frame += 1        
        
        #Controls what happens once the image is off-screen
        if self.y >screen.get_height() and self.velocity >0:
            self.y = -self.image.get_height() + 70
        if self.y < -self.image.get_height() and self.velocity <0:
            self.y = screen.get_height() - 70

    def move_down(self):
        self.velocity = 10

    def move_up(self):
        self.velocity = -10

def init():
    width, height = 800,600
    pygame.init()
    
    return pygame.display.set_mode((width,height))

def main(screen):
    clock =pygame.time.Clock()
    goku = Goku()
    #Starting location of Villain
    villain = Villain(700,275)
    
    villain.move_up()
    running = True
    while running:
        #fils background with the point (0,0) on the Goku image
        screen.fill(goku.image.get_colorkey())
        
        goku.draw(screen)
        villain.draw(screen)
        pygame.display.flip()
        goku.update(screen)
        villain.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    goku.shoot()
                if event.key == pygame.K_s:
                    goku.move_down()
                if event.key == pygame.K_w:
                    goku.move_up()
        clock.tick(40)

screen = init()
main(screen)
