# represents an Apple in the grid
from constants import *


class Apfel:
    def __init__(self,x,y,width,height,color):
        self.x = x;
        self.y = y;
        self.width = width;
        self.height = height;
        self.color = color;

    def draw_apfel(self, surface):
        pygame.draw.rect(surface , self.color , (self.x , self.y , self.width , self.height))
