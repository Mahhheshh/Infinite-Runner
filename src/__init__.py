import pygame
from .game import Game

pygame.init()
WIDTH, HEIGHT = 800, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCALEX, SCALEY = 60, 60
pygame.display.set_caption("Untitled Runner Game 1")

fps = pygame.time.Clock()
FPS = 30

background_image = pygame.image.load("src/environment/background.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, 400))

menu_img = pygame.image.load("src/environment/menu_img.jpg")
menu_img =  pygame.transform.scale(menu_img, (WIDTH, 400))

icon_img = pygame.image.load("src/player/Run/Run (1).png")
pygame.display.set_icon(icon_img)

pygame.mixer.pre_init(44100, -16, 2, 512)
jump_sound = pygame.mixer.Sound("src/sounds/jump.wav")
jump_sound.set_volume(0.2)
score_sound = pygame.mixer.Sound("src/sounds/milestone.wav")
score_sound.set_volume(0.2)
gameover = pygame.mixer.Sound("src/sounds/gameover.wav")
gameover.set_volume(0.2)

def create_game() -> Game:
    game_stage = Game(SCREEN, SCALEX, SCALEY, background_image, menu_img, sounds=(jump_sound, score_sound, gameover))
    return game_stage
