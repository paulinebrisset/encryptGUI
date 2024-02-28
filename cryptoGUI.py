import tkinter as tk
from tkinter import ttk
from tkinter import IntVar  # Add IntVar for handling checkbox state
from cesar import Cesar


def process_input(action=None):
    # Retrieve message input and key input
    message_input = entry_msg.get()
    key_input = key_msg.get()
    # Print the state of the checkbox
    print("Checkbox state:", type(newbie_contest_var.get()))
    try:
        # Convert key_input to int
        key_input = int(key_input)
        print("Key input:", key_input)
    except ValueError:
        print("Key input must be an integer")

    # Get the selected algorithm from the dropdown menu
    selected_algorithm = algorithm_var.get()
    print("Selected algorithm:", selected_algorithm)
    if selected_algorithm == "César":
        ces = Cesar()
        # Dynamically call the method based on the action
        method_to_call = getattr(ces, action)
        result = method_to_call(message_input, key_input, newbie_contest_var.get())
        print("Original Message:", message_input)
        print("Result:", result)
        result_label.config(text=result)  # Update the result label
    else:
        print("Selected algorithm not supported:", selected_algorithm)


# Add custom styles
vert = "#B4E1DC"
rose = "#F5E5E5"
mauve = "#D9D0EB"

# Create the main window
root = tk.Tk()
root.title("Encryption and Decryption")
root.geometry("700x550")  # Set the window size

# Create styles
style = ttk.Style(root)
style.element_create("plain.background", "from", "default")
style.configure("TFrame", background=vert)  # Set background color for frames
style.configure("TLabel", background=rose)  # Set background color for labels
style.configure(
    "TButton", background=mauve, foreground=vert, font=("Arial", 30, "bold")
)  # Set background and text color for buttons


# Create a frame for the message input
message_frame = ttk.LabelFrame(root, text="Message", style="TLabel")
message_frame.pack(pady=10, padx=10, fill="both", expand=True)
message_frame.config(style="TFrame")


# Create an input field for message
entry_msg = tk.Entry(message_frame, width=50)  # Increase the width
entry_msg.pack(pady=5, padx=5)

# Create a frame for the key input
key_frame = ttk.LabelFrame(root, text="Key")
key_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Create an input field for key
key_msg = tk.Entry(key_frame, width=30)
key_msg.pack(pady=5, padx=5)
key_msg.config(
    validate="key",
    validatecommand=(root.register(lambda p: p.isdigit() or p == ""), "%P"),
)

# Create a drop-down menu with the specified algorithms
algorithms = [
    "Atbash",
    "César",
    "Vigenère",
    "Homophone avec carré de Polybe",
    "Playfair",
    "Hill",
]
algorithm_var = tk.StringVar()
algorithm_dropdown = ttk.Combobox(
    root, textvariable=algorithm_var, values=algorithms, state="readonly"
)
algorithm_dropdown.pack(pady=5, padx=10, fill="both", expand=True)
algorithm_dropdown.current(algorithms.index("César"))  # Set "César" as default

# Create a frame for buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=5, padx=10, fill="both", expand=True)  # Pack the button frame

# Create a Crypt button
crypt_button = tk.Button(
    button_frame, text="Crypt", command=lambda: process_input("crypt")
)
crypt_button.pack(side="left", padx=10)

# Create a Decrypt buttons
decrypt_button = tk.Button(
    button_frame, text="Decrypt", command=lambda: process_input("decrypt")
)
decrypt_button.pack(side="right", padx=10)

# Add a checkbox
newbie_contest_var = IntVar()  # Variable to hold the state of the checkbox
newbie_contest_checkbox = tk.Checkbutton(
    root, text="Newbie Contest", variable=newbie_contest_var
)
newbie_contest_checkbox.pack()

# Add a label to display the result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run the main event loop
root.mainloop()
