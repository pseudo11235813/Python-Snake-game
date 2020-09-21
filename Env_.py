from constants import *

def create_env():
    pygame.init()
    pygame.display.set_caption('SNAKE_ASS_BOII')

display_surface = pygame.display.set_mode((window_width , window_height))
clock = pygame.time.Clock()

def print_sth(text , random_color , sth , font):
    text = font.render(text, True, random_color)
    text_rect = text.get_rect()
    text_rect.center = (sth[0] , sth[1])
    display_surface.blit(text, text_rect)

def drawGrid():
    for x in range(0,window_width,snake_width):
        pygame.draw.line(display_surface,(15,15,15),(x,0),(x,window_height))
    for y in range(0,window_height,snake_width):
        pygame.draw.line((display_surface),(15,15,15),(0,y),(window_width,y))




