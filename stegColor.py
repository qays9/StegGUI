import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import PhotoImage

 
def open_image():
    global img_path, img, img_copy, img_disp
    img_path = filedialog.askopenfilename()
    img = Image.open(img_path)
    img_copy = img.copy()
    img_disp = ImageTk.PhotoImage(img)
    canvas.itemconfig(image_item, image=img_disp)

 
def save_image():
    global img_copy
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    img_copy.save(save_path)

 
def change_color():
    global img_copy, img_disp, color_index
    color_index = (color_index + 1) % len(colors)
    new_img = img.convert("RGB")
    pixels = new_img.load()
    for i in range(new_img.size[0]):
        for j in range(new_img.size[1]):
            r, g, b = pixels[i, j]
            new_r, new_g, new_b = map(int, colors[color_index](r, g, b))
            pixels[i, j] = (new_r, new_g, new_b)
    img_copy = new_img.copy()
    img_disp = ImageTk.PhotoImage(new_img)
    canvas.itemconfig(image_item, image=img_disp)

 
colors = [
    lambda r, g, b: (r, g, b),  # original  
    lambda r, g, b: (b, r, g),  # red and blue  
    lambda r, g, b: (g, b, r),  # green and blue  
    lambda r, g, b: (r & 0xFE, g & 0xFE, b & 0xFE),  # LSB bit masking
    lambda r, g, b: (255 - r, 255 - g, 255 - b),  # inverse
    lambda r, g, b: (255 - r, 255 - b, 255 - g),  # inverse with red and blue swap
    lambda r, g, b: (255 - g, 255 - b, 255 - r),  # inverse with green and blue swap
    lambda r, g, b: (g, b, r),  # red and green swap
    lambda r, g, b: (b, g, r),  # all colors swap
    lambda r, g, b: (r * 0.5, g * 0.5, b * 0.5),  # darkened colors
    lambda r, g, b: (r * 2, g * 2, b * 2),  # brightened colors
    lambda r, g, b: (max(0, r - 50), max(0, g - 50), max(0, b - 50)),  # darker colors
    lambda r, g, b: (min(255, r + 50), min(255, g + 50), min(255, b + 50)),  # brighter colors
    lambda r, g, b: (r * 0.5, 0, b * 0.5 + g * 0.5), #purple color
    lambda r, g, b: (255, 0, 255),  # purple
    lambda r, g, b: (128, 0, 128),  # purple
    lambda r, g, b: (153, 50, 204),  # purple
    lambda r, g, b: (218, 112, 214),  # purple
    lambda r, g, b: (148, 0, 211),  # purple
    lambda r, g, b: (138, 43, 226),  # purple
    lambda r, g, b: (186, 85, 211),  # purple
    lambda r, g, b: (153, 0, 153),  # purple
    lambda r, g, b: (216, 191, 216),  # purple
    lambda r, g, b: (221, 160, 221),  # purple
    lambda r, g, b: (255, 0, 0),  # red
    lambda r, g, b: (0, 255, 0),  # green
    lambda r, g, b: (0, 0, 255),  # blue
    lambda r, g, b: (255, 255, 0),  # yellow
    lambda r, g, b: (255, 0, 255),  # magenta
    lambda r, g, b: (0, 255, 255),  # cyan
    lambda r, g, b: (255, 255, 255),  # white
    lambda r, g, b: (0, 0, 0),  # black
    lambda r, g, b: (255, 128, 0),  # orange
    lambda r, g, b: (128, 0, 0),  # maroon
    lambda r, g, b: (0, 128, 0),  # olive
]

color_index = 0


root = tk.Tk()
root.title("StegColor")


 
icon = PhotoImage(file='img/alien.png')
icon = icon.subsample(4)   

 
root.iconphoto(False, icon)
 

 
window_width = 1000
window_height = 800






 
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

 
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, fill=tk.X)

 
open_button = tk.Button(button_frame, text="File", command=open_image)
open_button.pack(side=tk.LEFT, padx=15, pady=15)

 
save_button = tk.Button(button_frame, text="Save Image", command=save_image)
save_button.pack(side=tk.LEFT, padx=15, pady=15)

 
color_button = tk.Button(button_frame, text="Change Color", command=change_color)
color_button.pack(side=tk.LEFT, padx=15, pady=15)

 
img_disp = ImageTk.PhotoImage(Image.new("RGB", (window_width, window_height), "white"))

 
image_item = canvas.create_image(0, 0, anchor=tk.NW, image=img_disp)

 
root.mainloop()
