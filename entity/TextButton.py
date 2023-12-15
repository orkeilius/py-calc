from entity.Button import Button
import customtkinter

class TextButton(Button) :
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

        Button.__init__(self,name,lambda list: self.textApply(text,list))

    def Onclick(self):
        pos = self.entryRef.index(customtkinter.INSERT) 
        entry = self.entryRef.get()
        
        if "(" in self.text:
            entry = entry[:pos] + self.text + ")" + entry[pos:]
        else:
            entry = entry[:pos] + self.text + entry[pos:]      
        
        self.entryRef.delete(0,len(self.entryRef.get()))
        self.entryRef.insert(0,entry)
    
        self.entryRef.icursor(pos + len(self.text)) 
