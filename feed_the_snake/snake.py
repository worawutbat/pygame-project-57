# Feed the snake template by Worawut Titumjariya 
# If you have any questions, no contact me!!

import pygame
import random
import time

screen_width = 800
screen_height = 600
X,Y = 0,1
UP,DOWN = -1,1
LEFT,RIGHT = -1,1

#def start_game():
     
def text_screen(msg,xx,yy,color=(255,255,255),size=40 , screen=pygame.display.set_mode((screen_width,screen_height))):

     font = pygame.font.Font(None,size)
     text = font.render(msg,1,color)
     text_positions = text.get_rect(x = xx,y = yy)
     screen.blit(text,text_positions)


def start_screen():
  
  pygame.init()
  screen = pygame.display.set_mode((screen_width, screen_height))
  screen.blit((pygame.image.load('bggame.png').convert()),[0,0])
  #background1 =  pygame.image.load('bggame.png').convert()#change picture
  #screen.blit(background1,[0,0])
  keydown_sound = pygame.mixer.Sound('keydown.wav')
  pygame.display.set_caption('Welcom to Snake Game')
  text_screen('Feed the Snake',(screen_width/3.2),(screen_height/2.2),size=60)
  text_screen('Press any Key to Continue',(screen_width/3.5),screen_height/1.5)
  pygame.display.flip()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
      elif event.type == pygame.KEYDOWN:          
          keydown_sound.play()
          main_menu()
          
                    
def main_menu():
  
  global score,speed,life
  score = 0
  speed = 8
  life = 3
 
  pygame.init()
  screen = pygame.display.set_mode((screen_width, screen_height))
  keydown_sound = pygame.mixer.Sound('keydown.wav')
  screen.blit((pygame.image.load('bg_screen.png').convert()),[0,0])#change picture
  pygame.display.set_caption('Welcom to Snake Game')
  text_screen('Feed the Snake',(screen_width/3.2),(screen_height/1.7),size=60)
  text_screen('Press N to Start',(screen_width/2.65),screen_height/1.4)
  text_screen('Press Esc to Exit',(screen_width/2.7),screen_height/1.2)
  pygame.display.flip()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_n:
             keydown_sound.play()
             level_manu()        
        elif event.key == pygame.K_ESCAPE:
          pygame.quit()
          quit()
          
          
def level_manu():
               
     global level
     level = 0
     pygame.init()
     screen = pygame.display.set_mode((screen_width, screen_height))
     screen.blit((pygame.image.load('bg-lv.png').convert()),[0,0])
     keydown_sound = pygame.mixer.Sound('keydown.wav')     
     pygame.display.set_caption('Welcom to Snake Game')
     #text_screen('Press a or b or c to Start',(screen_width/2.65),screen_height/1.4)
     #text_screen('Press Esc to Main manu',(screen_width/2.7),screen_height/1.2)
     pygame.display.flip()
     
     while True:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
               elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                         keydown_sound.play()
                         level = 1 
                         init_screen()                
                    elif event.key == pygame.K_b:
                         keydown_sound.play()
                         level = 2 
                         init_screen()              
                    elif event.key == pygame.K_c:
                         keydown_sound.play()
                         level = 3 
                         init_screen()
                    elif event.key == pygame.K_ESCAPE:
                         keydown_sound.play()
                         main_menu()
     
     
def game_over():
  
  pygame.init()
  game_over_sound = pygame.mixer.Sound('gameover.wav')
  game_over_sound.play()
  screen = pygame.display.set_mode((screen_width, screen_height))  
  background1 = pygame.image.load('bggameover.png').convert()#change picture
  screen.blit(background1,[0,0])
  pygame.display.flip()
  pygame.display.set_caption('Welcom to Snake Game')
  text_screen('GAME OVER!',(screen_width/2.7),screen_height/2.4,color=(255,255,255),size=50)
  text_screen('Your Score is %3d'%score,(screen_width/2.7),screen_height/1.9)
  text_screen('press R to play again',(screen_width/2.95),screen_height/1.2)  
  pygame.display.flip()
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
          main_menu()
          

