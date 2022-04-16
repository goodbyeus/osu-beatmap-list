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

        self.input = StringVar()

        frame = LabelFrame(self, padx=5, pady=5, bg="#393a3b", borderwidth=0)
        frame.place(x=10, y=10)

        instruction = Label(
            frame, text="osu! songs folder :", bg="#393a3b", fg="#91d9ff"
        ).grid(row=0, column=0)

        input_bar = Entry(
            frame,
            textvariable=self.input,
            width=40,
            bg="#BFBFBF",
            borderwidth=0,
            insertbackground="yellow",
        ).grid(row=0, column=1)

        start_button = Button(
            self,
            text="Go",
            width=12,
            height=2,
            command=self.start,
            bg="#393a3b",
            fg="white",
            borderwidth=0,
        ).place(x=120, y=80)

        broswse_button = Button(
            self,
            text="Browse",
            padx=5,
            pady=6,
            command=self.open_directory,
            bg="#393a3b",
            fg="white",
            borderwidth=0,
        ).place(x=382, y=10)

        clean_button = Button(
            self,
            text="Clear input bar",
            command=self.clean,
            height=2,
            bg="#393a3b",
            fg="white",
            borderwidth=0,
        ).place(x=242, y=80)

    def open_directory(self):
        b = filedialog.askdirectory()
        self.input.set(str(b))

    def start(self):
        gui_input = self.input.get()
        output = analize(gui_input)
        if len(gui_input) != 0:
            messagebox.showinfo("Beatmap directory", output)
        else:
            messagebox.showerror("Error", "Invalid path")

    def clean(self):
        self.input.set("")
