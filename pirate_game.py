import pygame
pygame.init()

import random 

from datetime import datetime 

#main spirit  
class Turkey: 
    def __init__(self, image, position):

        original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(original_image, (original_image.get_width() * .5, original_image.get_height() * .5))
        self.position = position 
        self.rect = self.image.get_rect(center = position)

    def update_rect(self):
        self.rect = self.image.get_rect(center = self.position)

#background 
class Beach: 
    def __init__(self, image, position):

        background = pygame.image.load(image)
        self.image = pygame.transform.scale(background, (background.get_width() * 1.5, background.get_height() * 1))
        self.position = position 
        self.rect = self.image.get_rect(center = position)

    def update_rect(self):
        self.rect = self.image.get_rect(center = self.position)

#coins 
class Coin:
    def __init__(self, image, position):

        coin = pygame.image.load(image)
        self.image = pygame.transform.scale(coin, (coin.get_width() * .5, coin.get_height() * .5))
        self.position = position 
        self.rect = self.image.get_rect(center = position)

    def update_rect(self):
        self.rect = self.image.get_rect(center = self.position)

image_1 = r"C:\Users\rushi\.vscode\images\drake.png"
turkey_1 = Turkey(image_1, (200, 300))

image_2 = r"C:\Users\rushi\.vscode\images\beach.jpg"
beach_2 = Beach(image_2, (-700, 0))

image_3 = r"C:\Users\rushi\.vscode\images\bag.png"

#creates objects of the class Coin 
coin_list = []
for i in range(200):
    coin_list.append(Coin(image_3, (random.randint(-250, 1100), random.randint(250, 500))))

#screen 
screen = pygame.display.set_mode([600, 600])
screen.fill((255, 255, 255)) 

#score
score_font = pygame.font.SysFont("ComicSans", 36)

font = pygame.font.SysFont("ComicSans", 96)

#win
win = font.render("You Win!", True, (0, 100, 200))

win_bool = False

#lose
lose = font.render("You Lose.", True, (200, 100, 0))

lose_bool = False

#timer
clock = pygame.time.Clock()
current_time = 0 

score = 0

running = True 
while running: 

    current_time = pygame.time.get_ticks()
    #print(current_time)

    #background  
    screen.fill((255,255,255))
    screen.blit(beach_2.image, beach_2.position)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        else:
            pass 
        
        key = pygame.key.get_pressed()

        #move spirit up
        if key[pygame.K_w] == True and turkey_1.position[1] > 200:
            turkey_1.position = (turkey_1.position[0], turkey_1.position[1] - 5)
            turkey_1.update_rect()

        #move spirit left 
        if key[pygame.K_a] == True and turkey_1.position[0] > 0:
            turkey_1.position = (turkey_1.position[0] - 5, turkey_1.position[1])
            turkey_1.update_rect()

        #left moving background 
        if key[pygame.K_a] == True and turkey_1.position[0] == 0 and beach_2.position[0] < -200:
            beach_2.position = (beach_2.position[0] + 5, beach_2.position[1])
            beach_2.update_rect()

            for coin in coin_list:
                coin.position = (coin.position[0] + 5, coin.position[1])
                coin.update_rect()

        #move spirit down 
        if key[pygame.K_s] == True and turkey_1.position[1] < 470:
            turkey_1.position = (turkey_1.position[0], turkey_1.position[1] + 5)
            turkey_1.update_rect()
        
        #move spirit right 
        if key[pygame.K_d] == True and turkey_1.position[0] < 470:
            turkey_1.position = (turkey_1.position[0] + 5, turkey_1.position[1])
            turkey_1.update_rect()

        #right moving background 
        if key[pygame.K_d] == True and turkey_1.position[0] == 470 and beach_2.position[0] > -1320:
            beach_2.position = (beach_2.position[0] - 5, beach_2.position[1])
            beach_2.update_rect()

            for coin in coin_list:
                coin.position = (coin.position[0] - 5, coin.position[1])
                coin.update_rect()

        #holds coins to remove 
        removed_coins = []

        #appends coins that the sprite collides with to a seperate list 
        for coin in coin_list: 
            if turkey_1.rect.colliderect(coin.rect) and lose_bool == False: 
                score = score + 1
                #print(score)
                removed_coins.append(coin)

        #removes coins from the screen 
        for coin in removed_coins:
            coin_list.remove(coin)
    
    #coins
    for coin in coin_list:
        screen.blit(coin.image, coin.position)

    #pirate 
    screen.blit(turkey_1.image, turkey_1.position)
    
    #score 
    score_value = score_font.render("Score: " + str(score), True, (0, 100, 200))
    screen.blit(score_value, (50, 50))

    #time 
    score_value = score_font.render("Time: " + str(current_time//1000), True, (0, 100, 200))
    screen.blit(score_value, (350, 50))

    #win message 
    if score == 200 and lose_bool == False: 
        screen.blit(win, (100, 200))
        win_bool = True

    #lose message 
    if current_time > 20000 and win_bool == False:
        screen.blit(lose, (100, 200))
        lose_bool = True

    #access log and end game
    if current_time > 25000:
        with open("data.txt", "a") as file:
            now = datetime.now()
            file.write("Accessed: " + str(now.strftime("%B %d, %Y, %I:%M:%S %p")) + " Score: " + str(score) + "\n")
        #with open('data.txt','r') as reader:
            #print(reader.read())
        
        running = False 

    pygame.display.set_caption("Pirate's Booty")

    pygame.display.flip()
    #clock.tick(60)

running = False 