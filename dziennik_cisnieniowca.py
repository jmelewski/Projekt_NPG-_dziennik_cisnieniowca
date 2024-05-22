import tkinter as tk
from tkinter import messagebox, filedialog
import csv
import os
#Wstępne biblioteki potrzebne do pisania kodu

# Czcionka
FONT = ("Helvetica", 13)
TITLE_FONT = ("Helvetica", 18, "bold")

# Kolory
BG_COLOR = "#fbaed2"
BUTTON_COLOR = "#fe28a2"
TEXT_COLOR = "#ffe4e1"
TITLE_COLOR = "#fc0fc0"

class Dziennik_Cisnieniowca_Aplikacja:
    def __init__(self, master):
        self.master = master
        #Okno
        self.master.title("Dziennik ciśnieniowca")
        self.master.geometry("600x400")
        self.master.config(bg=BG_COLOR)

        # Tytuł okna
        self.title_label = tk.Label(self.master, text="Dziennik Ciśnieniowca", font=TITLE_FONT, bg=BG_COLOR, fg=TITLE_COLOR)
        self.title_label.pack(pady=10)

        self.main_frame = tk.Frame(self.master, bg=BG_COLOR)
        self.main_frame.pack(expand=True)
        #Przyciski
        self.add_button = tk.Button(self.main_frame, text="Nowy Pomiar", command=self,
                                    font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.add_button.pack(pady=10)

def main():
    root = tk.Tk()
    app = Dziennik_Cisnieniowca_Aplikacja(root)
    root.mainloop()

main()
