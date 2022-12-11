import pygame


#fighter class
class Fighters():
    def __init__(self,x,y):
        self.flip= False
        self.rect=pygame.Rect((x,y,80,180))
        self.vel_y=0
        self.jump= False
        self.attacking=False 
        self.attack_type=0
        self.health=100
        
     
        


    def move(self,screen_width,screen_height,surface,target):
       
        SPEED=10
        GRAVITY=2

        dx=0 #change in x coordinate
        dy=0 #change in y coordinate

        #get keypresses
         #When you press anything on the keyboard
         #It is registered in this variable here
 
        key=pygame.key.get_pressed()

        #Can only perform other actions if currently not attacking
        if self.attacking == False:
      

        #movement left or right
         if key[pygame.K_a]:
            dx=-SPEED

         if key[pygame.K_d]:
            dx=SPEED

         #jumping 
         if key[pygame.K_w] and self.jump == False: 
           self.vel_y= -30
           self.jump=True
        
        #Fighter Atttacks
         if key[pygame.K_r] or key[pygame.K_t]:
            self.acttack(surface,target)
            #determine which attack typ e was used
            if[pygame.K_r]:
                self.attack_type=1
            if[pygame.K_t]:
                self.attack_type=2


        


        #apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

       

       



         
        #Make sure players stay on screen 
        if self.rect.left + dx <0:
            dx= -self.rect.left
        
        if self.rect.right + dx>screen_width:
            dx= screen_width -self.rect.right
        if self.rect.bottom +dy  >screen_height -110:
            self.vel_y=0
            self.jump=False
          
            dy= screen_height-110-self.rect.bottom

        #make sure players face each other
        #if target postion is greater than the current player, do not flip
        # else, flip
        if target.rect.centerx >self.rect.centerx:
            self.flip = False
        else:
            self.flip=True



     #update player position
        self.rect.x +=dx
        self.rect.y +=dy


    def acttack(self,surface,target):
     self.attacking=True
     attacking_rect=pygame.Rect(self.rect.centerx-(2*self.rect.width*self.flip),self.rect.y, 2*self.rect.width, self.rect.height)
     if attacking_rect.colliderect(target.rect):
       target.health -=10


     pygame.draw.rect(surface,(0,255,0),attacking_rect)
    
    
       #Rectangle to represent the distance of fighter attacks      
    def draw(self, surface):
        pygame.draw.rect(surface,(255,0,0), self.rect)

        


