import tkinter as tk
from tkinter import messagebox
import csv
import json
import login as lg
import voucher as vc

# Path file JSON untuk menyimpan data member
members_file = "members.json"

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

# Fungsi untuk memuat data member dari file JSON
def load_members():
    try:
        with open(members_file, "r") as file:
            return json.load(file)  # Mengembalikan data member dalam bentuk list of dict
    except FileNotFoundError:
        # Jika file tidak ditemukan, buat file kosong
        return []

# Fungsi untuk menyimpan data member ke file JSON
def save_members(members):
    with open(members_file, "w") as file:
        json.dump(members, file, indent=4)
        print("Data disimpan:", members)  # Memastikan data sudah disimpan
  # Menyimpan data dalam format JSON yang terformat rapi

# Validasi admin login
def validasi_admin(admin_data, no_hp, password):
    return no_hp in admin_data and admin_data[no_hp] == password

# Fungsi untuk mengganti frame
def switch_frame(new_frame):
    global current_frame
    if current_frame is not None:
        current_frame.destroy()
    current_frame = new_frame
    current_frame.pack(fill="both", expand=True)

# Fungsi login admin
def login_admin():
    no_hp = entry_no_hp.get()
    password = entry_password.get()

    if validasi_admin(admin_data, no_hp, password):
        messagebox.showinfo("Login Berhasil", f"Selamat datang, Admin {no_hp}!")
        show_menu()  # Pindah ke menu utama setelah login berhasil
    else:
        messagebox.showerror("Login Gagal", "No HP atau Password salah. Silakan coba lagi.")

# Fungsi untuk mendaftarkan member baru
def daftar_member():
    nama = entry_nama.get()
    no_telepon = entry_no_telepon.get()
    email = entry_email.get()
    
    save_members(members)

    if not nama or not no_telepon or not email:
        messagebox.showwarning("Peringatan", "Semua field harus diisi!")
        return

    # Muat data member yang ada
    members = load_members()

    # Periksa apakah nomor telepon sudah terdaftar
    for member in members:
        if member["no_telepon"] == no_telepon:
            messagebox.showwarning("Peringatan", "Nomor telepon sudah terdaftar!")
            return

    # Tambahkan member baru ke daftar
    members.append({
        "no_telepon": no_telepon,
        "e-mail": email,
        "nama": nama,
        "poin": 0
    })

    # Simpan kembali data member ke file JSON
    save_members(members)

    messagebox.showinfo("Berhasil", f"Member {nama} berhasil didaftarkan!")
    entry_nama.delete(0, tk.END)
    entry_no_telepon.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Menampilkan form login
def show_login():
    login_frame = tk.Frame(root)
    tk.Label(login_frame, text="Login Admin", font=("Arial", 16)).pack(pady=10)

    global entry_no_hp, entry_password
    tk.Label(login_frame, text="No HP:").pack()
    entry_no_hp = tk.Entry(login_frame)
    entry_no_hp.pack()

    tk.Label(login_frame, text="Password:").pack()
    entry_password = tk.Entry(login_frame, show="*")
    entry_password.pack()

    tk.Button(login_frame, text="Login", command=login_admin).pack(pady=10)

    switch_frame(login_frame)

# Menampilkan menu utama
def show_menu():
    menu_frame = tk.Frame(root)
    tk.Label(menu_frame, text="Menu Utama", font=("Arial", 16)).pack(pady=10)
    tk.Button(menu_frame, text="Daftar Member", command=show_daftar_member).pack(pady=5)
    tk.Button(menu_frame, text="Login Member", command=lg.show_login_page).pack(pady=5)
    tk.Button(menu_frame, text="Keluar", command=root.quit).pack(pady=5)

    switch_frame(menu_frame)

# Menampilkan form pendaftaran member
def show_daftar_member():
    daftar_frame = tk.Frame(root)
    tk.Label(daftar_frame, text="Pendaftaran Member", font=("Arial", 16)).pack(pady=10)

    global entry_nama, entry_no_telepon, entry_email
    tk.Label(daftar_frame, text="Nama:").pack()
    entry_nama = tk.Entry(daftar_frame)
    entry_nama.pack()

    tk.Label(daftar_frame, text="No Telepon:").pack()
    entry_no_telepon = tk.Entry(daftar_frame)
    entry_no_telepon.pack()

    tk.Label(daftar_frame, text="Email:").pack()
    entry_email = tk.Entry(daftar_frame)
    entry_email.pack()

    tk.Button(daftar_frame, text="Daftar", command=daftar_member).pack(pady=5)
    tk.Button(daftar_frame, text="Kembali ke Menu Utama", command=show_menu).pack(pady=5)

    switch_frame(daftar_frame)

# Program utama
csv_file = 'admin_data.csv'
admin_data = baca_data_admin(csv_file)

root = tk.Tk()
root.title("Aplikasi Member")
root.geometry("300x400")

current_frame = None

# Mulai dengan halaman login admin
show_login()
root.mainloop()
