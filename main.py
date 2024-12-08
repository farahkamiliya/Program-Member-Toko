import tkinter as tk
from tkinter import messagebox
import csv
import json
from PIL import Image, ImageTk
import login as lg
from tkinter import *

root = tk.Tk()
root.title("Member Toko")
root.geometry("1290x1080") 
root.configure(bg='#F5C400')

# Fungsi untuk memvalidasi admin login
def validasi_admin(admin_data, no_hp, password):
    return no_hp in admin_data and admin_data[no_hp] == password

# Fungsi untuk membaca data admin dari file CSV
def baca_data_admin(filename):
    admin_data = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                admin_data[row['no_hp']] = row['password']
    except FileNotFoundError:
        messagebox.showerror("Error", "File admin_data.csv tidak ditemukan!")
    return admin_data

# Fungsi untuk menyimpan data member ke file JSON
def save_members(members):
    with open(members_file, "w") as file:
        json.dump(members, file, indent=4)
        print("Data disimpan:", members)

# Fungsi untuk memuat data member dari file JSON
def load_members():
    try:
        with open(members_file, "r") as file:
            return json.load(file)  # Mengembalikan data member dalam bentuk list of dict
    except FileNotFoundError:
        return []  # Jika file tidak ditemukan, buat file kosong

# Fungsi untuk mendaftarkan member baru
def daftar_member():
    nama = entry_nama.get()
    no_telepon = entry_no_telepon.get()
    email = entry_email.get()
    
    if not nama or not no_telepon or not email:
        messagebox.showwarning("Peringatan", "Semua field harus diisi!")
        return

    members = load_members()
    
    # Cek apakah no telepon hanya berisi angka
    if not no_telepon.isdigit():
        messagebox.showerror("Error", "No Telepon harus berupa angka!")
        return

    for member in members:
        if member["no_telepon"] == no_telepon:
            messagebox.showwarning("Peringatan", "Nomor telepon sudah terdaftar!")
            return

    members.append({
        "no_telepon": no_telepon,
        "e-mail": email,
        "nama": nama,
        "poin": 0
    })

    save_members(members)

    messagebox.showinfo("Berhasil", f"Member {nama} berhasil didaftarkan!")
    entry_nama.delete(0, tk.END)
    entry_no_telepon.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Fungsi untuk login admin
def login_admin():
    no_hp = entry_no_hp.get()
    password = entry_password.get()

    if validasi_admin(admin_data, no_hp, password):
        messagebox.showinfo("Login Berhasil", f"Selamat datang, Admin {no_hp}!")
        show_menu()
    else:
        messagebox.showerror("Login Gagal", "No HP atau Password salah. Silakan coba lagi.")

# Fungsi untuk menampilkan form login admin
def show_login_admin():
    loginAdmin = tk.Frame(root, bg="#F5C400") 
    loginAdmin.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    
    tk.Label(loginAdmin, text="Login Admin", bg="#F5C400", font=("segoe UI", 45)).grid(row=0, column=1, pady=(150,10), padx=150, sticky="w")
    from PIL import Image
    img = Image.open(r"D:\projecta\envprojecta\logo.png")
    img = img.resize((683, 149))
    img_tk = ImageTk.PhotoImage(img)
    label_img = tk.Label(loginAdmin, image=img_tk, bg="#F5C400")
    label_img.image = img_tk  # Menyimpan referensi gambar
    label_img.grid(row=2, column=0, padx=20, pady=20)

    global entry_no_hp, entry_password
    tk.Label(loginAdmin, text="No HP:", bg='#F5C400', font=("segoe UI", 20)).grid(row=1, column=1, pady=10, padx=20, sticky='E' + 'W' + 'S')
    entry_no_hp = tk.Entry(loginAdmin, width=22, font=("segoe UI", 20))
    entry_no_hp.grid(row=2, column=1, sticky='E' + 'W')

    tk.Label(loginAdmin, text="Password:", bg='#F5C400', font=("segoe UI", 20)).grid(row=3, column=1, padx=20, pady=10, sticky='E' + 'W')
    entry_password = tk.Entry(loginAdmin, width=22, font=("segoe UI", 20), show="*")
    entry_password.grid(row=4, column=1, sticky='E' + 'W')

    button_login_admin = tk.Button(loginAdmin, text="Login", bg='#102A71', fg='white', font=("segoe UI", 20), command=login_admin)
    button_login_admin.grid(row=5, column=1, pady=20, padx=20)

    switch_frame(loginAdmin)

