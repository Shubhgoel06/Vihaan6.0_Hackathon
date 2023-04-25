import tkinter as tk
from PIL import ImageTk 
import datetime
from plyer import notification
import csv

bgcolour = '#a2d5c6'

def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def load_frame1():
    clear_widgets(frame1)
    clear_widgets(frame2)
    clear_widgets(frame3)
    frame1.tkraise()
    frame1.pack_propagate(False)
    logo_img = ImageTk.PhotoImage(file="E:/gui/health.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bgcolour)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Button(
        frame1,
        text="Your Reminders",
        font=("TkHeadingFont", 18),
        bg="light blue",
        fg="black",
        cursor="hand2",
        command=lambda:load_frame2()
    ).pack(pady=5, padx=200)

    tk.Button(
        frame1,
        text="Add Details",
        font=("TkHeadingFont", 18),
        bg="light blue",
        fg="black",
        cursor="hand2",
        command=lambda:load_frame6()
    ).pack(pady=5, padx=200)

    tk.Button(
    frame1,
    text="Chatbot",
    font=("TkHeadingFont", 18),
    bg="light blue",
    fg="black",
    cursor="hand2",
    command=lambda : load_frame3()
).pack(pady=5, padx=200)

def load_frame2():
    class InsulinReminderGUI:
        def _init_(self):
            self.root = tk.Tk()
            self.root.title("Insulin Reminder")
            self.root.configure(bg=bgcolour)
            self.reminder_time = None
            self.root.geometry("1300x700")

        # create label and entry for reminder time
            a=tk.Label(self.root, text="Enter the time you regularly inject insulin in hh:mm format:", bg=bgcolour, fg="black", font=40)
            a.pack(pady=50)
            self.reminder_entry = tk.Entry(self.root)
            self.reminder_entry.pack()

        # create button to set reminder time
            b=tk.Button(self.root, text="Set Reminder", height=2, width=10, bg="light blue", fg="black", command=self.set_reminder)
            b.pack(pady=50)

        # create label for insulin injection reminder
            self.injection_label = tk.Label(self.root, text="Inject your insulin now!!", font=("Arial Bold", 18))

        # create label and button for response
            c=tk.Label(self.root, text="Have you injected insulin?",bg=bgcolour, fg="black", font=26)
            c.pack()
            d=tk.Button(self.root, text="Yes",height=2, width=10, bg="light blue", fg="black" , font=26, command=self.check_food)
            d.pack(pady=20)
            h=tk.Button(self.root, text="No",height=2, width=10, bg="light blue", fg="black" , font=26, command=self.check_reminder)
            h.pack()

        # create label for food reminder
            self.food_label = tk.Label(self.root, text="Please eat a healthy meal now!!", font=("Arial Bold", 18))

        # create label and button for response
            e=tk.Label(self.root, text="Have you eaten properly?",bg=bgcolour, fg="black", font=26)
            e.pack(pady=20)
            f=tk.Button(self.root, text="Yes",height=2, width=10, bg="light blue", fg="black" , command=load_frame1())
            f.pack()
            g=tk.Button(self.root, text="No",height=2, width=10, bg="light blue", fg="black" , command=self.check_food)
            g.pack(pady=20)

        def set_reminder(self):
            user_input = self.reminder_entry.get()
            try:
                self.reminder_time = datetime.datetime.strptime(user_input, "%H:%M")
                self.reminder_entry.delete(0, tk.END)
                self.injection_label.pack()
                self.check_reminder()
            except ValueError:
                tk.messagebox.showerror("Error", "Invalid time format. Please enter the time in hh:mm format.")

        def check_reminder(self):
            current_time = datetime.datetime.now().time()
            if self.reminder_time and current_time >= self.reminder_time.time():
                self.injection_label.pack()
                notification.notify(title="⚠ INJECT INSULIN ⚠", message="Inject your insulin injection now!!",
                                    timeout=10)
            else:
                self.injection_label.pack()
                self.root.after(1, self.check_reminder)

        def injected(self):
            self.injection_label.pack()

        def eaten(self):
            self.food_label.pack()

        def check_food(self):
            self.food_label.pack()
            notification.notify(title="⚠ FOOD REMINDER ⚠", message="Please eat a healthy meal now!!", 
                                timeout=10)

        def start(self):
            self.root.mainloop()

    if _name_ == "_main_":
        gui = InsulinReminderGUI()
        gui.start()

