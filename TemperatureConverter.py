import tkinter as tk
from tkinter import ttk, messagebox

class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Set theme colors
        bg_color = "#f0f0f0"
        button_color = "#4a7a8c"
        text_color = "#333333"
        self.root.configure(bg=bg_color)
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Temperature input
        ttk.Label(self.main_frame, text="Temperature:", font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.temp_entry = ttk.Entry(self.main_frame, font=('Arial', 12), width=15)
        self.temp_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # From unit
        ttk.Label(self.main_frame, text="From:", font=('Arial', 12)).grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.from_unit = tk.StringVar()
        self.from_combobox = ttk.Combobox(self.main_frame, textvariable=self.from_unit, 
                                         values=("Celsius", "Fahrenheit", "Kelvin"), 
                                         state="readonly", font=('Arial', 12), width=12)
        self.from_combobox.grid(row=1, column=1, padx=5, pady=5)
        self.from_combobox.current(0)
        
        # To unit
        ttk.Label(self.main_frame, text="To:", font=('Arial', 12)).grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.to_unit = tk.StringVar()
        self.to_combobox = ttk.Combobox(self.main_frame, textvariable=self.to_unit, 
                                       values=("Celsius", "Fahrenheit", "Kelvin"), 
                                       state="readonly", font=('Arial', 12), width=12)
        self.to_combobox.grid(row=2, column=1, padx=5, pady=5)
        self.to_combobox.current(1)
        
        # Convert button
        self.convert_button = ttk.Button(self.main_frame, text="Convert", 
                                        command=self.convert_temperature, 
                                        style='Accent.TButton')
        self.convert_button.grid(row=3, column=0, columnspan=2, pady=15, ipadx=10, ipady=5)
        
        # Result display
        self.result_label = ttk.Label(self.main_frame, text="", font=('Arial', 14, 'bold'))
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Swap button
        self.swap_button = ttk.Button(self.main_frame, text="↔ Swap Units", 
                                     command=self.swap_units, style='TButton')
        self.swap_button.grid(row=5, column=0, columnspan=2, pady=5)
        
        # Style configuration
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 10), padding=5)
        self.style.configure('Accent.TButton', font=('Arial', 10, 'bold'), 
                            background=button_color, foreground='white')
        self.style.map('Accent.TButton', 
                      background=[('active', button_color), ('pressed', button_color)])
        
        # Focus on entry widget
        self.temp_entry.focus()
        
    def convert_temperature(self):
        try:
            temp = float(self.temp_entry.get())
            from_unit = self.from_unit.get()[0].upper()  # Get first letter (C, F, K)
            to_unit = self.to_unit.get()[0].upper()
            
            if from_unit == to_unit:
                converted_temp = temp
            else:
                # First convert to Celsius if needed
                if from_unit == 'F':
                    celsius = (temp - 32) * 5/9
                elif from_unit == 'K':
                    celsius = temp - 273.15
                else:
                    celsius = temp
                
                # Then convert from Celsius to target unit
                if to_unit == 'F':
                    converted_temp = celsius * 9/5 + 32
                elif to_unit == 'K':
                    converted_temp = celsius + 273.15
                else:
                    converted_temp = celsius
            
            # Display result
            self.result_label.config(
                text=f"{temp:.2f}°{from_unit} = {converted_temp:.2f}°{to_unit}"
            )
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid temperature value")
            self.temp_entry.focus()
    
    def swap_units(self):
        current_from = self.from_unit.get()
        current_to = self.to_unit.get()
        
        self.from_unit.set(current_to)
        self.to_unit.set(current_from)
        
        # If there's a result, convert it immediately with swapped units
        if self.result_label.cget("text"):
            self.convert_temperature()

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()