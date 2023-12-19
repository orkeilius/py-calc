from utils.buttonList import ButtonList
from ui.TextButton import TextButton
from ui.Button import *
import customtkinter


class HistoryPanel(customtkinter.CTkScrollableFrame):
    """ frame who handle history panel
    """
    
    history : list[str] = []
    historyButton :list[TextButton]= []
    entryRef : customtkinter.CTkEntry
        
    def __init__(self, parent, entryRef : customtkinter.CTkEntry):
        super().__init__(parent)
        self.entryRef = entryRef
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        self.title = customtkinter.CTkLabel(self,text="history",font=("",20))
        self.title.grid(row=0,columnspan=2,sticky=customtkinter.NSEW)
        
        self.draw()
        

    def draw(self):
        """ draw the history panel
        """
        
        # create new elem
        for i in range(len(self.historyButton),len(self.history)):
            
            if i % 2 == 0:
                elem = TextButton(str(self.history[i]),color="grey")
            else:
                elem = TextButton(str(self.history[i]))
            
            elem.initButton(self,self.entryRef)
            self.historyButton.insert(0,elem)
        
        # place button
        
        for i in range(len(self.historyButton)):
            self.historyButton[i].grid(row=i+2,column=i%2,sticky=customtkinter.NSEW) 
        
        
            

    def addHistoryItem(self,items : list[str]):
        """handeler to add elem in history

        Args:
            items (list[str]): item to be added
        """
        self.history.extend(reversed(items))  
        self.draw()      