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
#3
#4
#5