def load_frame3():
    clear_widgets(frame2)
    clear_widgets(frame1)
    frame3.tkraise()
    frame3.pack_propagate(False)
    label = tk.Label(frame3,text="CHATBOT", bg=bgcolour, fg="black", font=("Arial",30), anchor="center")
    label.pack(padx=20, pady=100)

    tk.Button(
        frame3,
        text="Patient to Assistant",
        font=("TkHeadingFont", 18),
        bg="light blue",
        fg="black",
        cursor="hand2",
        command=lambda:load_frame4()
    ).pack(pady=20)

    tk.Button(
        frame3,
        text="Assistant to Pharmacist",
        font=("TkHeadingFont", 18),
        bg="light blue",
        fg="black",
        cursor="hand2",
        command=lambda:load_frame5()
    ).pack(pady=20)

    tk.Button(
        frame3,
        text="Back",
        font=("TkHeadingFont", 18),
        bg="light blue",
        fg="black",
        cursor="hand2",
        command=lambda:load_frame1()
    ).pack(pady=120)

def load_frame4():
    def welcome_message():
        response = input_box.get()
        if response.lower() == "yes":
            result_label.config(text="Your order will reach you soon.")
        else:
            result_label.config(text="Okay. Take care.")

# Create a new instance of Tkinter
    root = tk.Tk()

# Set the window title and dimensions
    root.title("Medicine Reorder Chatbot")
    root.geometry("1300x700")

# Create a label for the prompt
    prompt_label = tk.Label(root, text="You are running out of your medicines. Would you like to re-order them?", bg=bgcolour, fg="black", font=("Arial",30))
    prompt_label.pack(pady=100)

# Create an input box for the user's response
    input_box = tk.Entry(root, width=50)
    input_box.pack()
    input_box.configure(font=('Arial', 30))
    text_var = tk.StringVar()
    text_var.set('Some text')
    input_box.config(textvariable=text_var)

# Create a button to submit the user's response
    submit_button = tk.Button(root, text="Submit",font=("Arial",20), command=welcome_message, width=20, height=1)
    submit_button.pack(pady=20)

# Create a label to display the result of the chatbot's response
    result_label = tk.Label(root, text="", font=("Arial",20), bg=bgcolour )
    result_label.pack(pady=100)

# add bg colour
    root.configure(bg=bgcolour)

# Start the main event loop
    root.mainloop()

def load_frame5():
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
    root.geometry("1300x700")
    root.configure(bg=bgcolour)

    medicine_name_label = tk.Label(root, text="Medicine Name",bg=bgcolour,font=15)
    medicine_name_entry = tk.Entry(root)

    medicine_quantity_label = tk.Label(root, text="Quantity",bg=bgcolour,font=15)
    medicine_quantity_entry = tk.Entry(root)

    add_button = tk.Button(root, text="Add Medicine",height=2, width=12, bg="light blue", fg="black",  command=add_medicine)
    delete_button = tk.Button(root, text="Delete Medicine", height=2, width=12, bg="light blue", fg="black" , command=delete_medicine)
    view_button = tk.Button(root, text="View Medicines", height=2, width=12, bg="light blue", fg="black" ,command=view_medicines)
    order_button = tk.Button(root, text="Order Medicine", height=2, width=12, bg="light blue", fg="black" ,command=order_medicine)

    medicine_name_label.pack()
    medicine_name_entry.pack()

    medicine_quantity_label.pack()
    medicine_quantity_entry.pack()

    add_button.pack(padx=20)
    delete_button.pack()
    view_button.pack(padx=20)
    order_button.pack()

    root.mainloop()
