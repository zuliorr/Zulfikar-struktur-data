# soal:
# masukan nama anda ;{nama pendek anda}
# jika benar akan lanjut ke program selanjutnya
# jika salah, akan muncul pesan "silahkan coba lagi"

# buat program yang menampilkan tabel perkalian dari angka yang di masukan user (1,10).
# contoh:
# masukan angka:3 
# 3 x 1= 3
# 3 x 2= 6
# ...
# 3 x 1= 30

# jawab :

nama= input ("fikar")

if nama== "fikar":
    print("terimakasih telah mengisi nama pendek yang bener")
    print("silahkan lanjut ke program berikutnya")
    
else:
    print("nama pendek yang anda masukan salah")
    print("silahkan coba lagi")

angka= int (input("mau lihat perkalian berapa"))

for i in range (1,11):
    hasil= angka*i
    print(f"{angka}*{i}={hasil}")