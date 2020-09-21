from Snake import *
from Apfel import *
from Env_ import *
from pygame.locals import *
import sys

create_env()

snake_list = [[snake_x , snake_y],[snake_x - snake_width , snake_y],[snake_x - snake_width * 2 , snake_y]]
snake = Snake(snake_list,snake_width,snake_height,snake_color,snake_length)

def apfel_coords_generator(apfel_x, apfel_y):
    while [apfel_x, apfel_y] in snake.the_fucking_snake:
        apfel_x = round(random.randint(0, 760) / 15) * 15
        apfel_y = round(random.randint(0, 560) / 15) * 15
    return apfel_x, apfel_y

apfel_x, apfel_y = apfel_coords_generator(apfel_x, apfel_y)
apfel = Apfel(apfel_x , apfel_y , apfel_width , apfel_height , apfel_color)

x = snake_list[-1][0]
y = snake_list[-1][1]

def event_Handeling():
    global game_state,direction,snake,snake_list,x,y,apfel
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT and direction != 0:
                direction = 1
            elif event.key == K_RIGHT and direction != 1:
                direction = 0
            elif event.key == K_DOWN and direction != 2:
                direction = 3
            elif event.key == K_UP and direction != 3:
                direction = 2
            elif event.key == K_SPACE :
                game_state = 'in'
            elif event.key == K_ESCAPE:
                quit()

def game_over_event_handeling():
    global game_state, direction, snake, snake_list, x, y, apfel,apfel_x,apfel_y
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                del snake
                snake_list = [[snake_x, snake_y], [snake_x - snake_width, snake_y],[snake_x - snake_width * 2, snake_y]]
                snake = Snake(snake_list, snake_width, snake_height, snake_color, snake_length)
                x = snake_list[-1][0]
                y = snake_list[-1][1]
                del apfel
                apfel_x, apfel_y = apfel_coords_generator(round(random.randint(0, 730) / 15) * 15,round(random.randint(0, 730) / 15) * 15)
                apfel = Apfel(apfel_x, apfel_y, apfel_width, apfel_height, apfel_color)
                direction = 2
                game_state = 'start'

            elif event.key == K_ESCAPE:
                quit()


def move():
    global x,y
    x,y = snake.change_coords(x,y,direction)
    snake.add_cell([x,y])

def apfel_is_eaten():
    global apfel
    global apfel_x,apfel_y
    if snake.eat_apple(apfel_x , apfel_y) == True:
        del apfel
        apfel_x , apfel_y = apfel_coords_generator(apfel_x , apfel_y)
        apfel = Apfel(apfel_x, apfel_y, apfel_width, apfel_height, apfel_color)

def check_lose():
    global game_state
    if snake.is_crashed() or snake.is_out():
        game_state = 'over'
        direction = 4

def game_start():
    global game_state,random_color
    display_surface.fill(grey)
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    rand_color = (r, g, b)
    print_sth("press 'ESC' to quit at anytime" , green , (90 , 10) , font_4)
    print_sth('SNAAKE BOII' , rand_color , (window_width / 2 , window_height / 2 - 200) , font_1)
    print_sth('The Sneakiest MF in the North' , rand_color , (window_width / 2 , window_height / 2 - 120) , font_2)
    print_sth('press SPACE to play..' , rand_color , (window_width / 2 , window_height / 2 + 30) , font_2)
    event_Handeling()
    pygame.display.update()
    clock.tick(FPS)


def game_in():
    display_surface.fill(grey)
    drawGrid()
    event_Handeling()
    move()
    snake.draw_snake(display_surface)
    apfel.draw_apfel(display_surface)
    apfel_is_eaten()
    check_lose()
    pygame.display.update()
    clock.tick(FPS)

def game_over():
    global x,y
    display_surface.fill(grey)
    drawGrid()
    snake.draw_snake(display_surface)
    apfel.draw_apfel(display_surface)
    game_over_event_handeling()
    print_sth('aight, you fucking suck...', (0,130,0,0), (window_width / 2, window_height / 2) , font_2)
    print_sth("press 'space' to go back to main menu or just gtfo..." , red , (window_width / 2  , window_height / 2 + 40) , font_3)
    print_sth('press \'ESC\' to quit at anytime' , green , (90 , 10) , font_4)
    pygame.display.update()
    clock.tick(FPS)


def game_loop():
    while game_isActive == True:
        print(game_state)
        if game_state == 'start':
            game_start()
        if game_state == 'in':
            game_in()
        if game_state =='over' :
            game_over()

game_loop()









