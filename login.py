import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
from datetime import datetime
from zoneinfo import ZoneInfo
from tkinter import simpledialog
import voucher as vc
import string

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

# Fungsi untuk memperbarui history dan poin
def update_history(member, action, amount, riwayat_belanja=None):
    now = datetime.now(ZoneInfo("Asia/Jakarta"))
    history_entry = {
        "action": action,
        "amount": amount,
        "date": now.strftime("%Y-%m-%d %H:%M:%S"),
    }
    if riwayat_belanja is not None:
        history_entry["riwayat_belanja"] = riwayat_belanja  # Menyimpan nilai belanja
    member["history"].append(history_entry)

def show_history(member):
    def edit_entry(selected_item):
        try:
            selected_values = tree.item(selected_item, 'values')
            date_str, action, old_amount, riwayat_belanja = selected_values

            # Konversi nilai lama ke integer
            old_amount = int(old_amount) if old_amount != "N/A" else 0
            riwayat_belanja = int(riwayat_belanja) if riwayat_belanja != "N/A" else 0

            # Prompt untuk nilai belanja baru
            new_riwayat_belanja = simpledialog.askinteger("Edit Nilai Belanja", "Masukkan nilai belanja yang baru:", initialvalue=riwayat_belanja)
            if new_riwayat_belanja is not None:
                # Hitung selisih poin
                old_poin = old_amount  # Jumlah poin lama
                new_poin = new_riwayat_belanja // 1000  # Poin baru berdasarkan nilai belanja baru
                diff_poin = new_poin - old_poin  # Selisih poin

                # Perbarui riwayat pada data anggota
                for entry in member['history']:
                    if entry['date'] == date_str and entry['action'] == action:
                        entry['riwayat_belanja'] = new_riwayat_belanja
                        entry['amount'] = new_poin  # Perbarui poin
                        break

                # Perbarui total poin member
                member['poin'] += diff_poin

                # Simpan perubahan ke file JSON
                members = memuat_data_member()
                for i, m in enumerate(members):
                    if m['no_telepon'] == member['no_telepon']:
                        members[i] = member
                        break
                simpan_data_member(members)

                # Perbarui tampilan di Treeview
                tree.item(selected_item, values=(date_str, action, new_poin, new_riwayat_belanja))
                messagebox.showinfo("Sukses", "Nilai belanja berhasil diupdate!")
        except ValueError:
            messagebox.showerror("Error", "Nilai belanja harus berupa angka!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        show_member_page(member)

    history_window = tk.Toplevel()
    history_window.title("Riwayat Poin")
    
    tree = ttk.Treeview(history_window, columns=('Tanggal', 'Aktivitas', 'Jumlah', 'Riwayat Belanja'), show='headings')
    tree.heading('Tanggal', text='Tanggal')
    tree.heading('Aktivitas', text='Aktivitas')
    tree.heading('Jumlah', text='Jumlah')
    tree.heading('Riwayat Belanja', text='Riwayat Belanja')
    tree.pack(fill=tk.BOTH, expand=True)

    for entry in member['history']:
        date_str = entry['date']
        formatted_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
        riwayat_belanja = entry.get("riwayat_belanja", "N/A")  # Ambil nilai belanja jika ada
        tree.insert('', tk.END, values=(formatted_date, entry['action'], entry['amount'], riwayat_belanja))

    tk.Button(history_window, text="Edit Nilai Belanja", command=lambda: edit_entry(tree.selection()[0])).pack(pady=10)


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

    login_window = tk.Tk()
    login_window.title("Login Member")
    login_window.attributes('-fullscreen', True)
    login_window.config(bg='#F5C400')
    login_window.bind("<Escape>", lambda e: login_window.attributes('-fullscreen', False))

    frame_login = tk.Frame(login_window, bg='#F5C400')
    frame_login.place(relx=0.5, rely=0.5, anchor='center')

    tk.Label(frame_login, text="Cari Member", bg='#F5C400', font=("segoe UI", 45, "bold")).grid(row=0, column=0, columnspan=2, pady=40)
    tk.Label(frame_login, text="Nomor Telepon:", bg='#F5C400', font=("Segoe UI", 20)).grid(row=1, column=0, padx=10, pady=10)
    entry_no_hp = tk.Entry(frame_login, width=22, font =("Segoe UI", 20))
    entry_no_hp.grid(row=1, column=1, padx=10, pady=10)
    tk.Button(frame_login, text="Cari", bg='#102A71', fg='white', font=("Segoe UI", 20), command=login).grid(row=2, column=0, columnspan=2, pady=30)
    
    login_window.mainloop()

# Fungsi untuk halaman member
def show_member_page(member):
    def tambah_poin():
        try:
            belanja = int(belanja_entry.get())
            poin_tambahan = belanja // 1000
            member['poin'] += poin_tambahan
            update_history(member, "tambah poin", poin_tambahan, belanja)  # Menyimpan nilai belanja
            
            members = memuat_data_member()
            for i, m in enumerate(members):
                if m['no_telepon'] == member['no_telepon']:
                    members[i] = member
                    break
            simpan_data_member(members)

            messagebox.showinfo("Berhasil", f"Poin berhasil ditambahkan! Poin total: {member['poin']}")
            belanja_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Masukkan nilai belanja yang valid!")
            belanja_entry.delete(0, tk.END)
        show_member_page(member)
    
    def close_member_window():
        member_window.destroy()

    member_window = tk.Tk()
    member_window.title("Member Dashboard")
    member_window.attributes('-fullscreen', True)
    member_window.config(bg='#F5C400')
    member_window.bind("<Escape>", lambda e: member_window.attributes('-fullscreen', False))

    page_member = tk.Frame(member_window, bg='#F5C400')
    page_member.place(relx=0.5, rely=0.5, anchor='center')

    tk.Label(page_member, text=f"Nama: {member['nama']}", bg='#F5C400', font=("Segoe UI", 20)).grid(row=0, column=0, columnspan=2, pady=10)
    tk.Label(page_member, text=f"E-mail: {member['e-mail']}", bg='#F5C400', font=("Segoe UI", 20)).grid(row=1, column=0, columnspan=2, pady=10)
    tk.Label(page_member, text=f"Poin: {member['poin']}", bg='#F5C400', font=("Segoe UI", 20)).grid(row=2, column=0, columnspan=2, pady=10)

    tk.Label(page_member, text="Nilai Belanja (Rp):", bg='#F5C400', font=("Segoe UI", 20)).grid(row=3, column=0, pady=10)
    belanja_entry = tk.Entry(page_member, width=22, font=("Segoe UI", 20))
    belanja_entry.grid(row=3, column=1, pady=10)
    
    tk.Button(page_member, text="Tambah Poin", bg='#102A71', fg='white', font=("Segoe UI", 15), command=tambah_poin).grid(row=4, column=0, columnspan=2, pady=20)
    tk.Button(page_member, text="Tukar Poin", command=lambda: vc.buat_menu_voucher(member['no_telepon']), bg='#102A71', fg='white', font=("Segoe UI", 15)).grid(row=5, column=0, columnspan=2, pady=20)
    tk.Button(page_member, text="History", command=lambda: show_history(member), bg='#102A71', fg='white', font=("Segoe UI", 15)).grid(row=6, column=0, columnspan=2, pady=20)
    tk.Button(page_member, text="Keluar", command=close_member_window, bg='#102A71', fg='white', font=("Segoe UI", 15)).grid(row=7, column=0, columnspan=2, pady=20)
    
# Jalankan aplikasi
if __name__ == "main":
    show_login_member()