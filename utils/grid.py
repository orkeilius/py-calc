from utils.buttonList import ButtonList
from entity.TextButton import *
from entity.Button import *
import customtkinter

basicGrid = [
            [   "(",  ")", "clr", "del"],
            [   "e",  "π",  "x²",   "√"],
            [     7,    8,     9,   "%"],
            [     4,    5,     6,   "/"],
            [     1,    2,     3,   "*"],
            [   ",",    0,   "-",   "+"],
           ]


def setGrid(app, entry:customtkinter.CTkEntry, mode: str = "basic"):
    if mode == "basic":
        grid = basicGrid
    
    # set grid config
    for col in range(len(grid[0])):
        app.grid_columnconfigure(col, weight=4)
    for row in range(2,len(grid) + 2):
        app.grid_rowconfigure(row, weight=4)

    # set Button
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            elem = ButtonList[grid[row][col]]
            Button = elem.generateButton(app,entry)
            Button.grid(row=row + 2, column=col, padx=5, pady=5, sticky=customtkinter.NSEW)


