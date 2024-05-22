import tkinter as tk
from tkinter import messagebox, filedialog
import csv
import os
#Wstępne biblioteki potrzebne do pisania kodu

# Czcionka
FONT = ("Helvetica", 13)
TITLE_FONT = ("Helvetica", 22, "bold")

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
        self.title_label.pack(pady=30)

        self.main_frame = tk.Frame(self.master, bg=BG_COLOR)
        self.main_frame.pack(expand=True)
        #Przyciski
        self.add_button = tk.Button(self.main_frame, text="Nowy pomiar", command=self,
                                    font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.add_button.pack(pady=10)

        self.search_button = tk.Button(self.main_frame, text="Szukaj pomiaru", command=self,
                                    font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.search_button.pack(pady=10)

        self.change_button = tk.Button(self.main_frame, text="Zmien ścieżkę zapisu", command=self,
                                    font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.change_button.pack(pady=10)

        self.chart_button = tk.Button(self.main_frame, text="Utwórz wykres pomiarów", command=self,
                                    font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.chart_button.pack(pady=10)

        self.quit_button = tk.Button(self.main_frame, text="Wyjscie", command=self.master.quit,
                                     font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.quit_button.pack(pady=10)

def main():
    root = tk.Tk()
    app = Dziennik_Cisnieniowca_Aplikacja(root)
    root.mainloop()

main()
