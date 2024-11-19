members = {}

def daftar_member():
    print("Pendaftaran Member")
    nama = input("Masukkan Nama: ")
    no_telepon = input("Masukkan No Telepon: ")
    email = input("Masukkan Email: ")
    
    members[no_telepon] = {
        "nama": nama,
        "email": email,
        "poin": 0
    }
    print("Pendaftaran berhasil!")
    print("Data tersimpan:", members)

def main():
    print("Selamat Datang di Program Member Toko")
import csv

def baca_data_admin(filename):
    admin_data = {}
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            admin_data[row['no_hp']] = row['password']
    return admin_data

def validasi_admin(admin_data, no_hp, password):
    if no_hp in admin_data and admin_data[no_hp] == password:
        return True
    return False

def main():
    csv_file = 'admin_data.csv'
    
    try:
        admin_data = baca_data_admin(csv_file)
    except FileNotFoundError:
        print("File CSV tidak ditemukan. Pastikan file admin_data.csv ada.")
        return
    
    print("=== Login Admin ===")
    no_hp = input("Masukkan No HP: ")
    password = input("Masukkan Password: ")
    

    if validasi_admin(admin_data, no_hp, password):
        print("Login berhasil! Selamat datang, Admin.")
    else:
        print("Bukan admin. Akses ditolak.")

if __name__ == '__main__':
    main()
git commit -m "Initial commit"

    while True:
        print("\nMenu Utama:")
        print("1. Daftar")
        print("2. keluar")
        pilihan = input("Pilih menu (1/2): ")

        if pilihan == "1":
            daftar_member()
        elif pilihan == "2":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()
