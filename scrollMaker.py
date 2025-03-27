import tkinter as tk
from tkinter import ttk

class scrollMaker :
    def __init__(self , frame, canvasColor, scrollSide=tk.RIGHT) :
        self.frame=frame
        self.canvasColor=canvasColor
        self.scrollSid=scrollSide
        
        self.canvas=tk.Canvas(self.frame , width=560 ,height=600)
        self.canvas.bind_all("<MouseWheel>" , self._on_mousewheel)
        
        self.canvasFrame=tk.Frame(self.canvas , width=560 , height=600)
        self.yscroll=ttk.Scrollbar(self.frame, orient="vertical" ,  command=self.canvas.yview )
        self.xscroll=ttk.Scrollbar(self.frame, orient="horizontal" ,  command=self.canvas.xview )
        
        
        self.style=ttk.Style(self.xscroll)
        self.style.theme_use('default')
        self.style.configure("Horizontal.TScrollbar",background="white", arrowcolor="white")
        
        self.style=ttk.Style(self.yscroll)
        self.style.theme_use('default')
        self.style.configure("Vertical.TScrollbar",background="white" , arrowcolor="white")
        
        
        self.yscroll.pack(side=self.scrollSid , fill="y")
        self.xscroll.pack(side="bottom" , fill="x")
        self.canvas.pack(side=self.scrollSid , fill="both", expand=True)
        self.canvas.config(bg=self.canvasColor )
        self.canvas.configure(yscrollcommand=self.yscroll.set , xscrollcommand=self.xscroll.set)
        self.canvas.create_window((0,0), window=self.canvasFrame, anchor="nw")
        
    def _on_mousewheel(self, event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
            
    def removeScroll(self):
        self.yscroll.pack_forget()
    def bindScrollAction (self):
        self.canvas.bind("<Configure>", lambda e : self.canvas.configure(scrollregion=self.canvas.bbox("all")))
    def returnFrame(self):
        self.canvasFrame    
        