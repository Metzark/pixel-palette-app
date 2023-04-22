import os
from tkinter import filedialog
from tkinter import *
from data import airtable

# This same model will be used in play and create modes. In play mode, users will update the play_grid
# which will be compared against the filled_grid to determine correctness. In create mode, users will
# update the play grid until they are satisfied. Each grid willcontain integers values that each
# correspond to an indice in the colors array. The colors array will just be an array of hex values
# as strings
class Model:
    # Variable explanations:
    # Colors: List of colors available to create with
    # Selected Color: Currently selected color to paint with.
    # Play Grid: Grid of colors
    def __init__(self, type, text):
        self.colors = []
        self.selected_color = IntVar()
        self.play_grid = []
        self.filled_grid = []
        if type == 'fromscratch':
            self.generate_default_grid()
        if type == 'updatecreation':
            self.generate_from_creation(text)
        if type == 'fill_from_creation': #only used in play mode
            self.generate_grids_play(text)

    #Generates a completely default grid of white & default colors array
    def generate_default_grid(self):
        #Default colors: [Red, Orange, Yellow, Green, Blue, Purple, Violet, Brown, White, Black]
        self.colors = ["#FF0000","#FF7F00","#FFFF00","#00FF00","#0000FF","#4B0082","#9400D3","#964B00","#FFFFFF","#000000"]
        for i in range(0, 20):
            self.play_grid.append([-1, -1, -1, -1, -1, -1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])

    # Generates a correctly filled in grid from a creation and gets colors
    def generate_from_creation(self, text):

        colors = text[0].split(':')[0]
        colors = colors.split('|')
        self.colors = colors
        grid = text[0].split(':')[1]
        grid = grid.split('|')
        for i in range(0, 20):
            grid[i] = grid[i].split(' ')
            for j in range(0, 20):
                grid[i][j] = int(grid[i][j])
        self.play_grid = grid

    def generate_grids_play(self, text):
        for i in range(0, 20):
            self.play_grid.append([-1, -1, -1, -1, -1, -1, -1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
        colors = text[0].split(':')[0]
        colors = colors.split('|')
        self.colors = colors
        grid = text[0].split(':')[1]
        grid = grid.split('|')
        for i in range(0, 20):
            grid[i] = grid[i].split(' ')
            for j in range(0, 20):
                grid[i][j] = int(grid[i][j])
        self.filled_grid = grid

    #Sets selected_color to the one chosen on the toolbar
    def setSelectedColor(self, color):
        self.selected_color = color

    #Changes toolbar color at index to the desired color specified via hex code
    def setToolbarColor(self, index, hexCode):
        self.colors[index] = hexCode

        #Changes one cell on the grid to a new color
    def change_grid_cell(self, x, y):
        self.play_grid[x][y] = self.selected_color.get()

    def get_grid_cell_color(self, x, y):
        if self.play_grid[x][y] == -1:
            return '#ffffff'
        return self.getToolbarColor(self.play_grid[x][y])
    
    # returns the numeric value for the cell in the filled grid, for play
    def get_cell_value(self, x, y):
        return self.filled_grid[x][y]

    #Returns toolbar color at index
    def getToolbarColor(self, index):
        return self.colors[index]

    #Returns selected color
    def getSelectedColor(self):
        return self.selected_color.get()
    
    def check_completed_play(self):
        for x in range(0,20):
            for y in range(0,20):
                if(self.play_grid[x][y] != self.filled_grid[x][y]):
                    return False
        return True
    
    #Saves the current displayed image to a file and returns file name
    #Example:
    ##FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF |;#FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF |
    # This is two rows of 10 colors, thr rows being seperated by a ;
    def saveCreation(self):
        path = filedialog.asksaveasfilename()

        file = open(path, "w") #Overwrites previous creation if it already existed
        text = ""
        for color in self.colors: #Saves colors to file, separated by |, ends with :
            text += (color + "|")
        
        text = text[:-1]
        text += ':'
        
        for i in self.play_grid: #Saves grid to file, rows separated by |
            row = ""
            for j in i:
                row += (str(j) + " ")
            row = row.strip()
            row += '|'
            text += row
        file.write(text)
        file.close()
        return path
    
    def upload_creation(self, path, user):
        airtable.upload_creation(path, user)

    


    # Files will be structured as follow:
    # For reading these, save the entire thing as a string, then use split on ";" and then split on the "|". Need to make sure the grid actually contains numbers and not strings as w3ll.
    #  colors : 1st array of colors | 2nd array of colors | ............. | nth array of colors
    #  #FFFFFF | #FFFFFF | #FFFFFF | #FFFFFF : 1 1 1 1 1 1 1 1 1 1 | 1 1 1 1 1 1 1 1 1 1 | ................. | 1 1 1 1 1 1 1 1 1 1
    

 # # Adds/Changes one color in the colors
    # # TODO: Make sure user cannot use more than 10 colors
    # def add_color(self, color):
    #     if(len(colors) >= 10):   #Colors list can only contain up to 10 colors
    #         return false
    #     else:
    #         colors.append(color) #Append to end if colors has 9 or less colors