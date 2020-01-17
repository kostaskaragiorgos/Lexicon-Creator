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
        self.master.geometry("250x200")
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
        
        self.defT = Text(self.master,height = 3,state="disabled")
        self.defT.pack()
        
        self.addb = Button(self.master,text = "ADD",state="disabled",command = self.addw)
        self.addb.pack()
        
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Create Lexicon",accelerator = 'Ctrl + O',command =self.create_l)
        self.file_menu.add_command(label = "Load Lexicon",accelerator = "Ctrl + L",command = self.load_l)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        self.master.bind('<Control-o>',lambda event:self.create_l())
        self.master.bind('<Control-l>',lambda event:self.load_l())
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event: self.aboutmenu())
        
    def addw(self):
        valam = 0
        valdes = 0
        try:
            if str(self.wordT.get(1.0,END)) or not(not createlex.strip() ):
                valam = 1
            else:
                msg.showerror("Value Error", "Enter a word")
                self.wordT.delete(0,END)
        except:
            msg.showerror("Value Error", "Enter a word")
            self.wordT.delete(1.0,END)
        if self.defT.count(1.0,END) == (1,):
            msg.showerror("Description Error", "Enter a Definition")
        else:
            valdes = 1
        if valam == 1 and valdes == 1:
            with open(str(self.createlex)+str('.csv'), 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([str(self.wordT.get(1.0,END)),self.defT.get(1.0,END)])
            msg.showinfo("Word info","Word: "+str(self.wordT.get(1.0,END))+"Definition: "+self.defT.get(1.0,END) )
        
    
    
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
            msg.showinfo("SUCCESS","THE FILE CREATED SUCCESSFULLY")

        else:
            msg.showerror("ERROR", "THIS FILE ALREADY EXISTS")

        
    def load_l(self):
        pass

    
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def helpmenu(self):
        pass
    
    def aboutmenu(self):
        pass

        

def main():
    root=Tk()
    LC = Lexicon_Creator(root)
    root.mainloop()
    
if __name__=='__main__':
    main()