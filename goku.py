import pygame

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
        self.kamehameha = [[130,200]]
        self.frame = 0

    def draw(self,screen):
        screen.blit(self.image, (self.x, self.y))
        for attack in self.kamehameha:
            pygame.draw.circle(screen, (255,255,255),(attack[0], attack[1]),6)

    def update(self,screen):
        self.frame +=1

        for attack in self.kamehameha:
            attack[0] += 1
        
        #Move Goku
        self.y += 1
        if self.y >screen.get_height():
            print len(self.kamehameha)
            self.y=0
        
        #Attack
        if self.y %100 ==0:
            self.kamehameha.append([130,self.y +100])

def init():
    width, height = 800,600
    pygame.init()
    
    return pygame.display.set_mode((width,height))

def main(screen):
    clock =pygame.time.Clock()
    goku = Goku()
    running = True
    while running:
        #fils background with the point (0,0) on the Goku image
        screen.fill(goku.image.get_colorkey())
        
        goku.draw(screen)
        pygame.display.flip()
        goku.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                running = False
        clock.tick(40)

screen = init()
main(screen)
