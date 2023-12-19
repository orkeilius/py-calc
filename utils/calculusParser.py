import customtkinter, math
from utils.buttonList import *
from ui.ButtonGrid import *
from typing import *
from ui import *

def calc(entryWidget,resultWidjet):
    """ handle calcul validation and handle error

    Args:
        entryWidget (_type_): entry widget for input
        resultWidjet (_type_): label widget for output
    """

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
    """ transform and sanitize input for eval()

    Args:
        text (_type_): input

    Raises:
        ValueError: invalid input to get handled by the calc()

    Returns:
        _type_: output
    """
    cutedString = []
    funcToken = "azertyuiopqsdrfghjklmwxcvbn√!"
    funcName = ""

    # spiting elem in token
    for char in text:
        
        if char in funcToken:
            funcName += char
        elif char == " " and funcName == "":
            continue
        
        elif char in "( ":      
            cutedString.append(funcName+char)
            funcName = ""
            
        else:
            if funcName != "":
                raise ValueError("missing '(' after function")
            
            cutedString.append(char)
    if funcName != "":
        raise ValueError("missing '(' after function")

    # transform token and check for invalid one
    output = []
    print(cutedString)
    for token in cutedString:
        found = False
        for elem in ButtonList.values():
            if type(elem) == Button.Button:
                continue
            
            if elem.text == token:
                output.append(elem.code)
                found = True
                break
        
        if not found:
            raise ValueError(f'unknow token "{token}" ')
    
    return output