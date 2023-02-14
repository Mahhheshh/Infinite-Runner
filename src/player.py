import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,scalex, scaley, jump_sound):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = 62
        self.pos_y = 329
        self.run_sprites = [pygame.transform.scale(pygame.image.load(f"src/player/Run/Run ({i}).png").convert_alpha(), (scalex, scaley)) for i in range(1, 9)]
        self.jump_sprites = [pygame.transform.scale(pygame.image.load(f"src/player/Jump/Jump ({i}).png").convert_alpha(), (scalex, scaley)) for i in range(1, 13)]
        self.slide_sprites = [pygame.transform.scale(pygame.image.load(f"src/player/Slide/Slide ({i}).png").convert_alpha(), (scalex, scaley)) for i in range(1, 6)]
        self.current_run_sprite = 0
        self.current_jump_sprite = 0
        self.current_slide_sprite = 0
        self.gravity = 1
        self.jump_height = 10
        self.vel_y = self.jump_height
        self.is_running = True
        self.is_jumping = False
        self.is_sliding = False
        self.jump_sound = jump_sound
        self.image = self.run_sprites[int(self.current_run_sprite)]
        self.rect = self.image.get_rect(center=(62, 329))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.mask = pygame.mask.from_surface(self.image)
        self.animation()
        self.jump()
        self.slide()

    def animation(self):
        if self.is_jumping:
            self.jump_animation()
        elif self.is_sliding:
            self.slide_animation()
        else:
            self.run_animation()
        
    def jump_animation(self):
        self.current_jump_sprite += 0.25
        if self.current_jump_sprite >= len(self.jump_sprites):
            self.current_jump_sprite = 0
        self.image = self.jump_sprites[int(self.current_jump_sprite)]

    def run_animation(self):
        self.current_run_sprite += 0.75
        if self.current_run_sprite >= len(self.run_sprites):
            self.current_run_sprite = 0
            self.is_sliding = False
            self.is_running = True
        self.image = self.run_sprites[int(self.current_run_sprite)]
    
    def slide_animation(self):
        self.current_slide_sprite += 0.3
        if self.current_slide_sprite >= len(self.slide_sprites):
            self.is_sliding, self.is_running = False, True
            self.current_slide_sprite = 0
        self.image = self.slide_sprites[int(self.current_slide_sprite)]

    def jump(self):
        key_pressed = pygame.key.get_pressed()
        if (key_pressed[pygame.K_SPACE]) and (not self.is_jumping):
            self.is_running, self.is_jumping = False, True
            self.jump_sound.play()
        if self.is_jumping:
            self.rect.y -= self.vel_y
            self.vel_y -= self.gravity
            if self.vel_y < -self.jump_height:
                self.is_jumping, self.is_sliding = False, False
                self.is_running = True
                self.vel_y = self.jump_height
    
    def slide(self):
        if (pygame.key.get_pressed()[pygame.K_s]) or (pygame.key.get_pressed()[pygame.K_DOWN]):
            self.is_sliding = True