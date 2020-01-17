from tkinter import *
from tkinter import messagebox as msg
from tkinter import simpledialog
import os 
import csv

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
        pass
    
    
    def create_l(self):
        createlex = simpledialog.askstring("NEW LEXICON","Enter the name of the new lexicon", parent = self.master)
        while createlex == None or (not createlex.strip() ): 
            createlex = simpledialog.askstring("NEW LEXICON","Enter the name of the new lexicon", parent = self.master)
        if os.path.exists(createlex+str(".csv")) == False:
            with open(str(createlex)+str(".csv"), 'a+') as d:
                thewriter = csv.writer(d)
                thewriter.writerow(['Word','Definition'])
        
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