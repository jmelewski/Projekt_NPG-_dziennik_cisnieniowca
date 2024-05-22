import tkinter as tk
from tkinter import messagebox, filedialog
import csv
import os
#Wstępne biblioteki potrzebne do pisania kodu

# Czcionka
FONT = ("Helvetica", 12)

# Kolory
BG_COLOR = "#fbaed2"
BUTTON_COLOR = "#fe28a2"
TEXT_COLOR = "#ffe4e1"

class Dziennik_Cisnieniowca_Aplikacja:
    def __init__(self, master):
        self.master = master
        self.master.title("Dziennik ciśnieniowca")
        self.master.geometry("600x400")
        self.master.config(bg=BG_COLOR)

        self.main_frame = tk.Frame(self.master, bg=BG_COLOR)
        self.main_frame.pack(expand=True)

def main():
    root = tk.Tk()
    app = Dziennik_Cisnieniowca_Aplikacja(root)
    root.mainloop()

main()
