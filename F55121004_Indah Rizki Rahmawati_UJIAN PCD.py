import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

def brightness_correction(img):
    brightness = 100
    bright_img = cv2.add(img, brightness)
    return bright_img

def grayscale(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_img

# fungsi untuk menampilkan gambar dalam kotak
def show_image(img, x, y, title):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=img)
    label.image = img
    label.place(x=x, y=y)
    title_label = tk.Label(root, text=title)
    title_label.place(x=x, y=y-20)

# fungsi untuk memproses citra dan menampilkan hasilnya
def process_image(method):
    global original_img
    if method == 'brightness_correction':
        corrected_img = brightness_correction(original_img)
        show_image(corrected_img, 350, 120, 'Contrast Stretching')
    elif method == 'grayscale':
        corrected_img = grayscale(original_img)
        show_image(corrected_img, 630, 120, 'Grayscale')
    elif method == 'Histogram_Equalization':
        img_gray = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
        img_eq = cv2.equalizeHist(img_gray)
        img = img_eq
        show_image(img_eq, 910, 120, 'Histogram Equalization')

# fungsi untuk menampilkan informasi pembuat program
def show_creator():
    creator_label = tk.Label(root, text='Nama : Indah Rizki Rahmawati')
    creator_label.place(x=80, y=530)
    creator_label = tk.Label(root, text='NIM : F55121004')
    creator_label.place(x=400, y=530)
    creator_label = tk.Label(root, text='Kelas : A')
    creator_label.place(x=720, y=530)

# fungsi untuk membuka gambar
def open_image():
    global original_img
    file_path = filedialog.askopenfilename()
    if file_path:
        original_img = cv2.imread(file_path)
        show_image(original_img, 70, 120, 'Gambar Original')


# membuat jendela utama
root = tk.Tk()
root.geometry('1240x600')
root.title('GUI Aplikasi Penerapan Perbaikan Citra')

# menambahkan judul gambar original
title_label = tk.Label(root, text='Gambar Original')
title_label.place(x=70, y=20)

# menambahkan kotak untuk perbaikan citra
correction_box = tk.LabelFrame(root, text='Perbaikan Citra', padx=5, pady=5)
correction_box.place(x=50, y=20, width=1140, height=450)

# menambahkan tombol untuk membuka gambar
open_button = tk.Button(root, text='Pilih Gambar', command=open_image)
open_button.place(x=70, y=400)


# tombol untuk perbaikan metode 1 (grayscale)
brightness_button = tk.Button(correction_box, text='Metode Perbaikan 1', command=lambda: process_image('brightness_correction'))
brightness_button.pack(side=tk.RIGHT, padx=10)
brightness_button.place(x=350, y=8)

# tombol untuk perbaikan metode 2 (contrast stretching)
smoothing_button = tk.Button(correction_box, text='Metode Perbaikan 2', command=lambda: process_image('grayscale'))
smoothing_button.pack(side=tk.LEFT, padx=10, pady=10)
smoothing_button.place(x=640, y=8)

# tombol untuk perbaikan metode 3 (Histogram Equalization)
hist_eq_button = tk.Button(correction_box, text="Metode Perbaikan 3", command=lambda: process_image('Histogram_Equalization'))
hist_eq_button.pack(side=tk.LEFT, padx=10, pady=10)
hist_eq_button.place(x=890, y=8)

# menambahkan kotak untuk informasi pembuat program
creator_box = tk.LabelFrame(root, text='Creator', padx=5, pady=5)
creator_box.place(x=53, y=500, width=1140, height=70)

# menampilkan informasi pembuat program
show_creator()

# menjalankan program
root.mainloop()

