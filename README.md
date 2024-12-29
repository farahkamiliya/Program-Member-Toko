# Kelas, Kelompok, Anggota
Kelas : A

Kelompok : 13

Anggota :
1. Gym Fadhil Hidayatullah, I0324010, [@GymFadhil](https://github.com/GymFadhil)
2. Mar'atus Sholekhah, I0324019, [@maratussholekhah](https://github.com/maratussholekhah)
3. Farah Kamiliya Izzati, I0324045, [@farahkamiliya](https://github.com/farahkamiliya)

# Program-Member-Toko
Program ini dirancang untuk mengelola keanggotaan toko dengan efisien, mencakup data nama, nomor telepon, e-mail, dan jumlah poin setiap anggota. Fitur utama meliputi penambahan anggota baru, pengelolaan poin untuk menambah atau mengurangi berdasarkan transaksi atau penukaran voucher, serta pembaruan data anggota secara mudah. Program juga dilengkapi validasi nomor telepon admin untuk mencegah kebocoran data member. Dengan fitur-fitur ini, program membantu meningkatkan layanan pelanggan melalui sistem keanggotaan yang terstruktur dan bermanfaat.

# Fitur Aplikasi
1. Terdapat menu login admin toko
2. Terdapat menu Daftar/Login member
3. Menu Daftar dapat menambah data member baru
4. Menu login dapat memunculkan data member dengan cara memasukkan nomor telepon
5. Setelah memasukkan nomor telepon, data member yang sesuai akan muncul beserta poinnya
6. Terdapat menu menambah poin atau menukar poin
7. Poin bisa ditukar dengan voucher 25% atau 40% lalu muncul kode redeem

# Library yang digunakan
1. tkinter: Untuk membuat GUI (Graphical User Interface).
2. csv: Untuk membaca dan menulis file CSV.
3. json: Untuk membaca dan menulis file dalam format JSON
4. Pillow (PIL): Digunakan untuk memproses dan menampilkan gambar (Image, ImageTk).
5. string dan random: Untuk menghasilkan kode acak berupa kombinasi huruf dan angka.

# Diagram alir
![WhatsApp Image 2024-11-15 at 21 06 55_940ca628](https://github.com/user-attachments/assets/66f5b2d1-11ae-4669-bcc7-bf025a8a2ce9)

# Diagram alir (revisi)
![WhatsApp Image 2024-11-25 at 12 37 59_b4119b33](https://github.com/user-attachments/assets/baa63dd8-f089-4b42-ae5f-979027e060b6)

# Diagram alir (Revisi terakhir)
![membertoko7](https://github.com/user-attachments/assets/14ec0fea-cadc-4e7a-8b1d-1febe363162d)

Diagram alir di atas menggambarkan proses kerja sebuah sistem program keanggotaan yang mengelola data anggota, penukaran poin, dan pemberian voucher. Proses dimulai dengan login menggunakan nomor telepon dan password admin untuk mengakses menu utama. Dalam menu utama, terdapat tiga pilihan: mendaftarkan anggota baru, login sebagai anggota, atau keluar dari sistem.

  Jika memilih untuk mendaftar, pengguna akan mengisi data seperti nama, nomor telepon, dan email, yang kemudian disimpan oleh sistem. Setelah berhasil, akan muncul pesan konfirmasi bahwa pendaftaran telah selesai. Jika pengguna sudah menjadi anggota, mereka dapat login menggunakan nomor telepon yang sudah terdaftar. Jika nomor tersebut ditemukan di sistem, informasi anggota seperti nama, nomor telepon, email, dan poin terkini akan ditampilkan.

  Setelah login, anggota dapat memasukkan total belanja untuk menambahkan poin baru. Perhitungan poin dilakukan berdasarkan total belanja dibagi 1.000. Sistem kemudian menyimpan poin terkini yang telah diperbarui. Selanjutnya, anggota memiliki opsi untuk menukarkan poin dengan voucher. Jika memilih menukarkan poin, sistem akan menampilkan dua pilihan: voucher diskon 40% (dengan pengurangan 500 poin) atau voucher diskon 20% (dengan pengurangan 250 poin). Setelah penukaran berhasil, poin terkini akan diperbarui dan ditampilkan bersama kode redeem juga konfirmasi bahwa penukaran telah berhasil.

# Sitemap
![WhatsApp Image 2024-12-06 at 18 44 36_7982ebc8](https://github.com/user-attachments/assets/4e93d0cc-bdd6-42bc-9c98-61e720723a66)

