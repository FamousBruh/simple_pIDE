from tkinter import filedialog
from tkinter import *
from os import system, makedirs
import js2py

class editor:
    def __init__(self, root):
        self.root = root
        self.root.title("CRINGEPAD++")
        #self.root.geometry("700x645+200+150")
        #self.root.resizable(False, False)
        self.root.config(bg="black")
        self.dircheck = False
        if system == "win32":
            self.dir = "C:/"
        else:
            self.dir = "home/"

        self.main_shit = Frame(self.root, width = 680, height = 350)
        self.file_shit = Frame(self.root, width = 680, height = 95)
        self.term = Frame(self.root, width = 680, height = 200)
        self.main_shit.pack(expand=1, fill=X, side=TOP)
        self.term.pack(expand=1, fill=BOTH)
        self.file_shit.pack(expand=1, fill=X, side=BOTTOM)
        self.texts = []

        scroll_y = Scrollbar(self.main_shit,orient=VERTICAL)

        self.txtarea = Text(
            self.main_shit,
            yscrollcommand=scroll_y.set,
            font=("Courier New",18),
            state="normal",
            bg="#070d0f",
            fg="white",
            bd=0,
            highlightcolor="black",
            insertbackground="magenta",
            tabs=('0.25i', '0.4i', RIGHT, '0.6i', CENTER, '1i', NUMERIC),
            relief=GROOVE
        )

        scroll_y.config(command=self.txtarea.yview)
        

        self.save = Button(
            self.file_shit,
            text="Save",
            font=("Arial", 16, "bold"),
            command=self.save_file,
            relief=GROOVE
        )

        self.save_s = Button(
            self.file_shit,
            text="Save as",
            font=("Arial", 16, "bold"),
            command=self.save_as,
            relief=GROOVE
        )

        self.load = Button(
            self.file_shit,
            text="Load",
            font=("Arial", 16, "bold"),
            command=self.load_file,
            relief=GROOVE
        )

        self.run = Button(
            self.file_shit,
            text="Run",
            font=("Arial", 16, "bold"),
            command=self.run_code,
            relief=GROOVE
        )

        self.txtarea.pack(fill=BOTH, expand=1)
        #scroll_y.pack(side=RIGHT,fill=Y)
        self.wid = self.term.winfo_id()
        system("xterm -into %d -geometry 680x200 -sb -fa 'Monospace' -fs 14 &" % self.wid)
        self.save.pack(side=LEFT, fill=X, expand=True)
        self.save_s.pack(side=LEFT, fill=X, expand=True)
        self.load.pack(side=LEFT, fill=X, expand=True)
        self.run.pack(side=LEFT, fill=X, expand=True)
        
    def save_file(self):
        if not self.dircheck: self.save_as()
        f = open(self.dir, "w+")
        t = self.txtarea.get("1.0", "end-1c")
        f.write(t)
        f.close

    def save_as(self):
        try:
            t = self.txtarea.get("1.0", "end-1c")
            save_location = filedialog.asksaveasfilename(
                filetypes = (
                    ('Python files', "*.py"),
                    ('JavaScript files', "*.js"),
                    ('Text files', "*.txt"),
                    ('All files', '*.*')
                )
            )
            self.dir = save_location
            self.dircheck = True
            f = open(save_location, "w+")
            f.write(t)
            f.close()
        except: pass

    def load_file(self):
        try:
            f = filedialog.askopenfilename(
                initialdir = self.dir,
                title = "Select File",
                filetypes = (
                    ('Python files', "*.py"),
                    ('JavaScript files', "*.js"),
                    ('Text files', "*.txt"),
                    ('All files', '*.*')
                )
            )
            t = open(f).read()
            self.dir = f
            self.dircheck = True
            self.txtarea.delete('1.0', END)
            self.txtarea.insert("1.0", t)
        except: pass

    def run_code(self):
        code = self.txtarea.get("1.0", END)
        code.replace("document.write", "return")
        if self.dircheck: self.save_file()
        else: self.save_as()
        if(self.dir[-2:] == "py"):
            cmd = "python3 " + self.dir
        if(self.dir[-2:] == "js"):  
            cmd = "node " + self.dir
        system(cmd)

        

root = Tk()
editor(root)
root.mainloop()