import pygame


class Human(pygame.sprite.Sprite):

 
 
    def __init__(self, x, y, width, height, image_string):
        super().__init__()
 
  
        self.image = pygame.image.load("Human Ship.png")
 
       
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
    
        self.change_x = 0
        self.change_y = 0
        
 
 
    def velocityH(self, x, y):
  
        self.change_x += x
        self.change_y += y
 
    def update(self):
        
        self.rect.x += self.change_x
        self.rect.y += self.change_y



#class Alien(pygame.sprite.Sprite):

 
 
    #def __init__(self, x, y, width, height, image_string):
        
        #self.image = pygame.image.load("Alien Fighter.png")
   
        #super().__init__()
 
  
        #self.rect = self.image.get_rect()
        #self.rect.x = x
        #self.rect.y = y
 
    
        #self.change_x = 0
        #self.change_y = 0
        
 
 
    #def velocityA(self, x, y):
  
        #self.change_x += x
        #self.change_y += y
 
    #def update(self):
        
        #self.rect.x += self.change_x
        #self.rect.y += self.change_y      
        

