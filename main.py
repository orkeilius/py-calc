import customtkinter
from utils.calculusParser import *


def app():
    global entryWidget,resultWidjet
    app = customtkinter.CTk()
    app.geometry("500x500")

    app.grid_rowconfigure(0, weight=1)
    app.grid_rowconfigure(1, weight=3)


    submitWidjet = customtkinter.CTkButton(app,text="=",command=lambda : calc(entryWidget,resultWidjet),fg_color="green")
    entryWidget = customtkinter.CTkEntry(app)
    resultWidjet = customtkinter.CTkLabel(app,text="result",anchor="sw")

    submitWidjet.grid(row=1, column=3, padx=5, pady=5,columnspan=4,sticky=customtkinter.NSEW)
    entryWidget.grid(row=1, column=0, padx=5, pady=5, columnspan=3,sticky=customtkinter.NSEW)
    resultWidjet.grid(row=0, column=0, padx=5, pady=5, columnspan=3, sticky=customtkinter.NSEW)
    
    setGrid(app,entryWidget,"basic")
    entryWidget.focus()

    app.mainloop()



if __name__ == '__main__':
    app()