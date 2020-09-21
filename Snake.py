from constants import *

class Snake:
    def __init__(self,the_fucking_snake,width,height,color,length):
        self.the_fucking_snake = the_fucking_snake;
        self.width = width;
        self.height = height;
        self.color = color;
        self.length = length;

    def add_cell(self,cell):
        self.the_fucking_snake.append(cell)
        if len(self.the_fucking_snake) > self.length:
            del self.the_fucking_snake[0]

    def draw_snake(self, surface):
        for cell in self.the_fucking_snake:
            pygame.draw.rect(surface , self.color , (cell[0] , cell[1] , self.width , self.height))

    def change_coords(self ,x ,y ,direction):
        if direction == 1:
            x -= snake_speed
        if direction == 0:
            x += snake_speed
        if direction == 2:
            y -= snake_speed
        if direction == 3:
            y += snake_speed
        return (x,y)

    def is_out(self):
        global game_state,snake_speed
        if self.the_fucking_snake[-1][0] + self.width > window_width or self.the_fucking_snake[-1][0] < 0 or self.the_fucking_snake[-1][1] + self.height > window_height or self.the_fucking_snake[-1][1] < 0:
            return True
    def is_crashed(self):
        global game_state,snake_speed
        for cell in self.the_fucking_snake[0:len(self.the_fucking_snake) - 2]:
            if self.the_fucking_snake[-1][0] == cell[0] and self.the_fucking_snake[-1][1] == cell[1]:
                return True
    def eat_apple(self,apfel_x , apfel_y):
        if self.the_fucking_snake[-1][0] == apfel_x and self.the_fucking_snake[-1][1] == apfel_y:
            self.length += 1
            return True







