from pygame import *

class gamSprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, p_speed):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (50, 50))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 

class Player(gamSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.speed            

class Enemy(gamSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 420:
            self.direction = 'right'
        if self.rect.x >= weight - 85:
            self.direction = 'left'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy2(gamSprite):
    direction = 'down'
    def update(self):
        if self.rect.y <= 90:
            self.direction = 'up'
        if self.rect.y >= height - 85:
            self.direction = 'down'
        
        if self.direction == 'down':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed


class Enemy3(gamSprite):
    direction = 'down'
    def update(self):
        if self.rect.y <= 90:
            self.direction = 'up'
        if self.rect.y >= height - 85:
            self.direction = 'down'
        
        if self.direction == 'down':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Wall(gamSprite):
    def __init__(self, color1, color2, color3, w_x, w_y, w_weight, w_height):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.w_weight = w_weight
        self.w_height = w_height
        self.image = Surface((self.w_weight, self.w_height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = w_x
        self.rect.y = w_y

    def ima(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
         

weight = 700
height = 500

window = display.set_mode((weight, height))
display.set_caption("Лабиринт кентавра")
#фон и персонажи
back = transform.scale(image.load('background.jpg'), (weight, height))

sp1 = Player("hero.png", 50, 400, 5)
sp2 = Enemy("cyborg.png", weight - 80, 270, 2)
sp4 = Enemy2 ("1.png", height - 5, 350, 2)
sp5 = Enemy3 ("22.jpg", height - 300, 350, 2)
sp3 = gamSprite("treasure.png", 550, 400, 5)
#стены
wall1 = Wall(0, 255, 0, 150, 20, 520, 10)
wall2 = Wall(0, 255, 0, 150, 20, 10, 350)
wall3 = Wall(0, 255, 0, 150, 470, 350, 10)
wall4 = Wall(0, 255, 0, 490, 350, 10, 120)
wall5 = Wall(0, 255, 0, 250, 350, 250, 10)
wall6 = Wall(0, 255, 0, 400, 120, 10, 230)
wall7 = Wall(0, 255, 0, 400, 120, 150, 10)
wall8 = Wall(0, 255, 0, 660, 20, 10, 110)
wall9 = Wall(0, 255, 0, 250, 250, 10, 100)
wall10 = Wall(0, 255, 0, 250, 250, 70, 10)
wall11 = Wall(0, 255, 0, 150, 150, 100, 10)
wall12 = Wall(0, 255, 0, 330, 150, 70, 10)



finish = False
htoto = True
clock = time.Clock()
fps = 60

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
dengi = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

#Текста

font.init()
font = font.SysFont('Arial', 70)
yxb = font.render('Гы :)', True, (5, 33, 6))
lose = font.render('ДЕТБИЛ', True, (20, 56, 21))
lose1 = font.render('ТЕБЕ КОНЕЦ', True, (5, 33, 6))

while htoto:
    for e in event.get():
        if e.type == QUIT:
            htoto = False
    if finish != True:
        window.blit(back, (0, 0))
        sp1.update()
        sp2.update()
        sp4.update()
        sp5.update()

        sp1.reset()
        sp2.reset()
        sp3.reset()
        sp4.reset()
        sp5.reset()

        wall1.ima()
        wall2.ima()
        wall3.ima()
        wall4.ima()
        wall5.ima()
        wall6.ima()
        wall7.ima()
        wall8.ima()
        wall9.ima()
        wall10.ima()
        wall11.ima()
        wall12.ima()

        if sprite.collide_rect(sp1, sp3):
            window.blit(yxb, (250, 250))
            finish = True
            dengi.play()

        if sprite.collide_rect(sp1, sp2) or sprite.collide_rect(sp1, sp4) or sprite.collide_rect(sp1, sp5) or sprite.collide_rect(sp1, wall1) or sprite.collide_rect(sp1, wall2) or sprite.collide_rect(sp1, wall3) or sprite.collide_rect(sp1, wall4) or sprite.collide_rect(sp1, wall5) or sprite.collide_rect(sp1, wall6) or sprite.collide_rect(sp1, wall7) or sprite.collide_rect(sp1, wall8) or sprite.collide_rect(sp1, wall9) or sprite.collide_rect(sp1, wall10) or sprite.collide_rect(sp1, wall11) or sprite.collide_rect(sp1, wall12):
            window.blit(lose, (160, 200))
            window.blit(lose1, (170, 270))
            finish = True
            kick.play()

    display.update()
    clock.tick(fps)