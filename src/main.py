import pygame
from package.game import Game

pygame.init()
WIDTH, HEIGHT = 800, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCALEX, SCALEY = 60, 60
pygame.display.set_caption("Untitled Runner Game 1")

fps = pygame.time.Clock()
FPS = 30

background_image = pygame.image.load("environment/background (3).jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, 400))

menu_img = pygame.image.load("environment\menu_img.jpg")
menu_img =  pygame.transform.scale(menu_img, (WIDTH, 400))

icon_img = pygame.image.load("player/Run/Run (1).png")
pygame.display.set_icon(icon_img)

pygame.mixer.pre_init(44100, -16, 2, 512)
jump_sound = pygame.mixer.Sound("sounds\jump.wav")
jump_sound.set_volume(0.2)
score_sound = pygame.mixer.Sound("sounds\milestone.wav")
score_sound.set_volume(0.2)
gameover = pygame.mixer.Sound("sounds\gameover.wav")
gameover.set_volume(0.2)
game_stage = Game(SCREEN, SCALEX, SCALEY, background_image, menu_img, sounds=(jump_sound, score_sound, gameover))

def main():
    while True:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
        #     if event.type == pygame.KEYDOWN:
        #         if (event.key == pygame.K_ESCAPE) and (game_stage.state != "game_end"):
        #             game_stage.state = "menu"
        #         if (event.key == pygame.K_p) and (game_stage.state != "menu") and (game_stage.state != "game_end"):
        #             game_stage.state = "pause"
        #         if (event.key != pygame.K_p) and (event.key != pygame.K_ESCAPE) and (game_stage.state != "game_end"):
        #             game_stage.state = "main_game"
        #         if (game_stage.state == "game_end"):
        #             game_stage.state = "restart"
        # game_stage.state_manager()
        game_stage.gameloop()
        
        fps.tick(30)

if __name__ == "__main__":
    main()