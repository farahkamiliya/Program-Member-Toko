import csv

# Dictionary untuk menyimpan data members
members = {}

def daftar_member():
    print("\n=== Pendaftaran Member ===")
    nama = input("Masukkan Nama: ")
    no_telepon = input("Masukkan No Telepon: ")
    email = input("Masukkan Email: ")

    # Simpan data member
    members[no_telepon] = {
        "nama": nama,
        "email": email,
        "poin": 0
    }
    print("Pendaftaran berhasil!")
    print("Data tersimpan:", members)

def baca_data_admin(filename):
    """Membaca data admin dari file CSV"""
    admin_data = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                admin_data[row['no_hp']] = row['password']
    except FileNotFoundError:
        print("File CSV tidak ditemukan. Pastikan file admin_data.csv ada.")
        exit()  # Hentikan program jika file tidak ditemukan
    return admin_data

def validasi_admin(admin_data, no_hp, password):
    """Memvalidasi login admin"""
    return no_hp in admin_data and admin_data[no_hp] == password

def login_admin(admin_data):
    """Fungsi untuk login admin dengan pengulangan jika gagal"""
    while True:
        print("\n=== Login Admin ===")
        no_hp = input("Masukkan No HP: ")
        password = input("Masukkan Password: ")

        if validasi_admin(admin_data, no_hp, password):
            print("Login berhasil! Selamat datang, Admin.")
            break  # Keluar dari loop jika login berhasil
        else:
            print("Bukan admin, silakan coba lagi.")

def main():
    csv_file = 'admin_data.csv'
    admin_data = baca_data_admin(csv_file)
    login_admin(admin_data)
    try:
        admin_data = baca_data_admin(csv_file)
    except FileNotFoundError:
        return
    
if __name__ == '__main__':
    main()

    while True:
        print("\nMenu Utama:")
        print("1. Daftar Member")
        print("2. login")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            daftar_member()
        elif pilihan == "3":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == '__main__':
    main()
