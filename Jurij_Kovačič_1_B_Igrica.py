import pygame
import time 


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
 
class Player(pygame.sprite.Sprite):
    
   
    def __init__(self):
       
 
        
        super().__init__()
 
       
        width = 40
        height = 60
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
 
        
        self.rect = self.image.get_rect()
 
        
        self.change_x = 0
        self.change_y = 0
 
        
        self.level = None
 
    def update(self):
        
        
        self.calc_grav()
 
        
        self.rect.x += self.change_x
 
        
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                
                self.rect.left = block.rect.right
 
        
        self.rect.y += self.change_y
 
        
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            
            self.change_y = 0
 
    def calc_grav(self):
        
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
 
    def jump(self):
        
 
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
 
    
    def go_left(self):
        
        self.change_x = -6
 
    def go_right(self):
        
        self.change_x = 6
 
    def stop(self):
        
        self.change_x = 0
 
 
class Platform(pygame.sprite.Sprite):
    
 
    def __init__(self, width, height):
        
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
 
 
class Level():
    
 
    def __init__(self, player):
        
            
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
 
        
        self.world_shift = 0
 
    
    def update(self):
        
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        
 
        
        screen.fill(BLUE)
 
        
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
 
    def shift_world(self, shift_x):
        
        
 
        
        self.world_shift += shift_x
 
    
        for platform in self.platform_list:
            platform.rect.x += shift_x
 
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x


 

class Level_01(Level):
 
 
    def __init__(self, player):
     
 
       
        Level.__init__(self, player)
 
 
        
        level = [
                 [43, 150, 1120, 280],
                 [143, 67, 1000, 280],
                 [123, 86, 1245, 500],
                 [432, 34, 1379, 400],
                 [321, 34, 1234, 500],
                 [123, 65, 1567, 280],
                 [232, 43, 1468, 280],
                 [432, 23, 1587, 500],
                 [324, 54, 1654, 400],
                 [223, 34, 1567, 500],
                 [210, 56, 1678, 280],
                 [210, 34, 1907, 280],
                 [210, 23, 2567, 500],
                 [210, 34, 2098, 400],
                 [210, 24, 2498, 500],
                 [210, 54, 2254, 280],
                 [210, 12, 2678, 280],
                 [210, 13, 2789, 500],
                 [210, 15, 2954, 400],
                 [210, 23, 3098, 500],
                 [210, 23, 3675, 280],
                 [210, 46, 3567, 280],
                 [210, 32, 3789, 500],
                 [210, 23, 3975, 400],
                 [210, 13, 4000, 500],
                 [210, 65, 4326, 280],
                 [210, 67, 4456, 280],
                 [210, 45, 4567, 500],
                 [210, 65, 4768, 400],
                 [210, 43, 4976, 500],
                 [210, 54, 5354, 280],
                 [210, 34, 5234, 280],
                 [210, 23, 5567, 500],
                 [210, 34, 5687, 400],
                 [210, 34, 5897, 500],
                 [210, 45, 6000, 280],
                 [210, 34, 6457, 280],
                 [210, 65, 6890, 500],
                 [210, 34, 6790, 400],
                 [210, 45, 300, 500],
                 [210, 34, 7000, 280],
                 [210, 56, 200, 280],
                 [210, 23, 7854, 500],
                 [210, 12, 7234, 400],
                 [210, 43, 7457, 500],
                 [210, 54, 7434, 280],
                 [210, 56, 7986, 280],
                 [210, 34, 8000, 500],
                 [210, 40, 8231, 400],
                 [210, 32, 8432, 500],
                 [210, 12, 8546, 280],
                 [210, 23, 8743, 280],
                 [210, 76, 8943, 500],
                 [210, 65, 9000, 400],
                 [210, 45, 9086, 500],
                 [210, 34, 9123, 280],
                 [210, 40, 9213, 280],
                 [210, 34, 9321, 500],
                 [210, 65, 9532, 400],
                 [210, 43, 9654, 500],
                 [210, 45, 9854, 280],
                 [210, 56, 9999, 280],
                 [210, 34, 10111, 500],
                 [210, 70, 11000, 400],
                                  ]
 
        
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
 
 

 
 
def main():
    
    pygame.init()
 
    
    font = pygame.font.Font(None, 50)
    
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("speedy game")
 

    
    
    player = Player()
 
    
    def time_convert(sec):
        mins = sec // 60
        sec = sec % 60
        hours = mins // 60
        mins = mins % 60
        čas = ('Vzelo ti je:{0}:{1}:{2}'.format(int(hours),int(mins),sec))
        
    
    level_list = []
    level_list.append(Level_01(player))
    
        
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
 
    player.rect.x = 30
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
 
    navodilo1_surf = font.render('BRAVO prišel si do konca', False, (64, 64, 64))
    navodilo1_rect = navodilo1_surf.get_rect(center = (400, 450))
    navodilo_surf = font.render(' pritisni katerokoli tipko, da nadaljuješ', False, (64, 64, 64))
    navodilo_rect = navodilo_surf.get_rect(center = (400, 500))
    done = False
    game_active = True
    
    clock = pygame.time.Clock()
 
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:

                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
            if game_active == False:
                player.stop()
                if event.type == pygame.KEYDOWN:
                    game_active = True
                    done = True #to lahko comment outamo
        if game_active == True:
            
            active_sprite_list.update()
     
            
            current_level.update()
     
            
            if player.rect.right >= 500:
                diff = player.rect.right - 500
                player.rect.right = 500
                current_level.shift_world(-diff)
     
            
            if player.rect.left <= 120:
                diff = 120 - player.rect.left
                player.rect.left = 120
                current_level.shift_world(diff)
     
           
            current_position = player.rect.x + current_level.world_shift
            if current_position < -9999:
                game_active = False
         
            current_level.draw(screen)
            active_sprite_list.draw(screen)
 
        else:
            
            screen.fill(RED)
            Level.shift_world(current_level, 135)
            screen.blit(navodilo_surf, navodilo_rect)
            screen.blit(navodilo1_surf, navodilo1_rect)
            player.rect.x = 0
            
        clock.tick(60)
 
       
        pygame.display.flip()
 
    pygame.quit()
 
if __name__ == "__main__":
    main()