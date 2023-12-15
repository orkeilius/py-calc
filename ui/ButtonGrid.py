from utils.buttonList import ButtonList
from ui.TextButton import *
from ui.Button import *
import customtkinter

basicGrid = [
            [   "(",  ")", "clr", "del"],
            [   "e",  "π",  "x²",   "√"],
            [     7,    8,     9,   "%"],
            [     4,    5,     6,   "/"],
            [     1,    2,     3,   "*"],
            [   ",",    0,   "-",   "+"],
           ]

class ButtonGrid(customtkinter.CTkFrame):
    def __init__(self, parent, entryRef:customtkinter.CTkEntry, mode: str = "basic"):
        super().__init__(parent)
        if mode == "basic":
            grid = basicGrid

        # set grid config
        for col in range(len(grid[0])):
            self.grid_columnconfigure(col, weight=4)
        for row in range(2,len(grid) + 2):
            self.grid_rowconfigure(row, weight=4)

        # set Button
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                elem = ButtonList[grid[row][col]]
                elem.initButton(self,entryRef)
                elem.grid(row=row + 2, column=col, padx=5, pady=5, sticky=customtkinter.NSEW)


