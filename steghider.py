import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess
from tkinter import PhotoImage

def embed_data():
    image_file = filedialog.askopenfilename(title="Select Image File")
    if not image_file:
        return

    data_file = filedialog.askopenfilename(title="Select Data File")
    if not data_file:
        return

    password = password_entry.get()

    try:
        subprocess.run(["steghide", "embed", "-cf", image_file, "-ef", data_file, "-sf", "steg_image.jpg", "-p", password], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", str(e))
        return

    messagebox.showinfo("Success", "Data embedded and image saved successfully!")

def extract_data():
    steg_image_file = filedialog.askopenfilename(title="Select Steganographed Image")
    if not steg_image_file:
        return

    password = extract_password_entry.get()

    try:
        subprocess.run(["steghide", "extract", "-sf", steg_image_file, "-p", password], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", str(e))
        return

    messagebox.showinfo("Success", "Data extracted successfully!")

window = tk.Tk()
window.title("StegHider GUI")

 
window.configure(bg="black")

icon = PhotoImage(file='img/alien.png')
icon = icon.subsample(4)   
window.iconphoto(False, icon)

password_frame = tk.LabelFrame(window, text="Password", bg="black", fg="red")
password_frame.pack(padx=10, pady=10, fill=tk.BOTH)

password_label = tk.Label(password_frame, text="Password (optional):", bg="black", fg="red")
password_label.pack(pady=5)

password_entry = tk.Entry(password_frame, show="*", bg="black", fg="red")
password_entry.pack(pady=5)

embed_frame = tk.LabelFrame(window, text="Embed Data", bg="black", fg="red")
embed_frame.pack(padx=10, pady=10, fill=tk.BOTH)

embed_file_button = tk.Button(embed_frame, text="Select Data File", command=embed_data, bg="black", fg="red")
embed_file_button.pack(padx=10, pady=5)

extract_frame = tk.LabelFrame(window, text="Extract Data", bg="black", fg="red")
extract_frame.pack(padx=10, pady=10, fill=tk.BOTH)

extract_file_button = tk.Button(extract_frame, text="Select Steganographed Image", command=extract_data, bg="black", fg="red")
extract_file_button.pack(padx=10, pady=5)

extract_password_label = tk.Label(extract_frame, text="Password (optional):", bg="black", fg="red")
extract_password_label.pack(pady=5)

extract_password_entry = tk.Entry(extract_frame, show="*", bg="black", fg="red")
extract_password_entry.pack(pady=5)

window.mainloop()
