import tkinter as tk
from tkinter import messagebox
import json
import voucher as vc

# Fungsi untuk memuat data member dari file JSON
def load_members():
    try:
        with open('members.json', 'r') as file:
            members = json.load(file)
            return members
    except FileNotFoundError:
        return []

# Fungsi untuk menyimpan data member ke file JSON
def save_members(members):
    with open('members.json', 'w') as file:
        json.dump(members, file, indent=4)

# Fungsi untuk memverifikasi nomor telepon
def verify_phone_number(phone_number):
    members = load_members()
    for member in members:
        if member.get('no_telepon') == phone_number:
            return member
    return None

# Fungsi untuk halaman login
def show_login_page():
    def handle_login():
        phone_number = phone_entry.get()
        member = verify_phone_number(phone_number)
        
        if member:
            login_window.destroy()
            show_member_page(member)
        else:
            messagebox.showerror("Error", "Nomor telepon tidak terdaftar!")
            phone_entry.delete(0, tk.END)

    # Buat window login
    login_window = tk.Tk()
    login_window.title("Login Member")
    login_window.attributes('-fullscreen', True)  # Set fullscreen
    login_window.config(bg='#F5C400')  # Background warna kuning

    # Tutup fullscreen dengan tombol Esc
    login_window.bind("<Escape>", lambda e: login_window.attributes('-fullscreen', False))

    # Frame utama untuk pusat elemen
    frame = tk.Frame(login_window, bg='#F5C400')
    frame.grid(row=0, column=0, padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor='center')  # Pusatkan frame

    tk.Label(frame, text="Login Member", bg='#F5C400', font=("segoe UI", 45, "bold")).grid(row=0, column=0, columnspan=2, pady=40)
    tk.Label(frame, text="Nomor Telepon:", bg='#F5C400', font=("Segoe UI", 20)).grid(row=1, column=0, padx=10, pady=10)
    phone_entry = tk.Entry(frame, width=22, font=("Segoe UI", 20))
    phone_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(frame, text="Login", bg='#102A71', fg='white', font=("Segoe UI", 20), command=handle_login).grid(row=2, column=0, columnspan=2, pady=30)

    login_window.mainloop()

# Fungsi untuk halaman member
def show_member_page(member):
    def add_points():
        try:
            belanja = int(belanja_entry.get())
            added_points = belanja // 1000
            member['poin'] += added_points
            members = load_members()
            for i, m in enumerate(members):
                if m['no_telepon'] == member['no_telepon']:
                    members[i] = member
                    break
            save_members(members)
            messagebox.showinfo("Berhasil", f"Poin berhasil ditambahkan! Poin total: {member['poin']}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan nilai belanja yang valid!")
    
    def close_member_window():
        member_window.destroy()  # Menutup jendela member

    # Buat window member
    member_window = tk.Tk()
    member_window.title("Member Dashboard")
    member_window.attributes('-fullscreen', True)
    member_window.config(bg='#F5C400')

    # Tutup fullscreen dengan tombol Esc
    member_window.bind("<Escape>", lambda e: member_window.attributes('-fullscreen', False))

    # Frame utama untuk pusat elemen
    frame = tk.Frame(member_window, bg='#F5C400')
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # Elemen dalam frame
    tk.Label(frame, text=f"Nama: {member['nama']}", bg='#F5C400', font=("Segoe UI", 20)).grid(row=0, column=0, columnspan=2, pady=10)
    tk.Label(frame, text=f"E-mail: {member['e-mail']}", bg='#F5C400', font=("Segoe UI", 20)).grid(row=1, column=0, columnspan=2, pady=10)
    tk.Label(frame, text=f"Poin: {member['poin']}", bg='#F5C400', font=("Segoe UI", 20)).grid(row=2, column=0, columnspan=2, pady=10)

    tk.Label(frame, text="Nilai Belanja (Rp):", bg='#F5C400', font=("Segoe UI", 20)).grid(row=3, column=0, pady=10)
    belanja_entry = tk.Entry(frame, width=22, font=("Segoe UI", 20))
    belanja_entry.grid(row=3, column=1, pady=10)

    tk.Button(frame, text="Tambah Poin", bg='#102A71', fg='white', font=("Segoe UI", 15), command=add_points).grid(row=4, column=0, columnspan=2, pady=20)
    tk.Button(frame, text="Tukar Poin", command=lambda: vc.buat_menu(member['no_telepon']),bg='#102A71', fg='white', font=("segoe UI", 15)).grid(row=5, column=0, columnspan=2, pady=20)
    tk.Button(frame, text="Keluar", command=close_member_window, bg='#102A71', fg='white', font=("Segoe UI", 15)).grid(row=6, column=0, columnspan=2, pady=20)
    
# Jalankan aplikasi
if __name__ == "__main__":
    show_login_page()