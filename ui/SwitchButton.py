import customtkinter

modes = ["basic","scientific"]

class SwitchButton(customtkinter.CTkButton):
    """button to switch between basic/scientific
    """
    
    mode = 0
    
    def __init__(self,app):
        super().__init__(app, text=modes[self.mode], command=self.switch,fg_color="gray28",hover_color="gray52")    
        self.app = app
    
    def switch(self):
        self.mode = (self.mode + 1) % len(modes)
        self.configure(text=modes[self.mode])
        self.app.updateGrid(modes[self.mode])
        