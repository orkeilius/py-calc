import customtkinter

class Button(customtkinter.CTkButton) :
    name :str = ""
    clickAction:callable = None
    entryRef : customtkinter.CTkEntry 
    button : customtkinter.CTkButton

    def Onclick(self):
        self.clickAction(self,self.entryRef)

    def __init__(self,name:str,clickAction:callable):
        self.name = name
        self.clickAction = clickAction

    def initButton(self,frame,entryRef):
        super().__init__(frame, text=self.name, font=("",20), command=self.Onclick)
        self.entryRef = entryRef
        self.frame = frame