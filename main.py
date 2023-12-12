import customtkinter, math
from typing import *
from commande import *


normal_grid = [
            [ COM[0], COM["sin"], COM["cos"], COM["+"] ],
            [ COM[1], COM[2]    , COM[3]    , COM["-"] ],
            [ COM[4], COM[5]    , COM[6]    , COM["/"] ],
            [ COM[7], COM[8]    , COM[9]    , COM["*"] ],
           ]

MARGIN = 5


def handleClick(elem : Command):
    newEntry :str= elem.Onclick(entry.get(),entry)

    entry.delete(0,len(entry.get()))
    entry.insert(0,newEntry)

    print("".join(newEntry))
    print(transformEntry(entry.get()))

def setGrid(app, grid: list[list[InputCommande]]):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            elem = normal_grid[row][col]
            button = elem.generateButton(app,handleClick)
            button.grid(row=row + 1, column=col, padx=MARGIN, pady=MARGIN)

def transformEntry(text):
    cutedString = []
    alphabet = "azertyuiopqsdrfghjklmwxcvbn"
    funcName = ""

    # spiting elem
    for char in text:
        
        if char in alphabet:
            funcName += char
        
        elif char == "(":
            cutedString.append(funcName+"(")
            funcName = ""
            
        else:
            if funcName != "":
                raise ValueError("missing '(' after function")
            
            cutedString.append(char)
    
    # transform token and check for invalid one
    output = []
    for token in cutedString:
        found = False
        for elem in COM.values():
            if elem.text == token:
                output.append(elem.code)
                found = True
                break
        
        if not found:
            raise ValueError(f'unknow token "{elem}" ')
    return output
        



def app():
    global entry
    app = customtkinter.CTk()
    app.geometry("400x150")
    entry = customtkinter.CTkEntry(app)
    entry.grid(row=0, column=0, padx=MARGIN, pady=MARGIN, columnspan=5,sticky=customtkinter.EW)

    setGrid(app,normal_grid)

    app.mainloop()



if __name__ == '__main__':
    app()