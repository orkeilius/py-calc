from ui.Button import Button
import customtkinter

class TextButton(Button) :
    """ extended from Button to handle button who write to the entry

    """
    
    text :str = ""
    code :str = ""

    def __init__(self,name:str, text:str=None, code:str=None,color="#3a7ebf"):
        """

        Args:
            name (str): text to be show
            
            text (str, optional): text write in the entry. 
                Default: copied from name.
                
            code (str, optional): text that will replace the text to be evalued. 
                Default: copied from text
                
            color (str, optional): button color. Defaults to "#3a7ebf".
        """
        
        if text == None:
            self.text = name
        else:
            self.text = text

        if code == None:
            self.code = self.text
        else:
            self.code = code

        Button.__init__(self,name,lambda list: self.textApply(text,list),color)

    def Onclick(self):
        """ function call onClick
        add the text at the cursor position 
        
        and add a ")" after if that a function
        
        """
        pos = self.entryRef.index(customtkinter.INSERT) 
        entry = self.entryRef.get()
        
        if "(" in self.text:
            entry = entry[:pos] + self.text + ")" + entry[pos:]
        else:
            entry = entry[:pos] + self.text + entry[pos:]      
        
        self.entryRef.delete(0,len(self.entryRef.get()))
        self.entryRef.insert(0,entry)
    
        self.entryRef.icursor(pos + len(self.text)) 
