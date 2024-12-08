import tkinter as tk
from tkinter import messagebox
import json
import voucher as vc

# Fungsi untuk memuat data member dari file JSON
def memuat_data_member():
    try:
        with open('members.json', 'r') as file:
            members = json.load(file)
            return members
    except FileNotFoundError:
        return []

# Fungsi untuk menyimpan data member ke file JSON
def simpan_data_member(members):
    with open('members.json', 'w') as file:
        json.dump(members, file, indent=4)

# Fungsi untuk memverifikasi nomor telepon
def verifikasi_nomor_hp(nomor_hp):
    members = memuat_data_member()
    for member in members:
        if member.get('no_telepon') == nomor_hp:
            return member
    return None

# Fungsi untuk halaman login
def show_login_member():
    def login():
        nomor_hp = entry_no_hp.get()
        member = verifikasi_nomor_hp(nomor_hp)
        
        if member:
            login_window.destroy()
            show_member_page(member)
        else:
            messagebox.showerror("Error", "Nomor telepon tidak terdaftar!")
            entry_no_hp.delete(0, tk.END)

    # Buat window login
    login_window = tk.Tk()
    login_window.title("Login Member")
    login_window.attributes('-fullscreen', True)  # Set fullscreen
    login_window.config(bg='#F5C400')  # Background warna kuning

    # Tutup fullscreen dengan tombol Esc
    login_window.bind("<Escape>", lambda e: login_window.attributes('-fullscreen', False))

    # Frame utama untuk pusat elemen
    frame_login = tk.Frame(login_window, bg='#F5C400')
    frame_login.grid(row=0, column=0, padx=20, pady=20)
    frame_login.place(relx=0.5, rely=0.5, anchor='center')  # Pusatkan frame

    tk.Label(frame_login, text="Login Member", bg='#F5C400', font=("segoe UI", 45, "bold")).grid(row=0, column=0, columnspan=2, pady=40)
    tk.Label(frame_login, text="Nomor Telepon:", bg='#F5C400', font=("Segoe UI", 20)).grid(row=1, column=0, padx=10, pady=10)
    entry_no_hp = tk.Entry(frame_login, width=22, font=("Segoe UI", 20))
    entry_no_hp.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(frame_login, text="Login", bg='#102A71', fg='white', font=("Segoe UI", 20), command=login).grid(row=2, column=0, columnspan=2, pady=30)

    login_window.mainloop()

# Fungsi untuk halaman member
def show_member_page(member):
    def tambah_poin():
        try:
            belanja = int(belanja_entry.get())
            poin_tambahan = belanja // 1000
            member['poin'] += poin_tambahan
            members = memuat_data_member()
            for i, m in enumerate(members):
                if m['no_telepon'] == member['no_telepon']:
                    members[i] = member
                    break
            simpan_data_member(members)
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
    page_member = tk.Frame(member_window, bg='#F5C400')
    page_member.place(relx=0.5, rely=0.5, anchor='center')

    # Elemen dalam frame
    tk.Label(page_member, text=f"Nama: {member['nama']}", bg='#F5C400', font=("Segoe UI", 20)).grid(row=0, column=0, columnspan=2, pady=10)
    tk.Label(page_member, text=f"E-mail: {member['e-mail']}", bg='#F5C400', font=("Segoe UI", 20)).grid(row=1, column=0, columnspan=2, pady=10)
    tk.Label(page_member, text=f"Poin: {member['poin']}", bg='#F5C400', font=("Segoe UI", 20)).grid(row=2, column=0, columnspan=2, pady=10)

    tk.Label(page_member, text="Nilai Belanja (Rp):", bg='#F5C400', font=("Segoe UI", 20)).grid(row=3, column=0, pady=10)
    belanja_entry = tk.Entry(page_member, width=22, font=("Segoe UI", 20))
    belanja_entry.grid(row=3, column=1, pady=10)

    tk.Button(page_member, text="Tambah Poin", bg='#102A71', fg='white', font=("Segoe UI", 15), command=tambah_poin).grid(row=4, column=0, columnspan=2, pady=20)
    tk.Button(page_member, text="Tukar Poin", command=lambda: vc.buat_menu_voucher(member['no_telepon']),bg='#102A71', fg='white', font=("segoe UI", 15)).grid(row=5, column=0, columnspan=2, pady=20)
    tk.Button(page_member, text="Keluar", command=close_member_window, bg='#102A71', fg='white', font=("Segoe UI", 15)).grid(row=6, column=0, columnspan=2, pady=20)
    
# Jalankan aplikasi
if __name__ == "__main__":
    show_login_member()
