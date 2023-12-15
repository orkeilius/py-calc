import customtkinter, math
from utils.buttonList import *
from utils.grid import *
from typing import *
from entity import *


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
        for elem in ButtonList.values():
            print(elem,type(elem))
            if type(elem) == Button.Button:
                continue
            
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

    submitWidjet.grid(row=1, column=3, padx=5, pady=5,columnspan=4,sticky=customtkinter.NSEW)
    entryWidget.grid(row=1, column=0, padx=5, pady=5, columnspan=3,sticky=customtkinter.NSEW)
    resultWidjet.grid(row=0, column=0, padx=5, pady=5, columnspan=3, sticky=customtkinter.NSEW)
    
    setGrid(app,entryWidget,"basic")
    entryWidget.focus()

    app.mainloop()



if __name__ == '__main__':
    app()