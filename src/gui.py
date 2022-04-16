from tkinter import Tk, LabelFrame, Label, Entry, StringVar, Button
from tkinter import messagebox, filedialog
from src.funciones import analize


class App(Tk):
    def __init__(self):
        super().__init__()
        self.bg_color = "#252626"

        self.title("Beatmap Directory")
        self.configure(bg=self.bg_color)
        self.resizable(width=False, height=False)
        self.geometry("450x130")

        self.inputtexto = StringVar()
        self.outputtexto = StringVar()

        frame = LabelFrame(self, padx=5, pady=5, bg="#393a3b", borderwidth=0)
        frame.place(x=10, y=10)

        instruccion = Label(
            frame, text="osu! songs folder :", bg="#393a3b", fg="#91d9ff"
        ).grid(row=0, column=0)

        inputboton = Entry(
            frame,
            textvariable=self.inputtexto,
            width=40,
            bg="#BFBFBF",
            borderwidth=0,
            insertbackground="yellow",
        ).grid(row=0, column=1)

        startboton = Button(
            self,
            text="Go",
            width=12,
            height=2,
            command=self.buscar,
            bg="#393a3b",
            fg="white",
            borderwidth=0,
        ).place(x=120, y=80)

        broswseboton = Button(
            self,
            text="Browse",
            padx=5,
            pady=6,
            command=self.browse,
            bg="#393a3b",
            fg="white",
            borderwidth=0,
        ).place(x=382, y=10)

        limpiarboton = Button(
            self,
            text="Clear text values",
            command=self.limpiar,
            height=2,
            bg="#393a3b",
            fg="white",
            borderwidth=0,
        ).place(x=242, y=80)

    def browse(self):
        b = filedialog.askdirectory()
        self.inputtexto.set(str(b))

    def buscar(self):
        gui_input = self.inputtexto.get()
        output = analize(gui_input)
        if len(gui_input) != 0:
            messagebox.showinfo("Beatmap directory", output)
        else:
            messagebox.showerror("Error", "Invalid path")

    def limpiar(self):
        self.inputtexto.set("")
        self.outputtexto.set("")
