import tkinter as tk
from tkinter import ttk
from scrollMaker import *



class TableMaker(tk.Tk):
    def __init__(self, rows, cols, content, title):
        super().__init__()
        self.title(title)
        
        self.geometry("560x800")
        self.config(background='blue')
        ttk.Label(self, text="List of all patients" ,font=('Arial' ,40, 'bold'),foreground='yellow' , background='blue').pack()
        
        self.rows=rows
        self.cols=cols
        self.content=content
    
        self.fm=ttk.Frame(self , width=600 , height=800 )
        self.obj=scrollMaker(self.fm, 'blue', tk.RIGHT)
        self.obj.returnFrame()
        self.obj.bindScrollAction()

        
        
        for i in range(self.rows):
            for j in range(self.cols):
                self.e=ttk.Entry(self.obj.canvasFrame, width=15 , foreground="orange",  background='blue',font=('Arial',14,'bold'))
                self.e.grid(row=i , column=j ,sticky='nwes')
                self.e.insert(tk.END, self.content[i][j])
                
        
        self.fm.pack()
        self.mainloop()
       
        
    
       
         
               
                



        



