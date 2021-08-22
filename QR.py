import tkinter as tk
from tkinter import ttk
import pyqrcode


class QRCodeLabel(tk.Label):
    def __init__(self, parent, qr_data):
        super().__init__(parent)
        
        qrcode = pyqrcode.create(qr_data)
        tmp_file = "QRCode.png"
        
        qrcode.png(tmp_file, scale=8)
        self.image = tk.PhotoImage(file=tmp_file)
        self.configure(image=self.image)


class QRGenerator:

    def __init__(self, master):
        self.master = master
        self.master.title("QR Code Generator")

        self.url = tk.StringVar()

        self.Label = ttk.Label(self.master, text="Please enter the URL here:")
        self.Entry = ttk.Entry(self.master, width=100, textvariable=self.url)
        self.generateButton = ttk.Button(self.master, text="Generate QR Code", command=self.generate)
        self.QRLabel = None

        self.Label.grid(column=0, row=0)
        self.Entry.grid(column=0, row=1, pady=20, padx=10)
        self.generateButton.grid(column=0, row=2)

    def generate(self):
        self.QRLabel = QRCodeLabel(self.master, self.url.get())
        self.QRLabel.grid(column=0, row=4)


win = tk.Tk()
gui = QRGenerator(win)
win.mainloop()


