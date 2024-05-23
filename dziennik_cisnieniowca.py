import tkinter as tk
from tkinter import messagebox, filedialog
import csv
import os

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
        self.current_file = os.path.join(os.path.expanduser("~"), "Desktop", "pomiary.txt")
        if not os.path.exists(self.current_file):
            self.create_initial_file()

        # Okno
        self.master.title("Dziennik ciśnieniowca")
        self.master.geometry("800x600")
        self.master.config(bg=BG_COLOR)

        # Tytuł okna
        self.title_label = tk.Label(self.master, text="Dziennik Ciśnieniowca", font=TITLE_FONT, bg=BG_COLOR, fg=TITLE_COLOR)
        self.title_label.pack(pady=30)

        self.main_frame = tk.Frame(self.master, bg=BG_COLOR)
        self.main_frame.pack(expand=True)

        # Przyciski
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

        self.quit_button = tk.Button(self.main_frame, text="Wyjście", command=self.master.quit,
                                    font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.quit_button.pack(pady=10)

    def create_initial_file(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.current_file = os.path.join(script_dir, "pomiary.txt")
        with open(self.current_file, "w") as file:
            file.write("Data; Czas; Ciśnienie skurczowe; Ciśnienie rozkurczowe; Puls\n")
    
    def open_add_window(self):
        self.add_window = tk.Toplevel(self.master)
        self.add_window.title("Nowy pomiar")
        self.add_window.geometry("600x400")
        self.add_window.config(bg=BG_COLOR)

        # Tytuł
        self.title_label = tk.Label(self.add_window, text="Dodaj nowy pomiar", font=TITLE_FONT, bg=BG_COLOR, fg=TITLE_COLOR)
        self.title_label.pack(pady=10, padx=20, anchor="w")

        # Data
        date_frame = tk.Frame(self.add_window, bg=BG_COLOR)
        date_frame.pack(pady=5, padx=20, anchor="w")

        self.date_label = tk.Label(date_frame, text="Data:", font=FONT, bg=BG_COLOR)
        self.date_label.pack(side="left", padx=(0, 5))

        self.year_entry = tk.Entry(date_frame, font=FONT, width=5)
        self.year_entry.pack(side="left", padx=(0, 5))
        self.year_entry.insert(0, "RRRR")

        self.month_entry = tk.Entry(date_frame, font=FONT, width=3)
        self.month_entry.pack(side="left", padx=(0, 5))
        self.month_entry.insert(0, "MM")

        self.day_entry = tk.Entry(date_frame, font=FONT, width=3)
        self.day_entry.pack(side="left", padx=(0, 5))
        self.day_entry.insert(0, "DD")

        #Czas
        time_frame = tk.Frame(self.add_window, bg=BG_COLOR)
        time_frame.pack(pady=5, padx=20, anchor="w")

        self.time_label = tk.Label(time_frame, text="Time:", font=FONT, bg=BG_COLOR)
        self.time_label.pack(side="left", padx=(0, 5))

        self.hour_entry = tk.Entry(time_frame, font=FONT, width=3)
        self.hour_entry.pack(side="left", padx=(0, 0))
        self.hour_entry.insert(0, "GG")

        self.colon_label = tk.Label(time_frame, text=":", font=FONT, bg=BG_COLOR)
        self.colon_label.pack(side="left")

        self.minute_entry = tk.Entry(time_frame, font=FONT, width=3)
        self.minute_entry.pack(side="left", padx=(0, 5))
        self.minute_entry.insert(0, "MM")

        #Cisnienie skurczowe
        pressure1_frame = tk.Frame(self.add_window, bg=BG_COLOR)
        pressure1_frame.pack(pady=5, padx=20, anchor="w")

        self.systolic_label = tk.Label(pressure1_frame, text="Ciśnienie skurczowe:", font=FONT, bg=BG_COLOR)
        self.systolic_label.pack(side="left", padx=(0, 5))

        self.systolic_entry = tk.Entry(pressure1_frame, font=FONT, width=5)
        self.systolic_entry.pack(side="left", padx=(0, 5))

        self.systolic_unit_label = tk.Label(pressure1_frame, text="mmHg", font=FONT, bg=BG_COLOR)
        self.systolic_unit_label.pack(side="left", padx=(0, 5))

        #Cisnienie rozkurczowe
        pressure2_frame = tk.Frame(self.add_window, bg=BG_COLOR)
        pressure2_frame.pack(pady=5, padx=20, anchor="w")

        self.diastolic_label = tk.Label(pressure2_frame, text="Ciśnienie rozkurczowe:", font=FONT, bg=BG_COLOR)
        self.diastolic_label.pack(side="left", padx=(0, 5))

        self.diastolic_entry = tk.Entry(pressure2_frame, font=FONT, width=5)
        self.diastolic_entry.pack(side="left", padx=(0, 5))

        self.diastolic_unit_label = tk.Label(pressure2_frame, text="mmHg", font=FONT, bg=BG_COLOR)
        self.diastolic_unit_label.pack(side="left", padx=(0, 5))

        #Puls
        pulse_frame = tk.Frame(self.add_window, bg=BG_COLOR)
        pulse_frame.pack(pady=5, padx=20, anchor="w")

        self.pulse_label = tk.Label(pulse_frame, text="Puls:", font=FONT, bg=BG_COLOR)
        self.pulse_label.pack(side="left", padx=(0, 5))

        self.pulse_entry = tk.Entry(pulse_frame, font=FONT, width=5)
        self.pulse_entry.pack(side="left", padx=(0, 5))

        #Przycisk zatwierdzania
        self.submit_button = tk.Button(self.add_window, text="Zatwierdź", command=self.add_measurement,
                                    font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.submit_button.pack(pady=20, padx=20, anchor="w")




    def open_search_window(self):
        self.search_window = tk.Toplevel(self.master)
        self.search_window.title("Szukaj pomiaru")
        self.search_window.geometry("400x300")
        self.search_window.config(bg=BG_COLOR)

        # Tytuł okna
        self.title_label = tk.Label(self.search_window, text="Wyszukaj pomiar", font=TITLE_FONT, bg=BG_COLOR, fg=TITLE_COLOR)
        self.title_label.pack(pady=30)

    def open_change_window(self):
        self.change_window = tk.Toplevel(self.master)
        self.change_window.title("Ścieżka zapisu")
        self.change_window.geometry("400x300")
        self.change_window.config(bg=BG_COLOR)

        # Tytuł okna
        self.title_label = tk.Label(self.change_window, text="Zmień ścieżkę zapisu", font=TITLE_FONT, bg=BG_COLOR, fg=TITLE_COLOR)
        self.title_label.pack(pady=30)

    def open_chart_window(self):
        self.chart_window = tk.Toplevel(self.master)
        self.chart_window.title("Wykres pomiarów")
        self.chart_window.geometry("400x300")
        self.chart_window.config(bg=BG_COLOR)

        # Tytuł okna
        self.title_label = tk.Label(self.chart_window, text="Utwórz wykres pomiarów", font=TITLE_FONT, bg=BG_COLOR, fg=TITLE_COLOR)
        self.title_label.pack(pady=30)

    def add_measurement(self):
        date = f"{self.year_entry.get()}-{self.month_entry.get()}-{self.day_entry.get()}"
        time = f"{self.hour_entry.get()}:{self.minute_entry.get()}"
        pressure1 = self.systolic_entry.get()
        pressure2 = self.diastolic_entry.get()
        pulse = self.pulse_entry.get()
        measurement_data = f"{date}; {time}; {pressure1}; {pressure2}; {pulse}\n"
        with open(self.current_file, "a") as file:
            file.write(measurement_data)
        self.add_window.destroy()

def main():
    root = tk.Tk()
    app = Dziennik_Cisnieniowca_Aplikacja(root)
    root.mainloop()

main()
