from tkinter import *
from tkinter import messagebox as msg
from tkinter import simpledialog
import os 
import csv
import pandas as pd


class Lexicon_Creator():
    def __init__(self,master):
        self.master = master
        self.master.title("Lexicon Creator")
        self.master.geometry("250x220")
        self.master.resizable(False,False)
        
        if os.path.exists("Lexicons") == False:
            os.mkdir("Lexicons")
            os.chdir("Lexicons")
        else:
            os.chdir("Lexicons")
        
        self.wordlabel = Label(self.master,text= "Word",)
        self.wordlabel.pack()
        
        self.wordT = Text(self.master,height = 1,state="disabled")
        self.wordT.pack()
        
        self.deflablel = Label(self.master ,text = "Definition")
        self.deflablel.pack()
        
        self.defT = Text(self.master,height = 4,state="disabled")
        self.defT.pack()

        self.cleardb  = Button(self.master,text = "Clear Definition", state  ="disabled",command = self.cleardf)
        self.cleardb.pack()
        
        self.clearwb = Button(self.master,text ="Clear Word" ,state  = "disabled",command = self.clearwf)
        self.clearwb.pack()

        self.addb = Button(self.master,text = "Add",state="disabled",command = self.addw)
        self.addb.pack()
        

        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Create Lexicon",command =self.create_l)
        self.file_menu.add_command(label = "Load Lexicon",command = self.load_l)
        self.file_menu.add_command(label = "Close File",command = self.cfile,state = "disabled")
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event: self.aboutmenu())

    
    def cleardf(self):
        self.defT.delete(1.0,END)

    
    def clearwf(self):
        self.wordT.delete(1.0,END)

    
    def cfile(self):
        self.createlex = ""
        self.loadlex = ""
        self.wordT.config(state="disable")
        self.defT.config(state="disable")
        self.addb.config(state="disable")
        self.clearwb.config(state = "disable")
        self.cleardb.config(state = "disable")
        self.file_menu.entryconfig("Create Lexicon", state="normal")
        self.file_menu.entryconfig("Load Lexicon" , state = "normal")
        self.file_menu.entryconfig("Close File",state = "disable")
        msg.showinfo("SUCCESS", "FILE CLOASED")

 
    def addw(self):
        valam = 0
        valdes = 0
        try:
            if not str(self.wordT.get(1.0,END)==(1,)) or not(not createlex.strip() ):
                valam = 1
            else:
                msg.showerror("Value Error", "Enter a word")
                self.wordT.delete(1.0,END)
                self.defT.delete(1.0,END)
        except:
            msg.showerror("Value Error", "Enter a word")
            self.wordT.delete(1.0,END)
        if self.defT.count(1.0,END) == (1,):
            msg.showerror("Description Error", "Enter a Definition")
            self.defT.delete(1.0,END)
            self.wordT.delete(1.0,END)
        else:
            valdes = 1
        if valam == 1 and valdes == 1:
            with open(str(self.createlex)+str('.csv'), 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([str(self.wordT.get(1.0,END)),self.defT.get(1.0,END)])
            msg.showinfo("Word info","Word: "+str(self.wordT.get(1.0,END))+"Definition: "+self.defT.get(1.0,END) )
            self.wordT.delete(1.0,END)
            self.defT.delete(1.0,END)
        
    
    
    def create_l(self):
        self.createlex = simpledialog.askstring("NEW LEXICON","Enter the name of the new lexicon", parent = self.master)
        while self.createlex == None or (not self.createlex.strip() ): 
            self.createlex = simpledialog.askstring("NEW LEXICON","Enter the name of the new lexicon", parent = self.master)
        if os.path.exists(self.createlex+str(".csv")) == False:
            with open(str(self.createlex)+str(".csv"), 'a+') as d:
                thewriter = csv.writer(d)
                thewriter.writerow(['Word','Definition'])
            self.wordT.config(state="normal")
            self.defT.config(state="normal")
            self.addb.config(state="normal")
            self.clearwb.config(state = "normal")
            self.cleardb.config(state = "normal")
            msg.showinfo("SUCCESS","THE FILE CREATED SUCCESSFULLY")
            self.file_menu.entryconfig("Create Lexicon", state="disabled")
            self.file_menu.entryconfig("Load Lexicon" , state = "disabled")
            self.file_menu.entryconfig("Close File",state = "normal")

        else:
            msg.showerror("ERROR", "THIS FILE ALREADY EXISTS")

        
    def load_l(self):
        f=0
        self.loadlex = simpledialog.askstring("LOAD LEXICON" , "Enter the name  of the lexicon you want to load (Case sensitive)")
        while self.loadlex == None or (not self.loadlex.strip() ): 
            self.loadlex = simpledialog.askstring("LOAD LEXICON","Enter the name of the lexicon you want to load (Case sensitive)", parent = self.master)
        for i in os.listdir():
            if str(self.loadlex+".csv") == i:
                f +=1
        if f > 0:
            self.wordT.config(state="normal")
            self.defT.config(state="normal")
            self.addb.config(state="normal")
            self.clearwb.config(state = "normal")
            self.cleardb.config(state = "normal")
            self.createlex = self.loadlex 
            msg.showinfo("SUCCESS","THE FILE LOADED SUCCESSFULLY")
            self.file_menu.entryconfig("Close File",state = "normal")
            self.file_menu.entryconfig("Create Lexicon", state="disabled")
            self.file_menu.entryconfig("Load Lexicon" , state = "disabled")
        else:
            msg.showerror("ERROR", "THERE IS NO FILE NAMED "+ str(self.loadlex+".csv"))
            
        
    
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def helpmenu(self):
        msg.showinfo("Help","Create or load a lexicon from the file menu. Add the word and its definition to the lexicon")
    
    def aboutmenu(self):
        msg.showinfo("About", "Version 1.0")

        

def main():
    root=Tk()
    LC = Lexicon_Creator(root)
    root.mainloop()
    
if __name__=='__main__':
    main()