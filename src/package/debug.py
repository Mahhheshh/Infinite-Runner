import pygame

pygame.init()
text = pygame.font.Font(None, 30)

def render_text(info, dest, is_button=False):
    display_surf = pygame.display.get_surface()
    render_surf = text.render(str(info), True, "Black")
    render_rect = render_surf.get_rect(center=dest)
    display_surf.blit(render_surf, render_rect)
    if is_button:
        pygame.draw.rect(display_surf, (0, 0, 0), render_rect, 2)