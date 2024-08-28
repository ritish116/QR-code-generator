import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk

def generate_qr_code():
    data = entry.get()
    if not data:
        messagebox.showerror("Input Error", "Please enter some data.")
        return
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    img_tk = ImageTk.PhotoImage(img)
    
    img_label.config(image=img_tk)
    img_label.image = img_tk

def save_image():
    if img_label.image:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")],
        )
        if file_path:
            img = img_label.image._PhotoImage__photo
            img.save(file_path)
    else:
        messagebox.showerror("Save Error", "No QR code to save.")


root = tk.Tk()
root.title("QR Code Generator")


tk.Label(root, text="Enter data for QR code:").pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=10)

img_label = tk.Label(root)
img_label.pack(pady=10)

save_button = tk.Button(root, text="Save QR Code", command=save_image)
save_button.pack(pady=10)

root.mainloop()
