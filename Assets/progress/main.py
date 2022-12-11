import pygame
from fighter import Fighters

 #starting pygame
pygame.init()

#Creating the game window

SCREEN_WIDTH=1000
SCREEN_HEIGHT=600

#Creates a game window and assigns it to the variable 'screen'
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighter")

#Set frame  rate
clock=pygame.time.Clock()
FPS=60

#define colors used in game

YELLOW=(255,255,0)
RED=(255,0,0)
WHITE=(255,255,255)




#NEVER LODE IMAGES INSIDE YOUR GAME LOOP
#BACKGROUND IMAGE
backgroundimage=pygame.image.load("Assets/images/background/bkgrnd2.jpg").convert_alpha()

#load Sprite Sheets

# function for drawing background onto game window
def draw_background():


    #Scale background image to fit screen
    scaled_background=pygame.transform.scale(backgroundimage,(1000,600))
    #PCoordinte set at (0,0) since background will 
     #start from the top left corner of the screen
    screen.blit(scaled_background,(0, 0)) 

    #functiton for drawing fighter health bars
    
def draw_health_bars(health,x,y):
      ratio=health/100
      pygame.draw.rect(screen,WHITE,(x-3,y-3,403,33))
      pygame.draw.rect(screen,RED,(x,y,400,30))
      
      pygame.draw.rect(screen,YELLOW,(x,y,400*ratio,30)) 

#Create two instance of fighters
fighter1=Fighters(200,310)
fighter2=Fighters(700,310)
    
     
     
    



#Loop for game 

run=True
while run: 
    clock.tick(FPS)

    #Draw background

    draw_background()

    #show stats of fighters

    draw_health_bars(fighter1.health,20,20)
    draw_health_bars(fighter2.health,580,20)

    #move fighters
    fighter1.move(SCREEN_WIDTH,SCREEN_HEIGHT,screen,fighter2)
    #fighter2.move()


    #Draw fighters to screen
    fighter1.draw(screen)
    fighter2.draw(screen)



    #Evenet Handler
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        run=False

  #update display
    pygame.display.update()  

#EXIT Pygame
pygame.quit()
