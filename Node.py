#a node is a cell in the grid which be empty,snake or apple.

class Node:
    def __init__(self, x, y, width, height):
        self.x = x;
        self.y = y;
        self.width = width;
        self.height = height;

    def display(self):
        print(self.x , self.y)






