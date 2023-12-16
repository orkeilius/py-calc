from utils.buttonList import ButtonList
from ui.TextButton import *
from ui.Button import *
import customtkinter

grids = { "basic" :
        [
            [   "(",  ")", "clr", "del"],
            [   "e",  "π",  "x²",   "√"],
            [     7,    8,     9,   "%"],
            [     4,    5,     6,   "/"],
            [     1,    2,     3,   "*"],
            [   ",",    0,   "-",   "+"],
        ],
    "scientific":
        [
            [ "2de",   "(",  ")", "clr", "del"],
            [ "sin", "cos","tan", "|x|", "mod"],
            [  "xʸ",   "e",  "π",   "!",   "√"],
            [  "x²",     7,    8,     9,   "%"],
            [ "10ʸ",     4,    5,     6,   "/"],
            [ "log",     1,    2,     3,   "*"],
            [  "ln",   ",",    0,   "-",   "+"],
        ]



}
class ButtonGrid(customtkinter.CTkFrame):
    
    
    def __init__(self, parent, entryRef:customtkinter.CTkEntry, mode: str = "basic"):
        super().__init__(parent)
        grid = grids[mode]

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
                elem.initButton(self,entryRef)
                elem.grid(row=row, column=col, padx=5, pady=5, sticky=customtkinter.NSEW)
        
