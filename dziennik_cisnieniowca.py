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
        self.master.geometry("800x600")
        self.master.config(bg=BG_COLOR)

        # Tytuł okna
        self.title_label = tk.Label(self.master, text="Dziennik Ciśnieniowca", font=TITLE_FONT, bg=BG_COLOR, fg=TITLE_COLOR)
        self.title_label.pack(pady=30)

        self.main_frame = tk.Frame(self.master, bg=BG_COLOR)
        self.main_frame.pack(expand=True)
        #Przyciski
        self.add_button = tk.Button(self.main_frame, text="Nowy pomiar", command=self.open_add_window,
                                    font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.add_button.pack(pady=10)

        self.search_button = tk.Button(self.main_frame, text="Szukaj pomiaru", command=self.open_search_window,
                                    font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.search_button.pack(pady=10)

        self.change_button = tk.Button(self.main_frame, text="Ścieżka zapisu", command=self.open_change_window,
                                    font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.change_button.pack(pady=10)

        self.chart_button = tk.Button(self.main_frame, text="Wykres pomiarów", command=self.open_chart_window,
                                    font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.chart_button.pack(pady=10)

        self.quit_button = tk.Button(self.main_frame, text="Wyjscie", command=self.master.quit,
                                     font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.quit_button.pack(pady=10)

    def open_add_window(self):
        self.add_window = tk.Toplevel(self.master)
        self.add_window.title("Nowy pomiar")
        self.add_window.geometry("400x300")
        self.add_window.config(bg=BG_COLOR)

        # Tytuł okna
        self.title_label = tk.Label(self.add_window, text="Dodaj nowy pomiar", font=TITLE_FONT, bg=BG_COLOR, fg=TITLE_COLOR)
        self.title_label.pack(pady=30)

    def open_search_window(self):
        self.add_window = tk.Toplevel(self.master)
        self.add_window.title("Szukaj pomiaru")
        self.add_window.geometry("400x300")
        self.add_window.config(bg=BG_COLOR)

        # Tytuł okna
        self.title_label = tk.Label(self.add_window, text="Wyszukaj pomiar", font=TITLE_FONT, bg=BG_COLOR, fg=TITLE_COLOR)
        self.title_label.pack(pady=30)

    def open_change_window(self):
        self.add_window = tk.Toplevel(self.master)
        self.add_window.title("Ścieżka zapisu")
        self.add_window.geometry("400x300")
        self.add_window.config(bg=BG_COLOR)

        # Tytuł okna
        self.title_label = tk.Label(self.add_window, text="Zmień ścieżkę zapisu", font=TITLE_FONT, bg=BG_COLOR, fg=TITLE_COLOR)
        self.title_label.pack(pady=30)

    def open_chart_window(self):
        self.add_window = tk.Toplevel(self.master)
        self.add_window.title("Wykres pomiarów")
        self.add_window.geometry("400x300")
        self.add_window.config(bg=BG_COLOR)

        # Tytuł okna
        self.title_label = tk.Label(self.add_window, text="Utwórz wykres pomiarów", font=TITLE_FONT, bg=BG_COLOR, fg=TITLE_COLOR)
        self.title_label.pack(pady=30)

def main():
    root = tk.Tk()
    app = Dziennik_Cisnieniowca_Aplikacja(root)
    root.mainloop()

main()
