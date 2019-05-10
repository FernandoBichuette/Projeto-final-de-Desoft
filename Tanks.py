import pygame
import random
import time
from os import path
import math

img_dir = path.join(path.dirname(__file__), 'img')

WIDTH = 480
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Classe Jogador que representa a nave
class Tanque_purple(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load(path.join(img_dir, "Tank_purple.png")).convert()
        self.image = player_img
        
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (100, 60))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        #Rotação
        
        
        # Centraliza embaixo da tela.
        self.rect.x = random.randint(0, 380) 
        self.rect.y = random.randint(0, 400)
        self.direita = False
        self.img_referencia = self.image
        self.velocidade_angular=0
        self.angulo= 0
        self.speedx = 0
        self.speedy = 0
        self.diagonal = False
        self.radius = 25
        
        
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.angulo += self.velocidade_angular
        
        
        self.image = pygame.transform.rotate( self.img_referencia, self.angulo)

        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
            
            
            
        if self.rect.top > HEIGHT:
            self.rect.top = HEIGHT
        if self.rect.bottom < 0:
            self.rect.bottom = 0
    
# Classe Jogador que representa a nave
class Tanque_green(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load(path.join(img_dir, "Tank_green.png")).convert()
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (100, 60))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.x = random.randint(0, 430) 
        self.rect.y = random.randint(0, 600)
        
        self.speedx = 0
        self.speedy = 0
        
        self.radius = 25
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
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
    def __init__(self, x, y):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        Bullet_img = pygame.image.load(path.join(img_dir, "Bullet.png")).convert()
        self.image = Bullet_img
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.y += self.speedy
        
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("TANQUE")

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'Tela_de_fundo.jpg')).convert()
background_rect = background.get_rect()

clock = pygame.time.Clock()

player1 = Tanque_purple()
player2 = Tanque_green()
# Cria um grupo de todos os sprites e adiciona a nave.
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)
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
                   player1.velocidade_angular = 1
                   player1.direita = True
                   
                if event.key == pygame.K_LEFT:
                   player1.velocidade_angular = -1
                   player1.direita = True   
                   
                if event.key == pygame.K_UP:
                    player1.diagonal = True
                    player1.speedx = math.cos(player1.angulo)
                    player1.speedy = math.sin(player1.angulo)
                    
                   
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_RIGHT:
                   player1.velocidade_angular = 0
                
                if event.key == pygame.K_LEFT:
                   player1.velocidade_angular = 0  
                   
                if event.key == pygame.K_UP:
                    player1.speedx = 0
                    player1.speedy = 0
               
        
        
        
        
        
        all_sprites.update()
        
        screen.blit(player1.image, [player1.rect.x, player1.rect.y])
        # A cada loop, redesenha o fundo e os sprites

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)   
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

finally:
    
    pygame.quit()
