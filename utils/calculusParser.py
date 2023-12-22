import customtkinter, math
from utils.buttonList import *
from ui.ButtonGrid import *
from typing import *
from ui import *

def calc(entryWidget,resultWidjet,historyWidget):
    """ handle calcul validation and handle error

    Args:
        entryWidget (_type_): entry widget for input
        resultWidjet (_type_): label widget for output
    """

    try:
        entry = "".join(transformEntry(entryWidget.get()))
        output = eval(entry)
        
        # use scientific notation if too long
        if len(str(output)) > 12 :
            output = '%E' % output
            output = output.replace("E+00", "...")
        
    except Exception as error:
        print(error)
        resultWidjet.configure(text=str(error),text_color="red")
        return
    
    historyWidget.addHistoryItem([entryWidget.get(),output])
        
    entryWidget.delete(0,len(entryWidget.get()))
    resultWidjet.configure(text=output,text_color="white")
        


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
        
        elif char in "(":      
            cutedString.append(funcName+char)
            funcName = ""
            
        else:
            if funcName != "":
                cutedString.append(funcName)
                funcName = ""
            
            cutedString.append(char)
    if funcName != "":
        raise ValueError("missing value after function")

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