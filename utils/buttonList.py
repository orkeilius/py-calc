from ui.TextButton import *
from ui.Button import *
import customtkinter

"""file listing button and storing button's custom functions
 """

def delAction(self: Button, entryWidget:customtkinter.CTkEntry):
    pos = entryWidget.index(customtkinter.INSERT) 
    entry = entryWidget.get()
    
    entryWidget.delete(0,len(entryWidget.get()))
    entryWidget.insert(0,entry[:pos -1] + entry[pos:] ) 
    entryWidget.icursor(pos -1) 
    
def clearAction(self: Button, entryWidget:customtkinter.CTkEntry):   
    entryWidget.delete(0,len(entryWidget.get()))

def secondAction(self: Button, entryWidget:customtkinter.CTkEntry):   
    self.frame.switchSecond()


# list of usable button
ButtonList = {    
    "del": Button("del",delAction,color="red"),
    "clr": Button("clear",clearAction,color="grey"),
    "2de": Button("2de",secondAction,color="#ffb703"),
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
    "xʸ": TextButton("xʸ","^","**"),
    "x²": TextButton("x²","^2"),
    "x³": TextButton("x³","^3"),
    "10ʸ": TextButton("10ʸ","10^"),
    ",": TextButton(",","."),
    "π": TextButton("π","π","math.pi "),
    "e": TextButton("ℯ","ℯ","math.e "),
    "sin": TextButton("sin","sin(","math.sin("),
    "cos": TextButton("cos","cos(","math.cos("),
    "tan": TextButton("tan","tan(","math.tan("),
    "asin": TextButton("asin","asin(","math.asin("),
    "acos": TextButton("acos","acos(","math.acos("),
    "atan": TextButton("atan","atan(","math.atan("),
    "log": TextButton("log","log(","math.log10("),
    "ln": TextButton("ln","ln(","math.log("),
    "√": TextButton("√","√(","math.sqrt("),
    "|x|": TextButton("|x|","abs("),
    "mod": TextButton("mod","mod","%"), 
    "!": TextButton("!","!(","math.factorial("),
    "(": TextButton("("),
    ")": TextButton(")"),
    "e+":TextButton("E")
}
