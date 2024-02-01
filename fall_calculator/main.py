import tkinter as tk

# Constants
GRAVITY = 9.81  # m/s^2
AIR_RESISTANCE = 0.1  # arbitrary value

def calculate_fall():
    try:
        mass = float(entry_mass.get())
        height = float(entry_height.get())
        time = mass / AIR_RESISTANCE  # simple approximation
        final_time = time * (height / 100)  # assuming height is in meters
        result_text.set(f"Time of fall: {final_time} seconds")
    except ValueError:
        result_text.set("Please enter valid numbers.")

root = tk.Tk()
root.title("Fall Calculator")

# Create a StringVar for updating the label text
result_text = tk.StringVar()
result_text.set("Enter mass in kg and height in meters, then click Calculate.")

label_mass = tk.Label(root, text = "Mass (kg):")
label_mass.pack(padx = 10, pady = 10)  # Add padding

entry_mass = tk.Entry(root, width = 20, borderwidth = 5)
entry_mass.pack(padx = 10, pady = 10)  # Add padding

label_height = tk.Label(root, text = "Height (m):")
label_height.pack(padx = 10, pady = 10)  # Add padding

entry_height = tk.Entry(root, width = 20, borderwidth = 5)
entry_height.pack(padx = 10, pady = 10)  # Add padding

button_submit = tk.Button(root, text = "Calculate", command = calculate_fall)
button_submit.pack(padx = 10, pady = 10)  # Add padding

label_result = tk.Label(root, textvariable = result_text)
label_result.pack(padx = 10, pady = 10)  # Add padding

root.mainloop()