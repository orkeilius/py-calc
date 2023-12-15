import customtkinter, math
from typing import *
from commande import *


normal_grid = [
            [ COM[0], COM[0]    , COM[0]    , COM["sqrt"] ],
            [ COM[0], COM["sin"], COM["cos"], COM["+"] ],
            [ COM[1], COM[2]    , COM[3]    , COM["-"] ],
            [ COM[4], COM[5]    , COM[6]    , COM["/"] ],
            [ COM[7], COM[8]    , COM[9]    , COM["*"] ],
           ]

MARGIN = 5
DEBUG = True

def handleClick(elem : Command):
    newEntry :str= elem.Onclick(entryWidget)

def calc():

    try:
        entry = "".join(transformEntry(entryWidget.get()))
        print(entry)
        output = eval(entry)
        print(output)
        
        entryWidget.delete(0,len(entryWidget.get()))
        resultWidjet.configure(text=output,text_color="white")
    except Exception as error:
        print(error)
        resultWidjet.configure(text=str(error),text_color="red")

def setGrid(app, grid: list[list[InputCommande]]):

    # set grid config
    for col in range(len(grid[0])):
        app.grid_columnconfigure(col, weight=4)
    for row in range(2,len(grid) + 2):
        app.grid_rowconfigure(row, weight=4)

    # set button
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            elem = normal_grid[row][col]
            button = elem.generateButton(app,handleClick)
            button.grid(row=row + 2, column=col, padx=MARGIN, pady=MARGIN, sticky=customtkinter.NSEW)

def transformEntry(text):
    cutedString = []
    funcToken = "azertyuiopqsdrfghjklmwxcvbn√"
    funcName = ""

    # spiting elem
    for char in text:
        
        if char in funcToken:
            funcName += char
        
        elif char == "(":
            cutedString.append(funcName+"(")
            funcName = ""
            
        else:
            if funcName != "":
                raise ValueError("missing '(' after function")
            
            cutedString.append(char)
    if funcName != "":
        raise ValueError("missing '(' after function")

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
    global entryWidget,resultWidjet
    app = customtkinter.CTk()
    app.geometry("500x500")

    app.grid_rowconfigure(0, weight=1)
    app.grid_rowconfigure(1, weight=3)


    submitWidjet = customtkinter.CTkButton(app,text="=",command=calc,fg_color="green")
    entryWidget = customtkinter.CTkEntry(app)
    resultWidjet = customtkinter.CTkLabel(app,text="result",anchor="sw")

    submitWidjet.grid(row=1, column=3, padx=MARGIN, pady=MARGIN,columnspan=4,sticky=customtkinter.NSEW)
    entryWidget.grid(row=1, column=0, padx=MARGIN, pady=MARGIN, columnspan=3,sticky=customtkinter.NSEW)
    resultWidjet.grid(row=0, column=0, padx=MARGIN, pady=MARGIN, columnspan=3, sticky=customtkinter.NSEW)
    
    setGrid(app,normal_grid)
    entryWidget.focus()

    app.mainloop()



if __name__ == '__main__':
    app()