def load_frame6():
    def save_patient_info():
        # Get the user input
        patient_name = name_entry.get()
        phone_number = int(phone_entry.get())
        delivery_address = address_entry.get()
        doctors_visit = visit_entry.get()
        medicines_name = medicine_entry.get()
        prescribed_duration = int(duration_entry.get())
        time_taken = time_entry.get()
        last_purchase_date = purchase_entry.get()
        
        # Write the user input to the CSV file
        with open('patient_info.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([patient_name, phone_number, delivery_address, doctors_visit, medicines_name, prescribed_duration, time_taken, last_purchase_date])
        
        # Clear the input fields
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        visit_entry.delete(0, tk.END)
        medicine_entry.delete(0, tk.END)
        duration_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
        purchase_entry.delete(0, tk.END)
        
        # Print a message to confirm that the data has been saved
        status_label.config(text="Patient information has been saved.", fg="green")

    # Create a window
    window = tk.Tk()
    window.title("Patient Information Form")
    window.configure(bg=bgcolour)
    window.geometry("1300x700")

    # Create labels and input fields
    name_label = tk.Label(window, text="Name:",bg=bgcolour,font=15)
    name_label.pack(pady=15)
    name_entry = tk.Entry(window)
    name_entry.pack()

    phone_label = tk.Label(window, text="Phone Number:",bg=bgcolour,font=15)
    phone_label.pack(pady=15)
    phone_entry = tk.Entry(window)
    phone_entry.pack()

    address_label = tk.Label(window, text="Delivery Address:",bg=bgcolour,font=15)
    address_label.pack(pady=15)
    address_entry = tk.Entry(window)
    address_entry.pack()

    visit_label = tk.Label(window, text="Doctor's Visit (YYYY-MM-DD):",bg=bgcolour,font=15)
    visit_label.pack(pady=15)
    visit_entry = tk.Entry(window)
    visit_entry.pack()

    medicine_label = tk.Label(window, text="Medicine Name:",bg=bgcolour,font=15)
    medicine_label.pack(pady=15)
    medicine_entry = tk.Entry(window)
    medicine_entry.pack()

    duration_label = tk.Label(window, text="Prescribed Duration (in days):",bg=bgcolour,font=15)
    duration_label.pack(pady=15)
    duration_entry = tk.Entry(window)
    duration_entry.pack()

    time_label = tk.Label(window, text="Time Taken:",bg=bgcolour,font=15)
    time_label.pack(pady=15)
    time_entry = tk.Entry(window)
    time_entry.pack()

    purchase_label = tk.Label(window, text="Last Purchase Date (YYYY-MM-DD):",bg=bgcolour,font=15)
    purchase_label.pack(pady=15)
    purchase_entry = tk.Entry(window)
    purchase_entry.pack()

    # Create a button to save the user input
    save_button = tk.Button(window, text="Save", bg= bgcolour, command=save_patient_info)
    save_button.pack(pady=15)

    # Create a label to display the status of the save operation
    status_label = tk.Label(window, text="", fg="red")
    status_label.pack()

    # Run the window
    window.mainloop()


root = tk.Tk()
root.title("HEALTH BUDDY")


frame1 = tk.Frame(root, width=1300, height=700, bg=bgcolour)
frame2 = tk.Frame(root, width=1300, height=700, bg=bgcolour)
frame3 = tk.Frame(root, width=1300, height=700, bg=bgcolour)
frame4 = tk.Frame(root, width=1300, height=700, bg=bgcolour)
frame5 = tk.Frame(root, width=1300, height=700, bg=bgcolour)
frame6 = tk.Frame(root, width=1300, height=700, bg=bgcolour)

for frame in (frame1, frame2, frame3, frame4):
    frame.grid(row=0, column=0, sticky="nesw")

load_frame1()
root.eval("tk::PlaceWindow . center")
root.mainloop()
