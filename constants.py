import random,pygame
pygame.init()

#colors
green = (0,200,0,12)
red = (255,0,0)
blue = (0,0,255)
grey = (35,35,35)

#Envirenment ccnstants
FPS = 30
window_width =810
window_height = 600
font_1 = pygame.font.Font(r'C:\Users\kais\Desktop\python _Scripts\FONTS_\game_over.ttf',180)
font_2 = pygame.font.Font(r'C:\Users\kais\Desktop\python _Scripts\FONTS_\Positive System.otf', 40)
font_3 = pygame.font.Font(r'C:\Users\kais\Desktop\python _Scripts\FONTS_\Positive System.otf', 25)
font_4 = pygame.font.Font(r'C:\Users\kais\Desktop\python _Scripts\FONTS_\Positive System.otf', 10)
game_state = 'start'
game_isActive = True

#snake constants
snake_color = green
snake_x = window_width / 2
snake_y = window_height / 2
snake_width = 15
snake_height = 15
snake_speed = 15
snake_length = 3
speed_x = 0
speed_y = 0
direction = 2

#apfel constants
apfel_color = red
apfel_x = round(random.randint(0,760)/15)*15
apfel_y = round(random.randint(0,560)/15)*15
apfel_width = 15
apfel_height = 15

