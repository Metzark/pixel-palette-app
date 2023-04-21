import os

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
    def __init__(self, type, colors, width, height):
        self.colors = []
        self.selected_color = ''
        self.play_grid = [[-1] * width] * height
        if type == 'fill_from_creation':
            self.filled_grid = self.generate_filled_grid()
            
        if type == 'create_from_scratch': 
            self.play_grid = [[-1] * width] * height

    # Adds/Changes one color in the colors
    # TODO: Make sure user cannot use more than 10 colors
    def add_color(self, color):
        if(len(colors) >= 10):   #Colors list can only contain up to 10 colors
            return false
        else:
            colors.append(color) #Append to end if colors has 9 or less colors

    #Changes one cell on the grid to a new color
    def change_grid_cell(self, x, y):
        self.grid[x][y] = selected_color


    #Generates a completely default grid of white & default colors array
    def generate_default_grid(self):
        for row in self.grid:
            for element in row:
                element = "#FFFFFF" #Creates a grid of white pixels

        #Default colors: [Red, Orange, Yellow, Green, Blue, Purple, Violet, Brown, White, Black]
        colors = ["#FF0000","#FF7F00","FFFF00","#00FF00","0000FF","4B0082","9400D3","#964B00","#FFFFF","#00000"]

        selectedColor = colors[0] #Sets default selected color to red
        
    # Generates a correctly filled in grid from a creation
    # Takes name (without file type) as input. Eg: test for test.txt
    def generate_filled_grid_from_creation(self, name):
        name = name + ".txt"
        filePath = os.getcwd() + "\SavedCreations" + '\\' + name
        file = open(filePath, "r")

        gridString = file.readline()
        #TODO: Implement creation of grid from string
        colors = file.readline().split(" | ")
        
        file.close()

    #Saves the current displayed image to a file to be used later, asks for a name when saving
    #Example:
    ##FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF |;#FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF | #FFFFF |
    # This is two rows of 10 colors, thr rows being seperated by a ;
    def saveCreation(self, name):
        name = name + ".txt"
        filePath = os.getcwd() + "\SavedCreations" + '\\' + name
        file = open(filePath, "w") #Overwrites previous creation if it already existed
        
        for row in self.play_grid: #Saves all colors to file, seperates row members with a | and rows with a ;.
            for color in row:
                file.write(color + " | ")
            file.write(";")

        for color in colors:
            file.write(color + " | ")
            
        file.close()

    #Sets selected_color to the one chosen on the toolbar
    def setSelectedColor(color):
        selected_color = color

    #Changes toolbar color at index to the desired color specified via hex code
    def setToolbarColor(index, hexCode):
        colors[index] = hexCode

    # Generates a correctly filled in grid from a creation
    def generate_filled_grid_from_creation():
        pass

    
    #Returns toolbar color at index
    def getToolbarColor(index):
        return colors[index]


    #Returns selected color
    def getSelectedColor():
        return selected_color
    


    # Files will be structured as follow:
    # For reading these, save the entire thing as a string, then use split on ";" and then split on the "|". Need to make sure the grid actually contains numbers and not strings as w3ll.
    #  colors : 1st array of colors | 2nd array of colors | ............. | nth array of colors
    #  #FFFFFF | #FFFFFF | #FFFFFF | #FFFFFF : 1 1 1 1 1 1 1 1 1 1 | 1 1 1 1 1 1 1 1 1 1 | ................. | 1 1 1 1 1 1 1 1 1 1
    

