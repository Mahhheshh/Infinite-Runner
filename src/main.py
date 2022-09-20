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

# background_music = pygame.mixer.Sound()
# jump_sound = pygame.mixer.Sound()
# score_sound = pygame.mixer.Sound()
# game_end_sound = pygame.mixer.Sound()

game_stage = Game(SCREEN, SCALEX, SCALEY, background_image, menu_img)

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
        
        game_stage.run()
        
        fps.tick(30)

if __name__ == "__main__":
    main()