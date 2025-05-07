import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import re

# Function to Convert DDM to DMS
def ddm_to_dms(ddm_coord):
    match = re.match(r"(\d+)° (\d+\.\d+)' ([NSWE])", ddm_coord)
    if not match:
        return "Invalid Format"
    
    degrees = int(match.group(1))
    minutes = float(match.group(2))
    direction = match.group(3)
    
    seconds = round((minutes - int(minutes)) * 60, 1)  # Convert Decimal Minutes to Seconds
    return f"{degrees}° {int(minutes)}' {seconds}\" {direction}"

# Function to Process Input Data
def process_data():
    raw_data = text_input.get("1.0", tk.END).strip().split("\n")
    
    output_data = []
    for coord in raw_data:
        dms = ddm_to_dms(coord)
        output_data.append([coord, dms])
    
    df = pd.DataFrame(output_data, columns=["DDM", "DMS"])
    
    save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if save_path:
        df.to_csv(save_path, index=False)
        messagebox.showinfo("Success", f"File saved: {save_path}")

# GUI Setup
root = tk.Tk()
root.title("DDM to DMS Converter")
root.geometry("400x300")

tk.Label(root, text="Paste DDM Coordinates Below:", font=("Arial", 12)).pack()
text_input = tk.Text(root, height=10, width=50)
text_input.pack()

tk.Button(root, text="Convert & Save", command=process_data, font=("Arial", 12)).pack()

root.mainloop()