def init_screen():
  

  def setup_food():
    """ Create durian and store in the durian list """
    redbug_new_rect = food_rect.copy()
    pos_x = random.randrange(0,screen_width//40)*40
    pos_y = random.randrange(0,(screen_height-40)//40)*40    
    redbug_new_rect.topleft = (pos_x, pos_y)
    index_redbug = redbug_new_rect.collidelist(snake_body_positions)
    if index_redbug >= 0 or [pos_x,pos_y] in wall_positions or [pos_x,pos_y] in hole_positions or [pos_x,pos_y] in xfood_positions or [pos_x,pos_y] in goodfood_positions or [pos_x,pos_y] in badfood_positions :
         setup_food()
    else :
         food_positions.append(redbug_new_rect)
        

  def setup_goodfood():

    butterfly_new_rect = goodfood_rect.copy()
    pos_x = random.randrange(0,screen_width//40)*40
    pos_y = random.randrange(0,screen_height//40)*40
    butterfly_new_rect.topleft = (pos_x, pos_y)
    if butterfly_new_rect.collidelist(snake_body_positions)  >= 0 or [pos_x,pos_y] in wall_positions or [pos_x,pos_y] in hole_positions or [pos_x,pos_y] in food_positions or [pos_x,pos_y] in xfood_positions or [pos_x,pos_y] in badfood_positions:
         setup_goodfood()
    else :
         goodfood_positions.append(butterfly_new_rect)
         
        
  def setup_badfood():
       
       bee_new_rect = badfood_rect.copy()
       pos_x = random.randrange(0,screen_width//40)*40
       pos_y = random.randrange(0,screen_height//40)*40
       bee_new_rect.topleft = (pos_x, pos_y)
       if bee_new_rect.collidelist(snake_body_positions) >=0 or [pos_x,pos_y] in wall_positions or [pos_x,pos_y] in hole_positions or [pos_x,pos_y] in goodfood_positions or [pos_x,pos_y] in food_positions or [pos_x,pos_y] in xfood_positions:
            setup_badfood()
       else:
            badfood_positions.append(bee_new_rect)
            
                   
  def setup_xfood():

       xfood_new_rect = xfood_rect.copy()
       pos_x = random.randrange(0,screen_width//40)*40
       pos_y = random.randrange(0,screen_height//40)*40
       xfood_new_rect.topleft = (pos_x, pos_y)
       if xfood_rect.copy().collidelist(snake_body_positions) >=0 or [pos_x,pos_y] in wall_positions or [pos_x,pos_y] in hole_positions or  [pos_x,pos_y] in food_positions or [pos_x,pos_y] in goodfood_positions or [pos_x,pos_y] in badfood_positions:
            setup_xfood()
       else:
            xfood_positions.append(xfood_new_rect)
       
         
  def event_handler(event):
    """ handling the occured events """
    if event.type == pygame.QUIT:  # click close button at top corner of the screen
      pygame.quit()
      quit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP and snake_direction[Y] == 0: # occur when up key is pressed
        snake_direction[X] = 0
        snake_direction[Y] = UP
      elif event.key == pygame.K_DOWN and snake_direction[Y] == 0: 
        snake_direction[X] = 0
        snake_direction[Y] = DOWN
      elif event.key == pygame.K_LEFT and snake_direction[X] == 0: 
        snake_direction[X] = LEFT
        snake_direction[Y] = 0
      elif event.key == pygame.K_RIGHT and snake_direction[X] == 0: 
        snake_direction[X] = RIGHT
        snake_direction[Y] = 0
      # implement other directions here


  def text_screen(msg,xx,yy,color=(255,255,255),size=40 , screen=pygame.display.set_mode((screen_width,screen_height))):

     font = pygame.font.Font(None,size)
     text = font.render(msg,1,color)
     text_positions = text.get_rect(x = xx,y = yy)
     screen.blit(text,text_positions)

     
  def render():
    """ render all the game components """
    screen.blit(background ,[0,0]) # paint the background with white colour
    for position in wall_positions:
         screen.blit(wall_surface , position)
    for position in hole_positions:
         screen.blit(hole_surface , position)       
    for position in food_positions: 
      screen.blit(food_surface, position)
    for position in goodfood_positions: 
      screen.blit(goodfood_surface, position)
    for position in badfood_positions: 
      screen.blit(badfood_surface, position)
    for position in xfood_positions: 
      screen.blit(xfood_surface, position)
    for position in snake_body_positions: 
      screen.blit(snake_surface, position)
    text_screen('Score: %s   speed: %s   Life: %d' %(str(score),str(speed),life),20,10)    
    pygame.display.flip()     
     

  def check_collision():
    global score,speed,life
       
    """ Detect all the collision, you may check out of the boundary here """
    index_food = snake_body_positions[0].collidelist(food_positions)
    if index_food >= 0:
      eat_food_sound.play() #sound
      # Add code here to make the snake become bigger           
      score += 1
      pos = snake_rect.move(pos1.x - snake_rect.width, -(pos2.y - snake_rect.height))#snake is append body
      snake_body_positions.append(pos) 
      food_positions.pop(index_food)
      setup_food()
    index_goodfood = snake_body_positions[0].collidelist(goodfood_positions)
    if index_goodfood >=0:
         eat_goodfood_sound.play() #sound
         score += 2
         speed += 2
         pos = snake_rect.move(pos1.x - snake_rect.width, -(pos2.y - snake_rect.height))
         snake_body_positions.append(pos)
         goodfood_positions.pop(index_goodfood)
         setup_goodfood()             
    index_badfood = snake_body_positions[0].collidelist(badfood_positions)
    if index_badfood >=0:
         eat_badfood_sound.play() #sound
         score += -6
         speed += -1
         badfood_positions.pop(index_badfood)
         setup_badfood()
    index_xfood = snake_body_positions[0].collidelist(xfood_positions)
    if index_xfood >=0:
         eat_xfood_sound.play()  #sound       
         score += 5
         speed += 1
         pos = snake_rect.move(pos1.x - snake_rect.width, -(pos2.y - snake_rect.height))
         snake_body_positions.append(pos)
         xfood_positions.pop(index_xfood)
         setup_xfood()
    head = snake_body_positions.pop(0)
    index_snake = head.collidelist(snake_body_positions)
    if speed <= 0 :
         time.sleep(1)
         game_over()
    if index_snake >= 0: # gameover    
      attack_sound.play()      
      life -=1
      if life == 0:
           game_over()
    snake_body_positions.insert(0,head)
          
  
  def move():
    tail = snake_body_positions.pop()
    width = tail.width
    x = snake_body_positions[0].x + (width * snake_direction[0])
    y = snake_body_positions[0].y + (width * snake_direction[1])
    if x >= screen_width:
      x -= screen_width
    if x < 0:
      x += screen_width
    if [x,y] in wall_positions :# gameover
      attack_sound.play()
      time.sleep(1)
      game_over()
    elif y >= screen_height:             
         y -= screen_height
    elif y < 0:
         y += screen_height
    if [x,y] == hole_positions[0]:
         hole_sound.play()
         x,y = hole_positions[1]
    elif [x,y] == hole_positions[1]:
         hole_sound.play()
         x,y = hole_positions[0]
    tail.topleft = (x, y)
    snake_body_positions.insert(0, tail)


  def update():
    """ Update value of the game components """
    move()
    check_collision() 


  # Initialization
  
  pygame.init()
  screen = pygame.display.set_mode((screen_width, screen_height))
  pygame.display.set_caption("Feed the Snake")
  # level 1,2,3

  if level == 1:
       wall_positions = []
       hole_positions = [[120,240],[720,440]]

       eat_food_sound = pygame.mixer.Sound('redbug.wav')
       eat_goodfood_sound = pygame.mixer.Sound('eat_butterfly.wav')
       eat_badfood_sound = pygame.mixer.Sound('eat_bee.wav')
       eat_xfood_sound = pygame.mixer.Sound('honny.wav')
              
       food_surface = pygame.image.load("bug.png").convert_alpha()
       goodfood_surface = pygame.image.load("food_butterfly.png").convert_alpha()
       badfood_surface = pygame.image.load("bee.png").convert_alpha()
       xfood_surface = pygame.image.load("honny_food.png").convert_alpha()
       background = pygame.image.load('bg1.png').convert()
         

  elif level == 2:

       wall_positions = [[280,160],[280,120],[280,200],[240,200],[200,200],[600,360],[560,360],[520,360],[520,400],[520,440],[0,0],[40,0],[80,0],[120,0],[160,0],[200,0],[240,0],[280,0],[320,0],[360,0],[400,0],[440,0],[480,0],[520,0],[560,0],[600,0],[640,0],[680,0],[720,0],[760,0],[800,0],[0,560],[40,560],[80,560],[120,560],[160,560],[200,560],[240,560],[280,560],[320,560],[360,560],[400,560],[440,560],[480,560],[520,560],[560,560],[600,560],[640,560],[680,560],[720,560],[760,560],[800,560]]
       hole_positions = [[240,160],[560,400]]

       eat_food_sound = pygame.mixer.Sound('redbug.wav')
       eat_goodfood_sound = pygame.mixer.Sound('eat_butterfly.wav')
       eat_badfood_sound = pygame.mixer.Sound('eat_bee.wav')
       eat_xfood_sound = pygame.mixer.Sound('honny.wav')
              
       food_surface = pygame.image.load("bug2.png").convert_alpha()
       goodfood_surface = pygame.image.load("greenbug2.png").convert_alpha()
       badfood_surface = pygame.image.load("snail2.png").convert_alpha()
       xfood_surface = pygame.image.load("ant2.png").convert_alpha()
       background = pygame.image.load('bg2.png').convert()

       
  elif level == 3:
       
       wall_positions = [[280,160],[280,200],[240,200],[200,200],[600,360],[560,360],[520,360],[520,440],[0,0],[40,0],[80,0],[240,0],[280,0],[320,0],[440,0],[480,0],[520,0],[560,0],[760,0],[800,0],[0,560],[40,560],[80,560],[240,560],[280,560],[320,560],[440,560],[480,560],[520,560],[720,560],[760,560],[800,560]]
       hole_positions = [[240,160],[640,520]]

       eat_food_sound = pygame.mixer.Sound('redbug.wav')
       eat_goodfood_sound = pygame.mixer.Sound('eat_butterfly.wav')
       eat_badfood_sound = pygame.mixer.Sound('eat_bee.wav')
       eat_xfood_sound = pygame.mixer.Sound('honny.wav')
             
       food_surface = pygame.image.load("red3.png").convert_alpha()
       goodfood_surface = pygame.image.load("white3.png").convert_alpha()
       badfood_surface = pygame.image.load("violet3.png").convert_alpha()
       xfood_surface = pygame.image.load("oren3.png").convert_alpha()
       background = pygame.image.load('bg3.png').convert()
       
  
  
  attack_sound = pygame.mixer.Sound('ACCDENT.wav')
  hole_sound = pygame.mixer.Sound('holes.wav')


  snake_surface = pygame.image.load("snake1.png").convert()
  wall_surface = pygame.image.load("wall1.png").convert()
  hole_surface = pygame.image.load("hole.png").convert_alpha()
  
  food_rect = food_surface.get_rect()
  goodfood_rect = goodfood_surface.get_rect()
  badfood_rect = badfood_surface.get_rect()
  xfood_rect = xfood_surface.get_rect()
  snake_rect = snake_surface.get_rect()
  
  clock = pygame.time.Clock()
  snake_direction = [RIGHT,0]
  pos1 = snake_rect.move(400, 280)
  pos2 = snake_rect.move(pos1.x - snake_rect.width, pos1.y - snake_rect.height+40)#pos1.y - snake_rect.height
  pos3 = pos2.move(pos2.x - snake_rect.width, pos2.y - snake_rect.height)#pos2.y - snake_rect.height (320)
  snake_body_positions = [pos1, pos2, pos3]

  food_positions = []
  goodfood_positions = []
  badfood_positions = []
  xfood_positions = []
            
  setup_food()
  setup_goodfood()
  setup_badfood()
  setup_xfood()
  
  gameOver = False
  
    
  # Main game loop
  while not gameOver:
    clock.tick(speed)
    
    for event in pygame.event.get():
      event_handler(event)
    update()
    render()

    
# All the processes start here
start_screen()



