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
        result_label.config(text="Voici votre nouveau message")
        result_text.config(text=result)  # Update the result label
    else:
        print("Selected algorithm not supported:", selected_algorithm)


# Colors
vert = "#B4E1DC"
rose = "#F5E5E5"
mauve = "#D9D0EB"
font_bold = ("Helvetica", 12, "bold")
font_regular = ("Helvetica", 12)

# Create the main window
root = tk.Tk()
root.title("Encryption and Decryption")
root.geometry("700x550")
root.configure(bg=rose)  # Set pink background for the entire window
root.option_add("*Font", font_regular)

# Create styles
style = ttk.Style(root)
style.configure("TFrame", background=rose, foreground=mauve, font=font_regular)
style.configure("TLabel", background=rose, font=font_regular)
style.configure("TCombobox", background=rose, font=font_regular)
style.configure("TButton", background=rose, foreground="black", font=font_bold)
style.configure("TEntry", background=rose, font=font_regular)
style.configure("TCheckbutton", background=rose, font=font_regular)

# Create a frame for the message input
# Label
message_frame = ttk.Label(root, text="Message", style="TLabel")
message_frame.pack(pady=10, padx=10, fill="both", expand=True)
# Input
entry_msg = tk.Entry(message_frame, width=40)  # Increase the width
entry_msg.pack(pady=5, padx=5, expand=True)
entry_msg.insert(0, "Bonjour Pauline !")  # Set default value to Bonjour Pauline

# Create a frame for the key input
# Label
key_frame = ttk.Label(root, text="Clé", style="TLabel")
key_frame.pack(pady=10, padx=10, fill="both", expand=True)
# Input
key_msg = ttk.Entry(key_frame, width=40)
key_msg.insert(0, "3")  # Set default value to 3
key_msg.pack(pady=5, padx=5, expand=True)
key_msg.config(
    validate="key",
    validatecommand=(root.register(lambda p: p.isdigit() or p == ""), "%P"),
)
# Encryption method
# Label
algo_frame = ttk.Label(root, text="Choisir une méthode :", style="TLabel")
algo_frame.pack(pady=2, padx=10, fill="x", expand=True)
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
    root,
    textvariable=algorithm_var,
    values=algorithms,
    state="readonly",
    style="TCombobox",
)
algorithm_dropdown.pack(pady=5, padx=10, fill="x", expand=True)
algorithm_dropdown.current(algorithms.index("César"))  # Set "César" as default
# Add a checkbox for newbie
newbie_contest_var = IntVar()  # Variable to hold the state of the checkbox
newbie_contest_checkbox = ttk.Checkbutton(
    root, text="Mode newbie Contest", variable=newbie_contest_var
)
newbie_contest_checkbox.pack()

# Buttons
# Frame
button_frame = ttk.Frame(root)
button_frame.pack(pady=5, padx=10, fill="x", expand=True)  # Pack the button frame

# Crypt
crypt_button = ttk.Button(
    button_frame, text="Crypt", command=lambda: process_input("crypt")
)
crypt_button.pack(side="left", padx=50)

# Decrypt
decrypt_button = ttk.Button(
    button_frame, text="Decrypt", command=lambda: process_input("decrypt")
)
decrypt_button.pack(side="right", padx=50)


# Add a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

result_text = tk.Label(root, text="")
result_text.pack(pady=10)

# Run the main event loop
root.mainloop()
