from entity.TextButton import *
from entity.Button import *
import customtkinter


def delAction(entryWidget:customtkinter.CTkEntry):
    pos = entryWidget.index(customtkinter.INSERT) 
    entry = entryWidget.get()
    
    entryWidget.delete(0,len(entryWidget.get()))
    entryWidget.insert(0,entry[:pos -1] + entry[pos:] ) 
    entryWidget.icursor(pos -1) 
    
def clearAction(entryWidget:customtkinter.CTkEntry):   
    entryWidget.delete(0,len(entryWidget.get()))

ButtonList = {
    "del": Button("del",delAction),
    "clr": Button("clr", clearAction),
    1: TextButton("1"),
    2: TextButton("2"),
    3: TextButton("3"),
    4: TextButton("4"),
    5: TextButton("5"),
    6: TextButton("6"),
    7: TextButton("7"),
    8: TextButton("8"),
    9: TextButton("9"),
    0: TextButton("0"),
    "+": TextButton("+"),
    "-": TextButton("-"),
    "/": TextButton("/"),
    "*": TextButton("*"),
    "%": TextButton("%","%","/100 "),
    "x²": TextButton("^","^","**"),
    ",": TextButton(",",",","."),
    "π": TextButton("π","π","math.pi "),
    "e": TextButton("e","e","math.e "),
    "sin": TextButton("sin","sin(","math.sin("),
    "cos": TextButton("cos"," cos(","math.cos("),
    "tan": TextButton("tan"," tan(","math.tan("),
    "√": TextButton("√","√(","math.sqrt("),
    "(": TextButton("("),
    ")": TextButton(")"),
}
