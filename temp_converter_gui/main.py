import tkinter as tk

def convert_temp():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_text.set(f"Temperature in Fahrenheit: {fahrenheit}")
    except ValueError:
        result_text.set("Please enter a valid number.")

root = tk.Tk()
root.title("Celsius to Fahrenheit")

# Create a StringVar for updating the label text
result_text = tk.StringVar()
result_text.set("Enter temperature in Celsius and click Convert.")

entry = tk.Entry(root, width = 20, borderwidth = 5)
entry.pack(padx = 10, pady = 10)  # padding

button_submit = tk.Button(root, text = "Convert", command = convert_temp)
button_submit.pack(padx = 10, pady = 10)  # Add padding so everything sits in the middle

label_result = tk.Label(root, textvariable = result_text)
label_result.pack(padx = 10, pady = 10)  # padding 

root.mainloop()