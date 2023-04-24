import tkinter as tk

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
root.geometry("400x300")

# Create a label for the prompt
prompt_label = tk.Label(root, text="You are running out of your medicines. Would you like to re-order them?")
prompt_label.pack()

# Create an input box for the user's response
input_box = tk.Entry(root)
input_box.pack()

# Create a button to submit the user's response
submit_button = tk.Button(root, text="Submit", command=welcome_message)
submit_button.pack()

# Create a label to display the result of the chatbot's response
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()
