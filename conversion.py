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
    for line in raw_data:
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        
        identifier, lat_ddm, lon_ddm = parts
        lat_dms = ddm_to_dms(lat_ddm)
        lon_dms = ddm_to_dms(lon_ddm)
        
        output_data.append([identifier, lat_ddm, lat_dms, lon_ddm, lon_dms])
    
    df = pd.DataFrame(output_data, columns=["Identifier", "Latitude DDM", "Latitude DMS", "Longitude DDM", "Longitude DMS"])
    
    save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if save_path:
        df.to_csv(save_path, index=False)
        messagebox.showinfo("Success", f"File saved: {save_path}")

# GUI Setup
root = tk.Tk()
root.title("DDM to DMS Converter")
root.geometry("500x350")

tk.Label(root, text="Paste Identifier & DDM Coordinates Below:", font=("Arial", 12)).pack()
text_input = tk.Text(root, height=10, width=60)
text_input.pack()

tk.Button(root, text="Convert & Save", command=process_data, font=("Arial", 12)).pack()

root.mainloop()
