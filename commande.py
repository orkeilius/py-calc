import customtkinter

class Command :
    name :str = ""
    clickAction:str = ""
    button : customtkinter.CTkButton = None 

    def Onclick(self):
        pass

    def __init__(self,name:str,clickAction:str):
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

    def Onclick(self,calcEntry,entry:customtkinter.CTkEntry):
        print(self.text)
        calcEntry += self.text

        if "(" in self.text:
            calcEntry+= ")"
        
        return calcEntry

    


COM = {
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
    "^": InputCommande("^","^","**"),
    "sin": InputCommande("sin","sin(","math.sin("),
    "cos": InputCommande("cos"," cos(","math.cos("),
    "tan": InputCommande("tan"," tan(","math.tan("),

    ")": InputCommande(")"),
}

