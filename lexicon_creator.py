"""
You can create your own lexicon and save it to a .csv file
""" 
from tkinter import Label, Text, Button, Menu, Tk, END
from tkinter import messagebox as msg
from tkinter import simpledialog
import os 
import csv
import pandas as pd
def helpmenu():
    """ help menu """
    msg.showinfo("Help", "Create or load a lexicon from the file menu. Add the word and its definition to the lexicon")
def aboutmenu():
    """ about menu """
    msg.showinfo("About", "Version 1.0")
class LexiconCreator():
    """
    Lexicon Creator Class
    """
    def __init__(self, master):
        self.master = master
        self.master.title("Lexicon Creator")
        self.master.geometry("250x220")
        self.master.resizable(False, False)
        if not os.path.exists("Lexicons"):
            os.mkdir("Lexicons")
            os.chdir("Lexicons")
        else:
            os.chdir("Lexicons")
        self.createlex = ""
        self.wordlabel = Label(self.master, text="Word",)
        self.wordlabel.pack()
        self.wordT = Text(self.master, height=1, state="disabled")
        self.wordT.pack()
        self.deflablel = Label(self.master, text="Definition")
        self.deflablel.pack()
        self.defT = Text(self.master, height=4, state="disabled")
        self.defT.pack()
        self.cleardb = Button(self.master, text="Clear Definition", state="disabled", command=self.cleardf)
        self.cleardb.pack()
        self.clearwb = Button(self.master, text="Clear Word", state="disabled", command=self.clearwf)
        self.clearwb.pack()
        self.addb = Button(self.master, text="Add", state="disabled", command=self.addw)
        self.addb.pack()
        #menu
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Create Lexicon", accelerator='Ctrl+N', command=self.create_l)
        self.file_menu.add_command(label="Load Lexicon", accelerator='Ctrl+L', command=self.load_l)
        self.file_menu.add_command(label="Add Word", accelerator='Ctrl+O', command=self.addw)
        self.file_menu.add_command(label="Close File", accelerator='Ctrl+F4', command=self.cfile, state="disabled")
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.edimenu = Menu(self.menu, tearoff=0)
        self.edimenu.add_command(label="Reset", accelerator='Ctrl+Z', command=self.reset)
        self.edimenu.add_command(label="Clear Word", accelerator='Alt+Z', command=self.clearwf)
        self.edimenu.add_command(label="Clear Definition", accelerator='Alt+D', command=self.cleardf)
        self.edimenu.add_command(label="Delete Word", accelerator='Ctrl+D', command=self.deleteword)
        self.menu.add_cascade(label="Edit", menu=self.edimenu)
        self.showmenu = Menu(self.menu, tearoff=0)
        self.showmenu.add_command(label="Show Lexicon", accelerator='Ctrl+T', command=self.showlexicon)
        self.menu.add_cascade(label="Show", menu=self.showmenu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Control-z>', lambda event: self.reset())
        self.master.bind('<Control-o>', lambda event: self.addw())
        self.master.bind('<Alt-d>', lambda event: self.cleardf())
        self.master.bind('<Alt-z>', lambda event: self.clearwf())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        self.master.bind('<Control-t>', lambda event: self.showlexicon())
        self.master.bind('<Control-n>', lambda event: self.create_l())
        self.master.bind('<Control-l>', lambda event: self.load_l())
        self.master.bind('<Control-F4>', lambda event: self.cfile())
        self.master.bind('<Control-d>', lambda event: self.deleteword())
    def deleteword(self):
        """ deletes a word from the loaded or created lexicon"""
        if self.createlex == "":
            msg.showerror("Error", "No Lexicon")
        elif pd.read_csv(str(self.createlex)+str('.csv')).empty:
            msg.showerror('Error', "Empty Lexicon")
        #else:
            #self.word_delete = simpledialog.askstring("Word To Delete", "Enter the word to delete (Case sensitive)", parent=self.master) TODO
    def reset(self):
        """ clears both word and definition field """
        self.wordT.delete(1.0, END)
        self.defT.delete(1.0, END)
    def cleardf(self):
        """ clears the definition  text field"""
        self.defT.delete(1.0, END)
    def clearwf(self):
        """ clears the word text field"""
        self.wordT.delete(1.0, END)
    def showlexicon(self):
        """ shows the whole lexicon """
        if self.createlex == "":
            msg.showerror("Error", "No Lexicon")
        elif pd.read_csv(str(self.createlex)+str('.csv')).empty:
            msg.showerror('Error', "Empty Lexicon")
        else:
            df = pd.read_csv(str(self.createlex)+str('.csv'))
            df.drop_duplicates(keep="first", inplace=True)
            df.replace(r'\r\n', ' ', regex=True, inplace=True)
            msg.showinfo("Lexicon Words", str(df))
    def cfile(self):
        """ closes the lexicon """
        if self.createlex == "":
            msg.showerror("Error", "No lexicon to close")
        else:
            self.createlex = ""
            self.loadlex = ""
            self.wordT.config(state="disable")
            self.defT.config(state="disable")
            self.addb.config(state="disable")
            self.clearwb.config(state="disable")
            self.cleardb.config(state="disable")
            self.file_menu.entryconfig("Create Lexicon", state="normal")
            self.file_menu.entryconfig("Load Lexicon", state="normal")
            self.file_menu.entryconfig("Close File", state="disable")
            msg.showinfo("SUCCESS", "FILE CLOASED")
    def addw(self):
        """ adds word to the lexicon"""
        if self.wordT.count(1.0, END) == (1, ) or  self.defT.count(1.0, END) == (1, ):
            msg.showerror("Value Error Description Error", "Enter a word \n Enter a Definition")
            self.wordT.delete(1.0, END)
            self.defT.delete(1.0, END)
        else:
            with open(str(self.createlex)+str('.csv'), 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([str(self.wordT.get(1.0, END)), self.defT.get(1.0, END)])
            msg.showinfo("Word info", "Word: "+str(self.wordT.get(1.0, END))+"Definition: "+self.defT.get(1.0, END))
            self.wordT.delete(1.0, END)
            self.defT.delete(1.0, END)
    def button_menu_state_change(self):
        """ change buttons and menus after lexicon creation or after load"""
        self.wordT.config(state="normal")
        self.defT.config(state="normal")
        self.addb.config(state="normal")
        self.clearwb.config(state="normal")
        self.cleardb.config(state="normal")
        self.file_menu.entryconfig("Close File", state="normal")
        self.file_menu.entryconfig("Create Lexicon", state="disabled")
        self.file_menu.entryconfig("Load Lexicon", state="disabled")
    def createlexiconuserinput(self):
        """ create lexicon menu user input"""
        self.createlex = simpledialog.askstring("NEW LEXICON", "Enter the name of the new lexicon", parent=self.master)
        while self.createlex is None or (not self.createlex.strip()): 
            self.createlex = simpledialog.askstring("NEW LEXICON", "Enter the name of the new lexicon", parent=self.master)
    def create_l(self):
        """ creates a lexicon(.csv file)"""
        if  self.createlex != "":
            msg.showerror("Error", "Lexicon already created or loaded")
        else:
            self.createlexiconuserinput()
            if not os.path.exists(self.createlex+str(".csv")):
                with open(str(self.createlex)+str(".csv"), 'a+') as d:
                    thewriter = csv.writer(d)
                    thewriter.writerow(['Word', 'Definition'])
                msg.showinfo("SUCCESS", "THE FILE CREATED SUCCESSFULLY")
                self.button_menu_state_change()
            else:
                msg.showerror("ERROR", "THIS FILE ALREADY EXISTS")
                self.createlex = ""
    def load_l_user_input(self):
        """ load menu user input """
        self.loadlex = simpledialog.askstring("LOAD LEXICON", "Enter the name  of the lexicon you want to load (Case sensitive)")
        while self.loadlex is None: 
            self.loadlex = simpledialog.askstring("LOAD LEXICON", "Enter the name of the lexicon you want to load (Case sensitive)", parent=self.master)
    def load_l(self):
        """loads a lexicon(.csv file)"""
        if  self.createlex != "":
            msg.showerror("Error", "Lexicon already created or loaded")
        else:
            self.load_l_user_input()
            if str(self.loadlex+".csv") in os.listdir():
                self.createlex = self.loadlex 
                msg.showinfo("SUCCESS", "THE FILE LOADED SUCCESSFULLY")
                self.button_menu_state_change()
            else:
                msg.showerror("ERROR", "THERE IS NO FILE NAMED "+ str(self.loadlex+".csv"))
    def exitmenu(self):
        """ exit menu """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
def main():
    """ main f """ 
    root = Tk()
    LexiconCreator(root)
    root.mainloop()
if __name__ == '__main__':
    main()
    