# Fungsi untuk menampilkan menu utama
def show_menu():
    menu_utama = tk.Frame(root, bg="#F5C400")
    menu_utama.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    from PIL import Image
    img = Image.open(r"D:\projecta\envprojecta\logo.png")
    img = img.resize((683, 149))
    img_tk = ImageTk.PhotoImage(img)
    label_img = tk.Label(menu_utama, image=img_tk, bg="#F5C400")
    label_img.image = img_tk  # Menyimpan referensi gambar
    label_img.grid(row=3, column=0)
    
    tk.Label(menu_utama, text="Menu Utama", bg="#F5C400", font=("segoe UI", 45)).grid(row=0, column=1, pady=(150, 10), padx=150, sticky="w")
    
    button_daftarmember = tk.Button(menu_utama, text="Daftar Member", bg='#102A71', fg='white', font=("segoe UI", 20), command=show_daftar_member)
    button_daftarmember.grid(row=2, column=1, pady=10, padx=20)
    
    button_Loginmember = tk.Button(menu_utama, text="Login Member", bg='#102A71', fg='white', font=("segoe UI", 20), command=lg.show_login_member)
    button_Loginmember.grid(row=3, column=1, pady=10, padx=20)
    
    button_keluar = tk.Button(menu_utama, text="Keluar", bg='#102A71', fg='white', font=("segoe UI", 20), command=root.quit)
    button_keluar.grid(row=4, column=1, pady=10, padx=20)

    switch_frame(menu_utama)

# Fungsi untuk menampilkan form pendaftaran member
def show_daftar_member():
    daftar_member_frame = tk.Frame(root, bg="#F5C400")  
    daftar_member_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    tk.Label(daftar_member_frame, text="Daftar Member", bg='#F5C400', font=("segoe UI", 45, "bold")).grid(row=0, column=1, pady=(150,30), padx=150, sticky="w")
    from PIL import Image
    img = Image.open(r"D:\projecta\envprojecta\logo.png")
    img = img.resize((683, 149))
    img_tk = ImageTk.PhotoImage(img)
    label_img = tk.Label(daftar_member_frame, image=img_tk, bg="#F5C400")
    label_img.image = img_tk
    label_img.grid(row=2, column=0, padx=20, pady=20)

    global entry_nama, entry_no_telepon, entry_email
    tk.Label(daftar_member_frame, text="Nama:", bg='#F5C400', font=("segoe UI", 20)).grid(row=1, column=1, pady=10, padx=30, sticky="w")
    entry_nama = tk.Entry(daftar_member_frame, width=22, font=("segoe UI", 20))
    entry_nama.grid(row=1, column=1, padx=20, pady=10)

    tk.Label(daftar_member_frame, text="No Telepon:", bg='#F5C400', font=("segoe UI", 20)).grid(row=2, column=1, pady=10, padx=30, sticky="w")
    entry_no_telepon = tk.Entry(daftar_member_frame, width=22, font=("segoe UI", 20))
    entry_no_telepon.grid(row=2, column=1, padx=20, pady=10)

    tk.Label(daftar_member_frame, text="Email:", bg='#F5C400', font=("segoe UI", 20)).grid(row=3, column=1, pady=10, padx=30, sticky="w")
    entry_email = tk.Entry(daftar_member_frame, width=22, font=("segoe UI", 20))
    entry_email.grid(row=3, column=1, padx=20, pady=10)

    button_daftar = tk.Button(daftar_member_frame, text="Daftar", bg='#102A71', fg='white', font=("segoe UI", 15), command=daftar_member)
    button_daftar.grid(row=4, column=1, pady=10, padx=20)
    button_kembali = tk.Button(daftar_member_frame, text="Kembali ke Menu Utama", bg='#102A71', fg='white', font=("segoe UI", 15), command=show_menu)
    button_kembali.grid(row=5, column=1, pady=10, padx=20)

    switch_frame(daftar_member_frame)

# Fungsi untuk mengganti frame
def switch_frame(new_frame):
    global current_frame
    if current_frame:
        current_frame.destroy()  # Hapus frame sebelumnya
    new_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Tampilkan frame baru
    current_frame = new_frame

current_frame = None

csv_file = 'admin_data.csv'
admin_data = baca_data_admin(csv_file)
members_file = "members.json"  # Path file JSON untuk menyimpan data member

# Fungsi untuk keluar dari aplikasi jika tombol ESC ditekan
def keluar(event):
    root.quit()

# Mengaktifkan fullscreen
root.attributes('-fullscreen', True)

# Bind tombol ESC untuk keluar aplikasi
root.bind("<Escape>", keluar)

# Menampilkan form login admin pertama kali
show_login_admin()

root.mainloop()
