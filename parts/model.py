#import PIL
import os


# This same model will be used in play and create modes. In play mode, users will update the play_grid
# which will be compared against the filled_grid to determine correctness. In create mode, users will
# update the play grid until they are satisfied. Each grid willcontain integers values that each
# correspond to an indice in the colors array. The colors array will just be an array of hex values
# as strings
class Model:
    def __init__(self, type, colors, width, height):
        self.colors = []
        self.selected_color = ''
        self.play_grid = [[-1] * width] * height
        if type == 'fill_from_creation':
            self.filled_grid = self.generate_filled_grid()
        if type == 'fill_from_img':
            self.filled_grid = self.generate_filled_grid_from_img()
        if type == 'create_from_scratch': 
            self.play_grid = [[-1] * width] * height

    def add_color(self, color):
        self.colors[color] = color
    
    def change_grid_cell(self, x, y):
        self.grid[x][y] = self.colors.index()







    # Generates a correctly filled in grid from a creation
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
        
    # Files will be structured as follow:
    # For reading these, save the entire thing as a string, then use split on ":" and then split on the "|". Need to make sure the grid actually contains numbers and not strings as w3ll.
    #  colors : 1st array of colors | 2nd array of colors | ............. | nth array of colors
    #  #FFFFFF | #FFFFFF | #FFFFFF | #FFFFFF : 1 1 1 1 1 1 1 1 1 1 | 1 1 1 1 1 1 1 1 1 1 | ................. | 1 1 1 1 1 1 1 1 1 1
    
