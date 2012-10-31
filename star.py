import random
import pygame

width, height = 800, 600

def init():
    pygame.init()   # Initialized pygame module

    # Screen
    return pygame.display.set_mode((width, height))

#Drawing space and establishing the colors of our stars
def draw_space(surface, stars):
    surface.fill((0, 0, 0))          # Draw the vacuum of space
    for s in stars:
        if s[2] == 3:
            star = pygame.Color(255, 255, 255)
        elif s[2] == 2:
            star = pygame.Color(200, 200, 255)
            # star = pygame.Color(0, 0, 200)
        elif s[2] == 1:
            star = pygame.Color(255, 170, 170)
            # star = pygame.Color(200, 0, 0)
        elif s[2] ==4:
            star = pygame.Color(170,170,170)
        pygame.draw.circle(surface, star, s[:2], s[2])

#Creating stars of different sizes. The smaller stars are more likely to appear than the bigger stars. Random x/y coordinates and random size with weighted probablities.
def build_space(screen):
    # Get a new surface and its parameters
    space = screen.copy()
    width, height = screen.get_size()

    stars = []
    for star in range(40):
        x = random.randint(0, width)
        y = random.randint(0, height)
        rand = random.randint(1, 15)
        if rand <= 8:
            r = 1
        elif rand <= 11:
            r = 2
        elif rand <=14:
            r = 3
        else:
            r=6

        stars.append((x, y, r))
    # print stars

    draw_space(space, stars)
    return space

#Putting in a ship image and resizing the image to only take a portion of it.
def load_ship():
    ship = pygame.image.load('ship.png').convert()
    raw_size = ship.get_size()

    ship = ship.subsurface((0, 0, raw_size[0] / 2, raw_size[1] / 2))
    new_size = ship.get_size()

    ship = ship.subsurface((new_size[0] / 2 - 10, new_size[1] / 2, new_size[0] / 2 + 10, new_size[1] / 2))
    ship.set_colorkey((191, 220, 191))
    return ship


#Trying to add a meteor - need to make it smaller
#def red_meteor():
    #meteor = pygame.image.load('meteor.png').convert()
    #raw_size = meteor.get_size()

    #meteor = meteor.subsurface((0,0, raw_size[0], raw_size[1]))
    #new_size = meteor.get_size()

    #meteor = meteor.subsurface((new_size[0]/2-10, new_size[1] /2, new_size[0] / 2 +10, new_size[1] /2))
    #meteor.set_colorkey((100,100,100))
    #return meteor

def main(screen):
    running = True

    ship = load_ship()
    space = build_space(screen)
    #meteor = red_meteor()
    while running:
        screen.blit(space, (0, 0))
        screen.blit(ship, (100, 100))
        #screen.blit(meteor, (150,150))
        pygame.display.flip()           # Display screen in window

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                # exit()
                running = False


screen = init()
main(screen)
