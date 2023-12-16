import customtkinter

class Button(customtkinter.CTkButton) :
    name :str = ""
    clickAction:callable = None
    entryRef : customtkinter.CTkEntry 
    button : customtkinter.CTkButton

    def Onclick(self):
        self.clickAction(self,self.entryRef)

    def __init__(self,name:str,clickAction:callable,color="#3a7ebf"):
        self.name = name
        self.clickAction = clickAction
        self.color = color

    def initButton(self,frame,entryRef):
        super().__init__(frame, text=self.name, font=("",20), command=self.Onclick,fg_color=self.color)
        self.entryRef = entryRef
        self.frame = frame