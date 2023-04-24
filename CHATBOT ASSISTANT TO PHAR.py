import tkinter as tk
from tkinter import messagebox
import pandas as pd

medicine_df = pd.DataFrame(columns=["Name", "Quantity"])

def add_medicine():
    name = medicine_name_entry.get()
    quantity = int(medicine_quantity_entry.get())
    medicine_df.loc[len(medicine_df)] = [name, quantity]
    medicine_df.to_excel("medicines.xlsx", index=False)
    medicine_name_entry.delete(0, tk.END)
    medicine_quantity_entry.delete(0, tk.END)

def delete_medicine():
    name = medicine_name_entry.get()
    quantity = int(medicine_quantity_entry.get())
    # Update the quantity of the specified medicine in the dataframe
    medicine_df.loc[medicine_df["Name"] == name, "Quantity"] -= quantity
    # Drop rows where quantity is zero or less
    medicine_df.drop(medicine_df[medicine_df["Quantity"] <= 0].index, inplace=True)
    # Save the updated dataframe to the Excel file
    medicine_df.to_excel("medicines.xlsx", index=False)
    medicine_name_entry.delete(0, tk.END)
    medicine_quantity_entry.delete(0, tk.END)
    # Show the updated dataframe in a message box
    messagebox.showinfo("Medicine Deletion", f"{quantity} quantity of {name} deleted.")

def view_medicines():
    medicines = medicine_df.to_string(index=False)
    view_window = tk.Toplevel(root)
    view_text = tk.Text(view_window)
    view_text.insert(tk.END, medicines)
    view_text.pack()

def order_medicine():
    name = medicine_name_entry.get()
    quantity_str = medicine_quantity_entry.get()
    if quantity_str:
        quantity = int(quantity_str)
        messagebox.showinfo("Medicine Order", f"{quantity} quantity of {name} ordered.")
        medicine_name_entry.delete(0, tk.END)
        medicine_quantity_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter a quantity.")


root = tk.Tk()
root.title("Medicine Chatbot")

medicine_name_label = tk.Label(root, text="Medicine Name")
medicine_name_entry = tk.Entry(root)

medicine_quantity_label = tk.Label(root, text="Quantity")
medicine_quantity_entry = tk.Entry(root)

add_button = tk.Button(root, text="Add Medicine", command=add_medicine)
delete_button = tk.Button(root, text="Delete Medicine", command=delete_medicine)
view_button = tk.Button(root, text="View Medicines", command=view_medicines)
order_button = tk.Button(root, text="Order Medicine", command=order_medicine)

medicine_name_label.grid(row=0, column=0)
medicine_name_entry.grid(row=0, column=1)

medicine_quantity_label.grid(row=1, column=0)
medicine_quantity_entry.grid(row=1, column=1)

add_button.grid(row=2, column=0)
delete_button.grid(row=2, column=1)
view_button.grid(row=3, column=0)
order_button.grid(row=3, column=1)

root.mainloop()
