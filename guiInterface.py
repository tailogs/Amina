import tkinter as tk
import tkinter.font as font
#from textInterface import scanner

def Gui():
    root = tk.Tk()    
    root.title("Amina System")
    #root.minsize(width=500, height=400)
    #root.geometry("400x150")
    root.state('zoomed')

    commandFrame = tk.Frame(
        root,
        padx = 10,
        pady = 10
    )
    commandFrame.pack(expand=True)

    AminaLb = tk.Label(commandFrame,
                        text="Amina System",
                        font=font.Font(family="Arial", size=16))

    command = tk.Entry(commandFrame,
                    width=60,
                    font=font.Font(family="Arial", size=26),
                    bg="grey",
                    fg="white")

    commandBtn = tk.Button(commandFrame,
                    width=20,
                    text="To perform",
                    font=font.Font(family="Arial", size=16),
                    bg="blue",
                    fg="white")

    commandBtn.bind("<Return>", scanner(command.get().lower()))
    
    AminaLb.pack(expand=1)
    command.pack(expand=1)
    commandBtn.pack(side="right")

    root.mainloop()