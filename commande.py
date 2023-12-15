import customtkinter

class Command :
    name :str = ""
    clickAction:callable = None
    button : customtkinter.CTkButton = None 

    def Onclick(self,entryWidget:customtkinter.CTkEntry):
        self.clickAction(entryWidget)
        

    def __init__(self,name:str,clickAction:callable):
        self.name = name
        self.clickAction = clickAction
    
    def generateButton(self, app,function:callable):
        button = customtkinter.CTkButton(app, text=self.name, command=lambda: function(self))
        return button


class InputCommande(Command) :
    text :str = ""
    code :str = ""

    def __init__(self,name:str, text:str=None, code:str=None):
        
        if text == None:
            self.text = name
        else:
            self.text = text

        if code == None:
            self.code = self.text
        else:
            self.code = code

        Command.__init__(self,name,lambda list: self.textApply(text,list))

    def Onclick(self,entryWidget:customtkinter.CTkEntry):
        pos = entryWidget.index(customtkinter.INSERT) 
        entry = entryWidget.get()
        
        if "(" in self.text:
            entry = entry[:pos] + self.text + ")" + entry[pos:]
        else:
            entry = entry[:pos] + self.text + entry[pos:]      
        
        entryWidget.delete(0,len(entryWidget.get()))
        entryWidget.insert(0,entry)
    
        entryWidget.icursor(pos + len(self.text)) 


def delAction(entryWidget:customtkinter.CTkEntry):
    pos = entryWidget.index(customtkinter.INSERT) 
    entry = entryWidget.get()
    
    entryWidget.delete(0,len(entryWidget.get()))
    entryWidget.insert(0,entry[:pos -1] + entry[pos:] ) 
    entryWidget.icursor(pos -1) 
    
def clearAction(entryWidget:customtkinter.CTkEntry):   
    entryWidget.delete(0,len(entryWidget.get()))



CommandeList = {
    "del": Command("del",delAction),
    "clr": Command("clr", clearAction),
    1: InputCommande("1"),
    2: InputCommande("2"),
    3: InputCommande("3"),
    4: InputCommande("4"),
    5: InputCommande("5"),
    6: InputCommande("6"),
    7: InputCommande("7"),
    8: InputCommande("8"),
    9: InputCommande("9"),
    0: InputCommande("0"),
    "+": InputCommande("+"),
    "-": InputCommande("-"),
    "/": InputCommande("/"),
    "*": InputCommande("*"),
    "%": InputCommande("%"),
    "x²": InputCommande("^","^","**"),
    ",": InputCommande(",",",","."),
    "π": InputCommande("π","π","math.pi "),
    "e": InputCommande("e","e","math.e "),
    "sin": InputCommande("sin","sin(","math.sin("),
    "cos": InputCommande("cos"," cos(","math.cos("),
    "tan": InputCommande("tan"," tan(","math.tan("),
    "√": InputCommande("√","√(","math.sqrt("),

    ")": InputCommande(")"),
}


