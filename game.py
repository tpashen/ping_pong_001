#1
#2class Player(GameSprite): 
    def update_r(slef):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
    keys = key.gget_pressed()
    if keys[K_w] and self.rect.y > 5:
        self.rect.y -= self.speed
    if keys[K_s] and self.rect.y < win_height - 80:
        self.rect.y += self.speed
#3#Игровая сцена:
 back=(200,255,255)
 win_widht=600
 win_height=500
 window=display.set_mode((win_widht,win_height))
 window.fill(back)

 #Флаги отвечающие за состояние игры:
 game=True
 finish=False
 clock=time.Clock()
 FPS=60

 #Создание мяча и ракетки:
 racket1=Player('racket.png', 30, 200, 4, 50, 150)
 racket2=Player('racket.png', 520, 200, 4, 50, 150)
 ball=GameSprite('tenis_ball.png',200, 200, 4, 50, 50)

 font.init()
 font=font.Font('calibri.ttf', 35)
 lose1=font.render('Player 1 LOSE', True, (180,0,0))
 lose2=font.render('Player 2 LOSE', True, (180,0,0))
#4while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
#5
