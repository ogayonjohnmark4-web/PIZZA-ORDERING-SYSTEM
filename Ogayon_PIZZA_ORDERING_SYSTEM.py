#Step 1: Import the Libraries
import tkinter as tk
from tkinter import ttk, messagebox

#Step 2: Create the Price Lists
pizza_prices = {
    "Pepperoni": 220,
    "Hawaiian": 270,
    "Cheese": 188,
    "Bacon": 310,
    "Tuna": 400,
    "Vegetarian": 250
}

 
size_prices = {
    "Small": 0,
    "Medium": 110,
    "Large": 215,
    "Extra Large": 320
}
 
topping_prices = {
    "Extra Cheese": 30,
    "Mushrooms": 40,
    "Bacon": 50
}

#Step 3: Create the Main Window
window = tk.Tk()
window.title("Pizza Ordering System")
window.geometry("650x850")
window.resizable(True, True)
window.configure(bg="#32a852")

#Step 4: Create the Variables
pizza_var = tk.StringVar(value="Pepperoni")
size_var = tk.StringVar(value="Small")
quantity_var = tk.IntVar(value=1)
 
topping_vars = {
    topping: tk.BooleanVar(value=False)
    for topping in topping_prices
}

#Step 5: Add the Title
title = tk.Label(
    window,
    text="PIZZA ORDERING SYSTEM",
    font=("Arial", 22, "bold"),
    bg="#000000",
    fg="#ff9933"
)
title.pack(pady=20)

#Step 6: Create the Order Frame
order_frame = tk.Frame(
    window,
    bg="#2d2d2d",
    padx=25,
    pady=20
)
order_frame.pack(padx=25, fill="x")

#Step 7: Pizza Flavor (Drop-down List)
tk.Label(
    order_frame,
    text="Select Pizza Flavor:",
    font=("Arial", 12, "bold"),
    bg="#2d2d2d",
    fg="white"
).pack(anchor="w")
 
pizza_dropdown = ttk.Combobox(
    order_frame,
    textvariable=pizza_var,
    values=list(pizza_prices.keys()),
    state="readonly",
    font=("Arial", 11)
)
pizza_dropdown.pack(fill="x", pady=8)

#Step 8: Pizza Size (Radio Buttons)
tk.Label(
    order_frame,
    text="Select Pizza Size:",
    font=("Arial", 12, "bold"),
    bg="#2d2d2d",
    fg="white"
).pack(anchor="w", pady=(12, 5))
 
for size, price in size_prices.items():
 
    tk.Radiobutton(
        order_frame,
        text=f"{size} (+₱{price})",
        variable=size_var,
        value=size,
        font=("Arial", 11),
        bg="#2d2d2d",
        fg="white",
        selectcolor="#444444",
        activebackground="#2d2d2d",
        activeforeground="white"
    ).pack(anchor="w")

#Step 9: Extra Toppings (Checkboxes)
tk.Label(
    order_frame,
    text="Select Extra Toppings:",
    font=("Arial", 12, "bold"),
    bg="#2d2d2d",
    fg="white"
).pack(anchor="w", pady=(12, 5))
 
for topping, price in topping_prices.items():
 
    tk.Checkbutton(
        order_frame,
        text=f"{topping} (+₱{price})",
        variable=topping_vars[topping],
        font=("Arial", 11),
        bg="#2d2d2d",
        fg="white",
        selectcolor="#444444",
        activebackground="#2d2d2d",
        activeforeground="white"
    ).pack(anchor="w")

#Step 10: Quantity (Spinbox)
tk.Label(
    order_frame,
    text="Quantity:",
    font=("Arial", 12, "bold"),
    bg="#2d2d2d",
    fg="white"
).pack(anchor="w", pady=(12, 5))
 
quantity_spinbox = tk.Spinbox(
    order_frame,
    from_=1,
    to=50,
    textvariable=quantity_var,
    font=("Arial", 12),
    width=10
)
quantity_spinbox.pack(anchor="w")

#Step 11: The Function calculate_total()
def calculate_total():
 
    pizza = pizza_var.get()
    size = size_var.get()
    try:
        quantity = int(quantity_var.get())
 
        if quantity < 1 or quantity > 50:
            raise ValueError
 
    except (ValueError, tk.TclError):
 
        messagebox.showerror(
            "Invalid Quantity",
            "Please enter a quantity between 1 and 50."
        )
        return
    confirm = messagebox.askyesno(
        "Confirm Order",
        "Are you sure you want to place this order?"
    )
 
    if not confirm:
        return
        pizza_price = pizza_prices[pizza]
    size_price = size_prices[size]
    selected_toppings = [
        topping
        for topping, variable in topping_vars.items()
        if variable.get()
    ]
 
    topping_price = sum(
        topping_prices[topping]
        for topping in selected_toppings
    )
    total_per_pizza = pizza_price + size_price + topping_price
    total = total_per_pizza * quantity

    receipt_text.delete("1.0", tk.END)
 
    receipt_text.insert(
        tk.END,
        "========== ORDER RECEIPT ==========\n\n"
    )
 
    receipt_text.insert(tk.END, f"Pizza Flavor: {pizza}\n")
    receipt_text.insert(tk.END, f"Pizza Size: {size}\n")

#Step 12: The Function reset_order()
def reset_order():
 
    pizza_var.set("Pepperoni")
    size_var.set("Small")
    quantity_var.set(1)
 
    for variable in topping_vars.values():
        variable.set(False)
 
    receipt_text.delete("1.0", tk.END)

#Step 13: The Buttons
button_frame = tk.Frame(
    window,
    bg="#000000"
)
button_frame.pack(pady=15)
 
calculate_button = tk.Button(
    button_frame,
    text="PLACE ORDER",
    font=("Arial", 11, "bold"),
    bg="#ff9933",
    fg="black",
    width=18,
    command=calculate_total
)
calculate_button.grid(row=0, column=0, padx=8)
 
reset_button = tk.Button(
    button_frame,
    text="RESET",
    font=("Arial", 11, "bold"),
    bg="#555555",
    fg="white",
    width=12,
    command=reset_order
)
reset_button.grid(row=0, column=1, padx=8)

#Step 14: The Order Summary (Receipt Box)
tk.Label(
    window,
    text="ORDER SUMMARY",
    font=("Arial", 14, "bold"),
    bg="#000000",
    fg="#ff9933"
).pack(pady=5)
 
receipt_text = tk.Text(
    window,
    height=12,
    width=65,
    font=("Consolas", 11),
    bg="#2d2d2d",
    fg="white",
    insertbackground="white"
)
receipt_text.pack(padx=25, pady=10)

#Step 15: Run the Program
window.mainloop()

