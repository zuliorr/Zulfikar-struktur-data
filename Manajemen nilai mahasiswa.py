# Inisialisasi data awal mahasiswa (menggunakan struktur list sesuai ketentuan)
data_mahasiswa = [
    ["Ahmad", 85],
    ["Budi", 78],
    ["Citra", 90]
]

while True:
    # Tampilan Menu Utama
    print("\n====================================")
    print(" APLIKASI MANAJEMEN NILAI MAHASISWA")
    print("====================================")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Urutkan Data Berdasarkan Nilai")
    print("7. Hitung Rata-rata Nilai")
    print("8. Keluar")
    print("====================================")
    
    pilihan = input("Pilih menu 1-8: ")
    print("------------------------------------")

    # 1. TAMPILKAN DATA
    if pilihan == '1':
        if not data_mahasiswa:
            print("Data mahasiswa masih kosong.")
        else:
            print(f"{'No':<4} | {'Nama Mahasiswa':<20} | {'Nilai':<5}")
            print("-" * 35)
            for i, mhs in enumerate(data_mahasiswa):
                print(f"{i+1:<4} | {mhs[0]:<20} | {mhs[1]:<5}")
                
    # 2. TAMBAH DATA
    elif pilihan == '2':
        nama = input("Masukkan nama mahasiswa baru: ").strip()
        if nama == "":
            print("Nama tidak boleh kosong!")
            continue
        try:
            nilai = float(input("Masukkan nilai mahasiswa: "))
            data_mahasiswa.append([nama, nilai])
            print(f"Data {nama} berhasil ditambahkan.")
        except ValueError:
            print("Input nilai harus berupa angka!")

    # 3. UBAH DATA
    elif pilihan == '3':
        nama_cari = input("Masukkan nama mahasiswa yang ingin diubah: ").strip()
        ditemukan = False
        
        for mhs in data_mahasiswa:
            if mhs[0].lower() == nama_cari.lower():
                print(f"Data ditemukan: {mhs[0]} dengan nilai {mhs[1]}")
                try:
                    nilai_baru = float(input("Masukkan nilai baru: "))
                    mhs[1] = nilai_baru
                    print(f"Data nilai {mhs[0]} berhasil diubah menjadi {nilai_baru}.")
                except ValueError:
                    print("Input nilai harus berupa angka! Perubahan dibatalkan.")
                ditemukan = True
                break
        
        if not ditemukan:
            print(f"Mahasiswa dengan nama '{nama_cari}' tidak ditemukan.")

    # 4. HAPUS DATA
    elif pilihan == '4':
        nama_cari = input("Masukkan nama mahasiswa yang ingin dihapus: ").strip()
        ditemukan = False
        
        for mhs in data_mahasiswa:
            if mhs[0].lower() == nama_cari.lower():
                data_mahasiswa.remove(mhs)
                print(f"Data mahasiswa bernama {mhs[0]} berhasil dihapus.")
                ditemukan = True
                break
                
        if not ditemukan:
            print(f"Mahasiswa dengan nama '{nama_cari}' tidak ditemukan.")

    # 5. CARI DATA
    elif pilihan == '5':
        nama_cari = input("Masukkan nama mahasiswa yang dicari: ").strip()
        ditemukan = False
        
        print(f"\nHasil pencarian untuk '{nama_cari}':")
        print(f"{'Nama Mahasiswa':<20} | {'Nilai':<5}")
        print("-" * 28)
        
        for mhs in data_mahasiswa:
            # Menggunakan 'in' agar pencarian bersifat fleksibel (bisa keyword/sebagian nama)
            if nama_cari.lower() in mhs[0].lower():
                print(f"{mhs[0]:<20} | {mhs[1]:<5}")
                ditemukan = True
                
        if not ditemukan:
            print("Data tidak ditemukan.")

    # 6. URUTKAN DATA BERDASARKAN NILAI (Tertinggi ke Terendah)
    elif pilihan == '6':
        if not data_mahasiswa:
            print("Data kosong, tidak bisa mengurutkan.")
        else:
            # Menggunakan fungsi lambda untuk mengambil elemen indeks ke-1 (Nilai) sebagai acuan urutan
            data_terurut = sorted(data_mahasiswa, key=lambda x: x[1], reverse=True)
            print("Data Mahasiswa Berdasarkan Nilai Tertinggi:")
            print(f"{'No':<4} | {'Nama Mahasiswa':<20} | {'Nilai':<5}")
            print("-" * 35)
            for i, mhs in enumerate(data_terurut):
                print(f"{i+1:<4} | {mhs[0]:<20} | {mhs[1]:<5}")

    # 7. HITUNG RATA-RATA NILAI
    elif pilihan == '7':
        if not data_mahasiswa:
            print("Data kosong, rata-rata adalah 0.")
        else:
            total_nilai = sum(mhs[1] for mhs in data_mahasiswa)
            rata_rata = total_nilai / len(data_mahasiswa)
            print(f"Jumlah Mahasiswa : {len(data_mahasiswa)}")
            print(f"Total Nilai      : {total_nilai}")
            print(f"Rata-rata Nilai  : {rata_rata:.2f}")

    # 8. KELUAR
    elif pilihan == '8':
        print("Terima kasih telah menggunakan aplikasi ini. Sampai jumpa!")
        break

    else:
        print("Pilihan tidak valid! Silakan pilih menu 1-8.")
