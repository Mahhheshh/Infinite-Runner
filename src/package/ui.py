import pygame
class Text:
    def __init__(self, surf,file_name, size):
        pygame.init()
        self.text = pygame.font.Font(file_name, size)
        self.SCREEN = surf
        self.click = False

    def button(self, value, dest):
        render_surf = self.text.render(str(value), True, "Black")
        render_rect = render_surf.get_rect(center=dest)
        self.SCREEN.blit(render_surf, render_rect)
        pygame.draw.rect(self.SCREEN, (0, 0, 0), render_rect, 2)
    
    def labels(self, value, dest):
        render_surf = self.text.render(str(value), True, "Black")
        render_rect = render_surf.get_rect(center=dest)
        self.SCREEN.blit(render_surf, render_rect)


    