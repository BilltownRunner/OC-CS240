import pygame
class flag1(object):
    def __init__(self):
        self.left=0
        self.top=0
        self.width=305
        self.height=170
	self.horizontal = 8
	self.vertical = 4
	

    def draw(self,screen):
        pygame.draw.rect(screen,(255,255,255),(self.left,self.top,self.width,self.height))
        pygame.draw.circle(screen,(0,0,255), (self.left +52, self.top +55), 50,10)
        pygame.draw.circle(screen,(255,255,0),(self.left+102, self.top+110), 50,10)
        pygame.draw.circle(screen,(0,0,0), (self.left+152, self.top+55), 50,10)
        pygame.draw.circle(screen,(34,139,34), (self.left+202, self.top+110), 50,10)
        pygame.draw.circle(screen,(255,0,0), (self.left+252, self.top+55), 50,10)
        print self.left, self.top, self.width, self.height
	
    def update(self,screen):
	width, height = screen.get_size()
	if self.left+self.width <= width and self.left>=0:
            self.left += self.horizontal
        else:
            self.horizontal= -self.horizontal
            self.left+=self.horizontal
        if self.top+self.height <= height and self.top>=0:
            self.top += self.vertical
        else:
            self.vertical= -self.vertical
            self.top+= self.vertical
	
class flag2(object):
    def __init__(self):
        self.left=0
        self.top=0
        self.width=305
        self.height=170
	self.horizontal = 4
	self.vertical = 8
	

    def draw(self,screen):
        pygame.draw.rect(screen,(255,255,255),(self.left,self.top,self.width,self.height))
        pygame.draw.circle(screen,(0,0,255), (self.left +52, self.top +55), 50,10)
        pygame.draw.circle(screen,(255,255,0),(self.left+102, self.top+110), 50,10)
        pygame.draw.circle(screen,(0,0,0), (self.left+152, self.top+55), 50,10)
        pygame.draw.circle(screen,(34,139,34), (self.left+202, self.top+110), 50,10)
        pygame.draw.circle(screen,(255,0,0), (self.left+252, self.top+55), 50,10)
        print self.left, self.top, self.width, self.height
	

    def update(self,screen):
	width, height = screen.get_size()
	if self.left+self.width <= width and self.left>=0:
            self.left += self.horizontal
        else:
            self.horizontal= -self.horizontal
            self.left+=self.horizontal
        if self.top+self.height <= height and self.top>=0:
            self.top += self.vertical
        else:
            self.vertical= -self.vertical
            self.top+= self.vertical

class flag3(object):
    def __init__(self):
        self.left=0
        self.top=0
        self.width=305
        self.height=170
	self.horizontal = 9
	self.vertical = 9
	

    def draw(self,screen):
        pygame.draw.rect(screen,(255,255,255),(self.left,self.top,self.width,self.height))
        pygame.draw.circle(screen,(0,0,255), (self.left +52, self.top +55), 50,10)
        pygame.draw.circle(screen,(255,255,0),(self.left+102, self.top+110), 50,10)
        pygame.draw.circle(screen,(0,0,0), (self.left+152, self.top+55), 50,10)
        pygame.draw.circle(screen,(34,139,34), (self.left+202, self.top+110), 50,10)
        pygame.draw.circle(screen,(255,0,0), (self.left+252, self.top+55), 50,10)
        print self.left, self.top, self.width, self.height
	

    def update(self,screen):
	width, height = screen.get_size()
	if self.left+self.width <= width and self.left>=0:
            self.left += self.horizontal
        else:
            self.horizontal= -self.horizontal
            self.left+=self.horizontal
        if self.top+self.height <= height and self.top>=0:
            self.top += self.vertical
        else:
            self.vertical= -self.vertical
            self.top+= self.vertical

