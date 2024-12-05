import json
import tkinter as tk
from tkinter import messagebox
import json
import string
import random

current_frame = None
file_member = "members.json"
window = None

# Fungsi untuk mengganti frame
def switch_frame(new_frame):
    global current_frame
    if current_frame is not None:
        current_frame.destroy()
    current_frame = new_frame
    current_frame.pack(fill="both", expand=True)

# Fungsi untuk membaca data JSON
def baca_data():
    try:
        with open(file_member, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("Maaf", "Data member tidak ditemukan!")
        return []

# Fungsi untuk menyimpan data ke file JSON
def simpan_data(data):
    with open(file_member, "w") as file:
        json.dump(data, file, indent=4)
        
# Fungsi untuk menghasilkan kode acak
def generate_random_code(length=5):
    characters = string.ascii_uppercase + string.digits  # Kombinasi huruf besar dan angka
    return ''.join(random.choice(characters) for _ in range(length))

# Fungsi untuk menggunakan voucher
def gunakan_voucher(no_telepon, jumlah_poin):
    data = baca_data()
    member_found = next((m for m in data if m["no_telepon"] == no_telepon), None)

    if member_found is None:
        messagebox.showerror("Error", "Member tidak ditemukan!")
        return

    if member_found["poin"] >= jumlah_poin:
        member_found["poin"] -= jumlah_poin
        simpan_data(data)
        
        # Menghasilkan kode acak setelah voucher berhasil ditukar
        random_code = generate_random_code()
        
        messagebox.showinfo("Berhasil", f"Voucher berhasil digunakan!\nPoin Anda sekarang: {member_found['poin']}\nKode Anda: {random_code}")
    else:
        messagebox.showwarning("Gagal", "Poin Anda tidak mencukupi untuk voucher ini.")
        
# Fungsi untuk membuat menu voucher
def buat_menu(no_telepon):
    global window
    if window is not None and tk.Toplevel.winfo_exists(window):
        messagebox.showinfo("Info", "Jendela sudah terbuka!")
        return

    data = baca_data()
    member_found = next((m for m in data if m["no_telepon"] == no_telepon), None)

    if member_found is None:
        messagebox.showerror("Error", "Member tidak ditemukan!")
        return

    # Membuat window utama
    window = tk.Tk()
    window.title("Menu Voucher")
    window.attributes("-fullscreen", True)
    window.config(bg="#F5C400")

    # Keluar dari fullscreen dengan tombol Esc
    window.bind("<Escape>", lambda e: window.attributes("-fullscreen", False))

    # Frame utama untuk pusat elemen
    frame = tk.Frame(window, bg="#F5C400")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Menampilkan informasi pengguna
    tk.Label(frame, text=f" Tukar Poin", bg="#F5C400", font=("segoe UI", 45, "bold")).grid(row=0, column=0, columnspan=2, pady=20)
    tk.Label(frame, text=f"Nama: {member_found['nama']}", bg="#F5C400", font=("Segoe UI", 20)).grid(row=1, column=0, columnspan=2, pady=10)
    tk.Label(frame, text=f"Email: {member_found['e-mail']}", bg="#F5C400", font=("Segoe UI", 20)).grid(row=2, column=0, columnspan=2, pady=10)
    tk.Label(frame, text=f"Poin Anda: {member_found['poin']}", bg="#F5C400", font=("Segoe UI", 20)).grid(row=3, column=0, columnspan=2, pady=10)

    # Menampilkan opsi voucher
    tk.Label(frame, text="=== Pilih Voucher ===", bg="#F5C400", font=("Segoe UI", 20)).grid(row=4, column=0, columnspan=2, pady=20)
    tk.Button(frame, text="Voucher Diskon 40% (500 poin)", command=lambda: gunakan_voucher(no_telepon, 500), bg="#102A71", fg="white", font=("Segoe UI", 15)).grid(row=5, column=0, columnspan=2, pady=10)
    tk.Button(frame, text="Voucher Diskon 25% (250 poin)", command=lambda: gunakan_voucher(no_telepon, 250), bg="#102A71", fg="white", font=("Segoe UI", 15)).grid(row=6, column=0, columnspan=2, pady=10)

    window.mainloop()

# Fungsi untuk mereset variabel window
def reset_window():
    global window
    window = None