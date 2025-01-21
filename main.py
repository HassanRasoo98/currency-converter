from tkinter import *
import requests

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            exchange_rate = data['rates'][to_currency]
            converted_amount = amount * exchange_rate
            result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            result_label.config(text="Error fetching exchange rates.")

    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid amount.")

def button_click(number):
    current = calculator_entry.get()
    calculator_entry.delete(0, END)
    calculator_entry.insert(0, str(current) + str(number))

def button_clear():
    calculator_entry.delete(0, END)

def button_equal():
    try:
        result = eval(calculator_entry.get())
        calculator_entry.delete(0, END)
        calculator_entry.insert(0, str(result))
    except:
        calculator_entry.delete(0, END)
        calculator_entry.insert(0, "Error")

# Create the main window
window = Tk()
window.title("Multi-Tool App")
window.configure(padx=20, pady=20, bg="#e0e0e0")
window.resizable(False, False)

# Currency Converter
currency_frame = LabelFrame(window, text="Currency Converter", padx=10, pady=10, bg="#e0e0e0")
currency_frame.grid(row=0, column=0, padx=10, pady=10)

# Create labels
from_currency_label = Label(currency_frame, text="From Currency:", font=("Arial", 12))
from_currency_label.grid(row=0, column=0, sticky=W)

to_currency_label = Label(currency_frame, text="To Currency:", font=("Arial", 12))
to_currency_label.grid(row=1, column=0, sticky=W)

amount_label = Label(currency_frame, text="Amount:", font=("Arial", 12))
amount_label.grid(row=2, column=0, sticky=W)

result_label = Label(currency_frame, text="", font=("Arial", 12, "bold"))
result_label.grid(row=4, column=0, columnspan=2)

# Create dropdown menus
from_currency_var = StringVar(currency_frame)
from_currency_var.set("USD")  # Default currency
from_currency_dropdown = OptionMenu(currency_frame, from_currency_var, "USD", "EUR", "GBP", "JPY", "CAD", "PKR")
from_currency_dropdown.config(font=("Arial", 12))
from_currency_dropdown.grid(row=0, column=1)

to_currency_var = StringVar(currency_frame)
to_currency_var.set("EUR")  # Default currency
to_currency_dropdown = OptionMenu(currency_frame, to_currency_var, "USD", "EUR", "GBP", "JPY", "CAD", "PKR")
to_currency_dropdown.config(font=("Arial", 12))
to_currency_dropdown.grid(row=1, column=1)

# Create entry field for amount
amount_entry = Entry(currency_frame, width=15, font=("Arial", 12))
amount_entry.grid(row=2, column=1)

# Create convert button
convert_button = Button(currency_frame, text="Convert", command=convert_currency, font=("Arial", 12))
convert_button.grid(row=3, column=0, columnspan=2)

# Calculator
calculator_frame = LabelFrame(window, text="Calculator", padx=10, pady=10, bg="#e0e0e0")
calculator_frame.grid(row=0, column=1, padx=10, pady=10)

# Create the entry field
calculator_entry = Entry(calculator_frame, width=20, borderwidth=5)
calculator_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_count = 1
col_count = 0

for button in buttons:
    button = Button(calculator_frame, text=button, padx=20, pady=20, command=lambda b=button: button_click(b), font=("Arial", 12))
    button.grid(row=row_count, column=col_count)
    col_count += 1
    if col_count > 3:
        col_count = 0
        row_count += 1

# Clear button
clear_button = Button(calculator_frame, text="Clear", padx=20, pady=20, command=button_clear, font=("Arial", 12))
clear_button.grid(row=5, column=0, columnspan=2)

# Equal button
equal_button = Button(calculator_frame, text="=", padx=20, pady=20, command=button_equal, font=("Arial", 12))
equal_button.grid(row=5, column=2, columnspan=2)

# Run the application
window.mainloop()