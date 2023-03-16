class Model:
    def __init__(self, colors, width, height):
        self.colors = {}
        self.grid = [[0] * width] * height
        self.selected_color = ''

    def add_color(self, color):
        self.colors[color] = color
    
    def change_grid_cell(self, x, y):
        self.grid[x][y] = self.selected_color