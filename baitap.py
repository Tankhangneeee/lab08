import tkinter as tk
from tkinter import filedialog, messagebox, Menu, Scrollbar, Text

class Notepad:
    def __init__(self, **kwargs):
        self.__root = tk.Tk()
        self.__thisWidth = kwargs.get('width', 300)
        self.__thisHeight = kwargs.get('height', 300)
        self.__thisTextArea = Text(self.__root)
        self.__thisMenuBar = Menu(self.__root)
        self.__thisFileMenu = Menu(self.__thisMenuBar, tearoff=0)
        self.__thisEditMenu = Menu(self.__thisMenuBar, tearoff=0)
        self.__thisHelpMenu = Menu(self.__thisMenuBar, tearoff=0)
        self.__thisScrollBar = Scrollbar(self.__thisTextArea)
        self.__file = None
        
        # Set icon
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        # Set window size and title
        self.__root.title("Untitled - Notepad")
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()
        left = (screenWidth - self.__thisWidth) / 2
        top = (screenHeight - self.__thisHeight) / 2
        self.__root.geometry(f'{self.__thisWidth}x{self.__thisHeight}+{int(left)}+{int(top)}')

        # Make the textarea auto-resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
        self.__thisTextArea.grid(sticky=tk.N + tk.E + tk.S + tk.W)
        
        # Add controls (widget)
        self.__thisFileMenu.add_command(label="New", command=self.__newFile)
        self.__thisFileMenu.add_command(label="Open", command=self.__openFile)
        self.__thisFileMenu.add_command(label="Save", command=self.__saveFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit", command=self.__quitApplication)
        
        self.__thisEditMenu.add_command(label="Cut", command=self.__cut)
        self.__thisEditMenu.add_command(label="Copy", command=self.__copy)
        self.__thisEditMenu.add_command(label="Paste", command=self.__paste)

        self.__thisHelpMenu.add_command(label="About Notepad", command=self.__showAbout)

        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)
        self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)
        self.__thisMenuBar.add_cascade(label="Help", menu=self.__thisHelpMenu)
        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=tk.RIGHT, fill=tk.Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def __quitApplication(self):
        self.__root.destroy()

    def __showAbout(self):
        messagebox.showinfo("Notepad", "Mrinal Verma")

    def __openFile(self):
        self.__file = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if self.__file:
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            with open(self.__file, "r") as file:
                self.__thisTextArea.delete(1.0, tk.END)
                self.__thisTextArea.insert(1.0, file.read())

    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, tk.END)

    def __saveFile(self):
        if self.__file is None:
            self.__file = filedialog.asksaveasfilename(
                initialfile='Untitled.txt',
                defaultextension=".txt",
                filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if self.__file:
            with open(self.__file, "w") as file:
                file.write(self.__thisTextArea.get(1.0, tk.END))
            self.__root.title(os.path.basename(self.__file) + " - Notepad")

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):
        self.__root.mainloop()

# Run main application
if __name__ == "__main__":
    notepad = Notepad(width=600, height=400)
    notepad.run()