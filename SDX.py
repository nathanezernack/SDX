
from Classes import*

x = 1
y = 31
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

pygame.init()
WIDTH = 1364
HEIGHT = 736
screen = pygame.display.set_mode( (WIDTH, HEIGHT), 0, 0)
clock = pygame.time.Clock()
FPS = 60
V = 5
pygame.display.set_caption('SpaceDestroyerX')
pygame.init()

 
    
all_sprite_list = pygame.sprite.Group()


human = Human(20, 100, 96, 54, 'Human Ship.png')
all_sprite_list.add(human)
#alien = Alien(100, 300, 102, 45, 'Alien Fighter.png')
#all_sprite_list.add(alien)
 


 
done = False    
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_LEFT:
                human.velocityH(-V, 0)
                human.image = pygame.image.load('Human ShipSwitch.png')
            elif event.key == pygame.K_RIGHT:
                human.velocityH(V, 0)
                human.image = pygame.image.load('Human Ship.png')
            elif event.key == pygame.K_UP:
                human.velocityH(0, -V)
                human.image = pygame.image.load('Human ShipUp.png')
            elif event.key == pygame.K_DOWN:
                human.velocityH(0, V)
                human.image = pygame.image.load('Human ShipDown.png')
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                human.velocityH(V, 0)
            elif event.key == pygame.K_RIGHT:
                human.velocityH(-V, 0)
            elif event.key == pygame.K_UP:
                human.velocityH(0, V)
            elif event.key == pygame.K_DOWN:
                human.velocityH(0, -V)
 



        #elif event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_a:
                #alien.velocityA(-V, 0)
                #alien.image = pygame.image.load('Alien FigherSwitch.png')
            #elif event.key == pygame.K_d:
                #alien.velocityA(V, 0)
                #alien.image = pygame.image.load('Alien Figher.png')
            #elif event.key == pygame.K_w:
                #alien.velocityA(0, -V)
                #alien.image = pygame.image.load('Alien FigherUp.png')
            #elif event.key == pygame.K_s:
                #alien.velocityA(0, V)
                #alien.image = pygame.image.load('Alien FigherDown.png')
        #elif event.type == pygame.K_w:
            #if event.key == pygame.K_a:
                #alien.velocityA(V, 0)
            #elif event.key == pygame.K_d:
                #alien.velocityA(-V, 0)
            #elif event.key == pygame.K_w:
                #alien.velocityA(0, V)
            #elif event.key == pygame.K_s:
                #alien.velocityA(0, -V)









 
 
    all_sprite_list.update()
    
 
    background = pygame.image.load("spacebackground.png")
    screen.blit(background,(0,0))
 
    all_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
