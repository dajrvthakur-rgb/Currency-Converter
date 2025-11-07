import tkinter as tk

# Exchange rates relative to 1 USD
rates = {
    "USD": 1,
    "INR": 88.79,
    "EUR": 0.86,
    "GBP": 0.76,
    "JPY": 153.95,
    "AUD": 1.53
}

def convert():
    try:
        amt = float(entry.get())
        from_cur = from_var.get()
        to_cur = to_var.get()
        converted = amt * (rates[to_cur]/rates[from_cur])
        result.set(f"{converted:.2f} {to_cur}")
    except:
        result.set("Invalid input")

root = tk.Tk()
root.title("Currency Converter")

tk.Label(root, text="Amount:").pack()
entry = tk.Entry(root); entry.pack()

tk.Label(root, text="From Currency:").pack()
from_var = tk.StringVar(value="USD")
tk.OptionMenu(root, from_var, *rates.keys()).pack()

tk.Label(root, text="To Currency:").pack()
to_var = tk.StringVar(value="INR")
tk.OptionMenu(root, to_var, *rates.keys()).pack()

tk.Button(root, text="Convert", command=convert).pack(pady=5)
result = tk.StringVar(); tk.Label(root, textvariable=result, font=("Arial",14)).pack()

root.mainloop()
