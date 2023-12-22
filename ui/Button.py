import customtkinter

class Button(customtkinter.CTkButton) :
    """class to handle command and text Button
    
    extend by textButton
    """
    
    name :str = ""
    clickAction:callable = None
    entryRef : customtkinter.CTkEntry 
    button : customtkinter.CTkButton
    color: str

    def Onclick(self):
        self.clickAction(self,self.entryRef)

    def __init__(self,name:str,clickAction:callable,color="#3a7ebf"):
        """

        Args:
            name (str): text to be show
            clickAction (callable): function to be call
            color (str, optional): button color Defaults to "#3a7ebf".
        """
        self.name = name
        self.clickAction = clickAction
        self.color = color

    def initButton(self,frame,entryRef):
        """generate button before being isntancied

        that not in the __init__ so the class can be stored in buttonlist without frame set 
        
        Args:
            frame (_type_): parent widget
            entryRef (_type_): reference to the entry
        """
        super().__init__(frame, text=self.name, font=("",20), command=self.Onclick,fg_color=self.color)
        self.entryRef = entryRef
        self.frame = frame