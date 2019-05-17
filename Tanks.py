import pygame
import random
import time
from os import path
import math

img_dir = path.join(path.dirname(__file__), 'img')

WIDTH = 1000
HEIGHT = 900
FPS = 100

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Classe Jogador que representa a nave
class Tanque(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self,img):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        img =pygame.image.load(path.join(img_dir, img)).convert()
        
        # Diminuindo o tamanho da imagem.
        self.image = img
        self.image = pygame.transform.scale(img,(50, 47))
        
        

        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
                       
        # Centraliza embaixo da tela.
        self.direita = False
        self.img_referencia = self.image
        
        #Velocidades
        self.velocidade_angular = 0              
        self.angulo= 0
        self.x = random.randint(0, 1000) 
        self.speed = 0
        self.y = random.randint(0, 900)
        self.diagonal = False       
        self.radius = 25
        
        
       
        
    def update(self):
        self.angulo += self.velocidade_angular
        self.angulo1 = math.radians(self.angulo)
        self.x += math.sin((self.angulo1))*self.speed
        self.y += math.cos((self.angulo1))*self.speed
        self.rect.centerx = self.x
        self.rect.centery = self.y
        
 
       
        #Rotação
        loc = self.rect.center       
        self.image=pygame.transform.rotate( self.img_referencia, self.angulo)
        self.rect = self.image.get_rect()
        self.rect.center=loc    

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
                                           
        if self.rect.top > HEIGHT:
            self.rect.top = HEIGHT
        if self.rect.bottom < 0:
            self.rect.bottom = 0
            
            
            
            
    

            
# Classe Bullet que representa os tiros
class Bullet(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y, angulo):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        Bullet_img = pygame.image.load(path.join(img_dir, "Bullet.png")).convert()
        self.image = Bullet_img
        
        #Tamanho do bullet
        self.image = pygame.transform.scale(Bullet_img, (10, 10))
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centery = y
        self.rect.centerx = x
        self.speed = -5
        self.vx = math.sin(angulo)*self.speed
        self.vy = math.cos(angulo)*self.speed
    # Metodo que atualiza a posição da navinha
    def update(self):
        
        self.rect.centery += self.vy
        self.rect.centerx += self.vx
        
        
        # Se o tiro passar do inicio da tela, morre.
        #if self.rect.bottom < 0:
         #   self.kill()

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("TANQUE")

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'Tela_de_fundo.jpg')).convert()
background_rect = background.get_rect()

clock = pygame.time.Clock()

player1 = Tanque('Tank_purple.png')
player2 = Tanque('Tank_green.png')
#bullet = Bullet()
# Cria um grupo de todos os sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)
#all_sprites.add(bullet)
# Comando para evitar travamentos.
try:
    
    # Loop principal.

    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                running = False

            

          # A cada loop, redesenha o fundo e os sprites
          
          

                
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                 
                if event.key == pygame.K_RIGHT:
                   player1.velocidade_angular -= 1
                   player1.direita = True
                
                if event.key == pygame.K_a:
                    player2.velocidade_angular = 1
                    player2.direita = True
                
                   
                if event.key == pygame.K_LEFT:
                   player1.velocidade_angular += 1
                   player1.direita = True   
                
                if event.key == pygame.K_d:
                    player2.velocidade_angular = -1
                    player2.direita = True
                   
                   
                if event.key == pygame.K_UP:
                    player1.speed -= 1.5
                    
                if event.key == pygame.K_DOWN:
                    player1.speed += 1.5
                    
                if event.key == pygame.K_w:
                    player2.speed = -1.5
                     
                if event.key == pygame.K_s:
                    player2.speed = 1.5
                    
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player1.rect.centerx, player1.rect.centery, player1.angulo1)
                    bullets.add(bullet)
                    all_sprites.add(bullets)
                   
                if event.key == pygame.K_q:
                    bullet = Bullet(player2.rect.centerx, player2.rect.centery, player2.angulo1)
                    bullets.add(bullet)
                    all_sprites.add(bullets)
                    
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_RIGHT:
                   player1.velocidade_angular += 1
                
                if event.key == pygame.K_LEFT:
                   player1.velocidade_angular -= 1  
                   
                if event.key == pygame.K_UP:
                    player1.speed += 1.5
                
                if event.key == pygame.K_DOWN:
                    player1.speed -= 1.5
                    
                if event.key == pygame.K_w:
                    player2.velocidade_angular = 0
                    player2.speed = 0
                    
                if event.key == pygame.K_s:
                    player2.velocidade_angular = 0
                    player2.speed = 0

               
                if event.key == pygame.K_a:
                    player2.velocidade_angular = 0
                    
                if event.key == pygame.K_d:
                    player2.velocidade_angular = 0
        
        
        all_sprites.update()

        # A cada loop, redesenha o fundo e os sprites

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)   
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

finally:
    
    pygame.quit()
