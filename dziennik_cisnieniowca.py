import tkinter as tk
from tkinter import messagebox, filedialog
import csv
import os

# Font settings
FONT = ("Helvetica", 16)
TITLE_FONT = ("Helvetica", 42, "bold")

# Color settings
BG_COLOR = "#e0e0f0"
BUTTON_COLOR = "#509acc" #:3
TEXT_COLOR = "#ffffff"
TITLE_COLOR = "#333333"

class Dziennik_Cisnieniowca_Aplikacja:
    def __init__(self, master):
        self.master = master
        self.current_file = os.path.join(os.path.expanduser("~"), "Desktop", "pomiary.txt")

        self.measurements = []
        if not os.path.exists(self.current_file):
            self.create_initial_file()

        self.load_measurements()

        # Window settings
        self.master.title("Dziennik ciśnieniowca")
        self.master.geometry("800x600")
        self.master.config(bg=BG_COLOR)

        # Window title
        self.title_label = tk.Label(self.master, text="Dziennik Ciśnieniowca", font=TITLE_FONT, bg=BG_COLOR,
                                    fg=TITLE_COLOR)
        self.title_label.pack(pady=30)

        # Main frame for buttons
        self.main_frame = tk.Frame(self.master, bg=BG_COLOR)
        self.main_frame.pack(expand=True)

        # Buttons for various functionalities
        self.add_button = tk.Button(self.main_frame, text="Nowy pomiar", command=self.open_add_window,
                                    font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.add_button.pack(pady=10)

        self.view_button = tk.Button(self.main_frame, text="Zapisane pomiary", command=self.open_view_window,
                                     font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.view_button.pack(pady=10)

        self.search_button = tk.Button(self.main_frame, text="Szukaj pomiaru", command=self.open_search_window,
                                       font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.search_button.pack(pady=10)

        self.change_button = tk.Button(self.main_frame, text="Ścieżka zapisu", command=self.open_change_window,
                                       font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.change_button.pack(pady=10)

        self.chart_button = tk.Button(self.main_frame, text="Wykres pomiarów", command=self.open_chart_window,
                                      font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.chart_button.pack(pady=10)

        self.quit_button = tk.Button(self.main_frame, text="Wyjście", command=self.on_exit,
                                     font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.quit_button.pack(pady=10)

        self.master.protocol("WM_DELETE_WINDOW", self.on_exit)

    # Create the initial file with headers if it doesn't exist
    def create_initial_file(self):
        with open(self.current_file, "w") as file:
            file.write("Data; Czas; Ciśnienie skurczowe; Ciśnienie rozkurczowe; Puls\n")

    # Save the measurements to the file
    def save_measurements(self):
        with open(self.current_file, "w") as file:
            file.write("Data; Czas; Ciśnienie skurczowe; Ciśnienie rozkurczowe; Puls\n")
            for measurement in self.measurements:
                file.write("; ".join(measurement) + "\n")

    # Load measurements from the file
    def load_measurements(self):
        if os.path.exists(self.current_file):
            with open(self.current_file, "r") as file:
                reader = csv.reader(file, delimiter=';')
                next(reader)  # Skip the header
                self.measurements = [tuple(map(str.strip, row)) for row in reader]

    # Load measurements from a user-selected file
    def load_measurements_from_file(self):
        load_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if load_path:
            self.current_file = load_path
            with open(self.current_file, "r") as file:
                reader = csv.reader(file, delimiter=';')
                next(reader)  # Skip the header
                self.measurements = [tuple(row) for row in reader]
            self.save_measurements()
        else:
            self.load_measurements()

    # Exit the application and save measurements
    def on_exit(self):
        self.save_measurements()
        self.master.quit()

    # Open the window to add a new measurement
    def open_add_window(self):
        self.add_window = tk.Toplevel(self.master)
        self.add_window.title("Nowy pomiar")
        self.add_window.geometry("600x400")
        self.add_window.config(bg=BG_COLOR)

        # Title label for the add window
        self.title_label = tk.Label(self.add_window, text="Dodaj nowy pomiar", font=TITLE_FONT, bg=BG_COLOR,
                                    fg=TITLE_COLOR)
        self.title_label.pack(pady=10, padx=20, anchor="w")

        # Date entry fields
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

        # Time entry fields
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

        # Systolic pressure entry fields
        pressure1_frame = tk.Frame(self.add_window, bg=BG_COLOR)
        pressure1_frame.pack(pady=5, padx=20, anchor="w")

        self.systolic_label = tk.Label(pressure1_frame, text="Ciśnienie skurczowe:", font=FONT, bg=BG_COLOR)
        self.systolic_label.pack(side="left", padx=(0, 5))

        self.systolic_entry = tk.Entry(pressure1_frame, font=FONT, width=5)
        self.systolic_entry.pack(side="left", padx=(0, 5))

        self.systolic_unit_label = tk.Label(pressure1_frame, text="mmHg", font=FONT, bg=BG_COLOR)
        self.systolic_unit_label.pack(side="left", padx=(0, 5))

        # Diastolic pressure entry fields
        pressure2_frame = tk.Frame(self.add_window, bg=BG_COLOR)
        pressure2_frame.pack(pady=5, padx=20, anchor="w")

        self.diastolic_label = tk.Label(pressure2_frame, text="Ciśnienie rozkurczowe:", font=FONT, bg=BG_COLOR)
        self.diastolic_label.pack(side="left", padx=(0, 5))

        self.diastolic_entry = tk.Entry(pressure2_frame, font=FONT, width=5)
        self.diastolic_entry.pack(side="left", padx=(0, 5))

        self.diastolic_unit_label = tk.Label(pressure2_frame, text="mmHg", font=FONT, bg=BG_COLOR)
        self.diastolic_unit_label.pack(side="left", padx=(0, 5))

        # Pulse entry field
        pulse_frame = tk.Frame(self.add_window, bg=BG_COLOR)
        pulse_frame.pack(pady=5, padx=20, anchor="w")

        self.pulse_label = tk.Label(pulse_frame, text="Puls:", font=FONT, bg=BG_COLOR)
        self.pulse_label.pack(side="left", padx=(0, 5))

        self.pulse_entry = tk.Entry(pulse_frame, font=FONT, width=5)
        self.pulse_entry.pack(side="left", padx=(0, 5))

        # Submit button to add measurement
        self.submit_button = tk.Button(self.add_window, text="Zatwierdź", command=self.add_measurement,
                                       font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.submit_button.pack(pady=20, padx=20, anchor="w")

    # Open the window to view saved measurements
    def open_view_window(self):
        self.view_window = tk.Toplevel(self.master)
        self.view_window.title("Zapisane pomiary")
        self.view_window.geometry("900x720")
        self.view_window.config(bg=BG_COLOR)

        self.title_label = tk.Label(self.view_window, text="Historia zapisanych pomiarów", font=TITLE_FONT, bg=BG_COLOR,
                                    fg=TITLE_COLOR)
        self.title_label.pack(pady=30)

        # Text widget to display measurements
        self.measurements_text = tk.Text(self.view_window, font=FONT, bg=TEXT_COLOR, fg=BUTTON_COLOR, wrap=tk.WORD)
        self.measurements_text.pack(pady=10, padx=20, expand=True, fill=tk.BOTH)

        self.display_measurements()

    # Open the window to search for a specific measurement
    def open_search_window(self):
        self.search_window = tk.Toplevel(self.master)
        self.search_window.title("Szukaj pomiaru")
        self.search_window.geometry("600x400")
        self.search_window.config(bg=BG_COLOR)

        self.title_label = tk.Label(self.search_window, text="Wyszukaj pomiar", font=TITLE_FONT, bg=BG_COLOR,
                                    fg=TITLE_COLOR)
        self.title_label.pack(pady=30)

    # Open the window to change the save path
    def open_change_window(self):
        self.change_window = tk.Toplevel(self.master)
        self.change_window.title("Ścieżka zapisu")
        self.change_window.geometry("600x400")
        self.change_window.config(bg=BG_COLOR)

        # Tytuł okna
        self.title_label = tk.Label(self.change_window, text="Zmień ścieżkę zapisu", font=TITLE_FONT, bg=BG_COLOR, fg=TITLE_COLOR)
        self.title_label.pack(pady=10)

        # Entry field to display and change the current file path
        self.path_entry = tk.Entry(self.change_window, font=FONT, width=40)
        self.path_entry.pack(pady=10)
        self.path_entry.insert(0, self.current_file)

        # Button to update the save file path
        self.update_path_button = tk.Button(self.change_window, text="Zapisz ścieżkę", command=self.update_save_path,
                                            font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        self.update_path_button.pack(pady=20)

    def update_save_path(self):
        new_path = self.path_entry.get()
        if new_path:
            # Ensure the new path ends with ".txt"
            if not new_path.endswith(".txt"):
                new_path = os.path.join(new_path, "pomiary.txt")

            self.current_file = new_path
            self.save_measurements()

            # Close the change path window
            self.change_window.destroy()

    # Open the window to create a chart of measurements
    def open_chart_window(self):
        self.chart_window = tk.Toplevel(self.master)
        self.chart_window.title("Wykres pomiarów")
        self.chart_window.geometry("800x600")
        self.chart_window.config(bg=BG_COLOR)

        self.title_label = tk.Label(self.chart_window, text="Utwórz wykres pomiarów", font=TITLE_FONT, bg=BG_COLOR,
                                    fg=TITLE_COLOR)
        self.title_label.pack(pady=30)

    # Display all saved measurements in the text widget
    def display_measurements(self):
        self.measurements_text.delete(1.0, tk.END)
        for measurement in self.measurements:
            date, time, pressure1, pressure2, pulse = measurement
            self.measurements_text.insert(tk.END,
                                          f"Data: {date}\t\tCzas: {time}\nCiśnienie skurczowe:  {pressure1} mmHg\nCiśnienie rozkurczowe:  {pressure2} mmHg\nPuls:  {pulse} BPM\n\n")
        self.measurements_text.config(state=tk.DISABLED)

    # Add a new measurement to the file and list
    def add_measurement(self):
        date = f"{self.year_entry.get()}-{self.month_entry.get()}-{self.day_entry.get()}"
        time = f"{self.hour_entry.get()}:{self.minute_entry.get()}"
        pressure1 = self.systolic_entry.get()
        pressure2 = self.diastolic_entry.get()
        pulse = self.pulse_entry.get()
        measurement_data = f"{date}; {time}; {pressure1}; {pressure2}; {pulse}\n"
        with open(self.current_file, "a") as file:
            file.write(measurement_data)
        self.measurements.append((date, time, pressure1, pressure2, pulse))
        self.add_window.destroy()


# Main function to run the application
def main():
    root = tk.Tk()
    app = Dziennik_Cisnieniowca_Aplikacja(root)
    root.mainloop()


main()
