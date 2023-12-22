from utils.buttonList import ButtonList
from utils.gridsData import grids
from ui.TextButton import *
from ui.Button import *
import customtkinter

# store button position on grid

class ButtonGrid(customtkinter.CTkFrame):
    """ frame who handle button grid
    """
    
    
    second = 1
    mode: str
    entryRef : customtkinter.CTkEntry
    
    def __init__(self, parent, entryRef:customtkinter.CTkEntry, mode: str = "basic"):
        super().__init__(parent)
        self.entryRef = entryRef
        self.mode = mode
        
        if mode == "basic":
            self.drawGrid(grids[mode])
        else:
            self.drawGrid(grids[mode + str(self.second)])

    def drawGrid(self,grid):
        """ draw the given grid

        Args:
            grid (_type_): grid from grids variable
        """
        
        # set grid config
        for col in range(len(grid[0])):
            self.grid_columnconfigure(col, weight=1)
        for row in range(len(grid)):
            self.grid_rowconfigure(row, weight=1)

        # set Button
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if not grid[row][col] in ButtonList.keys(): #! for debug with not implemented button
                    continue
                
                elem = ButtonList[grid[row][col]]
                elem.initButton(self,self.entryRef)
                elem.grid(row=row, column=col, padx=5, pady=5, sticky=customtkinter.NSEW)
        
    def switchSecond(self):
        """ handeler to switch mode and redraw grid
        """
        self.second = (self.second + 1) % 2
        self.drawGrid(grids[self.mode + str(self.second)])