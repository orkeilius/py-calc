import customtkinter
from utils.calculusParser import *
from ui.ButtonGrid import ButtonGrid
from ui.SwitchButton import SwitchButton
from ui.HistoryPanel import HistoryPanel

class app(customtkinter.CTk):
    """Main class for the app
    
    """
    
    def __init__(self):
        super().__init__()
        self.title("py-calc")
        self.geometry("700x500")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=3)
        self.grid_rowconfigure(2, weight=20)
        
        self.grid_columnconfigure(0, weight=1)

        self.resultWidget = customtkinter.CTkLabel(self,text="result",anchor="sw",font=("",20))
        self.resultWidget.grid(row=0, column=0, padx=5, pady=5, sticky=customtkinter.NSEW)
        
        self.switchWidget = SwitchButton(self)
        self.switchWidget.grid(row=0, column=5, padx=5, pady=5, sticky=customtkinter.NSEW)

        self.entryWidget = customtkinter.CTkEntry(self)
        self.entryWidget.grid(row=1, column=0, padx=5, pady=5, columnspan=3,sticky=customtkinter.NSEW)
        self.entryWidget.focus()

        self.historyWidget = HistoryPanel(self,self.entryWidget)
        self.historyWidget.grid(row=0, column=9, rowspan=4, sticky=customtkinter.NSEW)
        
        self.submitWidget = customtkinter.CTkButton(self,text="=",command=lambda : calc(self.entryWidget,self.resultWidget,self.historyWidget),fg_color="green")
        self.submitWidget.grid(row=1, column=3, padx=5, pady=5,columnspan=5,sticky=customtkinter.NSEW)

        self.gridWidget = ButtonGrid(self,self.entryWidget,"basic")
        self.gridWidget.grid(row=2, column=0, padx=0, pady=0, columnspan=7, sticky=customtkinter.NSEW)

        self.bind('<Return>', lambda x: calc(self.entryWidget,self.resultWidget,self.historyWidget))
        self.mainloop()

    def updateGrid(self,mode:str):
        """ handeler for the switch button

        Args:
            mode (str): mode to send to grid widget
        """
        self.gridWidget = ButtonGrid(self,self.entryWidget,mode)
        self.gridWidget.grid(row=2, column=0, padx=0, pady=0, columnspan=7, sticky=customtkinter.NSEW)

if __name__ == '__main__':
    app()