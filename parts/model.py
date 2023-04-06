import os
import pygame

# This same model will be used in play and create modes. In play mode, users will update the play_grid
# which will be compared against the filled_grid to determine correctness. In create mode, users will
# update the play grid until they are satisfied. Each grid willcontain integers values that each
# correspond to an indice in the colors array. The colors array will just be an array of hex values
# as strings
class Model:
    # Variable explanations:
    # Toolbar: List of colors available to create with
    # Selected Color: Currently selected color to paint with.
    # Play Grid: Grid of colors
    def __init__(self, type, colors, width, height):
        self.toolbar = []
        self.selected_color = ''
        self.play_grid = [[-1] * width] * height
        if type == 'fill_from_creation':
            self.filled_grid = self.generate_filled_grid()
        if type == 'create_from_scratch': 
            self.play_grid = [[-1] * width] * height

    # Adds/Changes one color in the colors
    # TODO: Make sure user cannot use more than 10 colors
    def add_color(self, color):
        self.colors[color] = color

    #Changes one cell on the grid to a new color
    def change_grid_cell(self, x, y):
        self.grid[x][y] = self.colors.index()


    # Generates a correctly filled in grid from a creation
    # Takes name (without file type) as input. Eg: test for test.txt
    def generate_filled_grid_from_creation():
        pass
    
    # Generates a correctly filled in grid from an image
    def generate_filled_grid_from_img():
        pass

    #Saves the current displayed image to a file to be used later, asks for a name when saving
    #Example:
    ##FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF |;#FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF |
    # This is two rows of 10 colors, thr rows being seperated by a ;
    def saveCreation(name):
        name = name + ".txt"
        filePath = os.getcwd() + "\SavedCreations" + '\\' + name
        file = open(filePath, "w") #Overwrites previous creation if it already existed
        
        for row in colors: #Saves all colors to file, seperates row members with a | and rows with a ;.
            for color in colors:
                file.write(color + " | ")
            file.write(";")

        file.close()

    #Sets selected_color to the one chosen on the toolbar
    def setSelectedColor(index):
        selected_color = toolbar[index]

    #Changes toolbar color at index to the desired color specified via hex code
    def setToolbarColor(index, hexCode):
        pass
    
    #Returns toolbar 
    def getToolbar():
        return toolbar

    #Returns selected color
    def getSelectedColor():
        return selected_color
    

