import customtkinter

class Button :
    name :str = ""
    clickAction:callable = None
    entryRef : customtkinter.CTkEntry 
    button : customtkinter.CTkButton

    def Onclick(self):
        self.clickAction(self.entryRef)
        

    def __init__(self,name:str,clickAction:callable):
        self.name = name
        self.clickAction = clickAction
    
    def generateButton(self, app,entryRef:customtkinter.CTkEntry):
        self.entryRef = entryRef
        Button = customtkinter.CTkButton(app, text=self.name, command=self.Onclick)
        return Button
