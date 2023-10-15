import os
import time
Username = "Admin"
Pegawai = "User"
Pass1 = "071"
Pass2 = "210"

menu = {
    "Nasi Goreng" : 12000,
    "Mie Goreng" : 15000,
    "Ayam Lalapan" : 15000,
    "Ayam Geprek" : 10000
}
minuman = {
    "Teh Es/Panas" : 3000,
    "Jeruk Es/Panas" : 3000,
    "Air Mineral" : 5000,
    "Kopi" : 4000
}

struk = []
def List_Menu():
    print("""
============================================================
          Daftar List Makanan Warung Suka Mundur
============================================================
        """)
    menu
    for barang, value in menu.items():
        print(barang, ": Rp.", value)
def List_Minuman():
    print("""
============================================================
          Daftar List Minuman Warung Suka Mundur
============================================================
        """)
    minuman
    for barang, value in minuman.items():
        print(barang, ": Rp.", value)
def tambah_menu():
    print("="*60)
    banyak_menu = int(input("Berapa Banyak menu yang ditambahkan : "))
    x = 0
    while x < banyak_menu: 
        print("Menu ke-", 1 + x)   
        input_menu = input("Masukkan Menu Baru : ")
        input_harga = int(input("Masukkan Harga : "))
        x += 1
        menu[input_menu] = input_harga
    print("""
    ============================================================
            Selamat Menu baru telah berhasil di tambahkan
    ============================================================
            """)
def tambah_minuman():
    print("="*60)
    banyak_menu = int(input("Berapa Banyak menu yang ditambahkan : "))
    x = 0
    while x < banyak_menu: 
        print("Menu ke-", 1 + x)
        input_minuman = input("Masukkan Minuman Baru : ")
        input_harga1 = int(input("Masukkan Harga : "))
        minuman[input_minuman] = input_harga1
    print("""
    ============================================================
            Selamat Menu baru telah berhasil di tambahkan
    ============================================================
            """)
def Up_menu():
    print("="*60)
    input_menu = input("Masukkan Menu : ")
    input_harga = int(input("Update Harga : "))
    up_minuman = str(input("Apakah anda ingin mengupdate menu minuman juga? [Y/N] : "))
    if up_minuman == "Y" or up_minuman == "Yes" or up_minuman == "y":
        input_minuman = input("Masukkan Minuman Baru : ")
        input_harga1 = int(input("Masukkan Harga : "))
        minuman[input_minuman] = input_harga1
    else:
        print("")
    print("""
============================================================
        Selamat Menu baru telah berhasil di Update
============================================================
        """)
    menu[input_menu] = input_harga
def delete_Menu():
    hapus_menu = str(input("Masukkan daftar menu yang ingin di hapus : "))
    if hapus_menu == "":
        print("Tidak ada Menu yang di Hapus")
    else:
        del menu[hapus_menu]
        print("""
============================================================
        Selamat Menu baru telah berhasil di Hapus
============================================================
        """)
        os.system('cls')
def delete_minuman():
    hapus_menu = str(input("Masukkan daftar menu yang ingin di hapus : "))
    if hapus_menu == "":
        print("Tidak ada Minuman yang di Hapus")
    else:
        del minuman[hapus_menu]
        print("""
============================================================
     Selamat Menu Minuman baru telah berhasil di Hapus
============================================================
        """)
        os.system('cls')
def main_menu():
    os.system("cls")
    while True:
        print("""
============================================================
 SELAMAT DATANG DALAM DATA ADIMINSTRASI WARUNG SUKA MUNDUR
============================================================
        """)
        print('1. List menu\n2. Tambahkan Menu\n3. Update Harga\n4. Hapus Menu\n5. exit')
        choice = str(input('Masukan pilihan: '))
        time.sleep(3)
        os.system('cls')
        if choice == '1':
            while True:
                print("""
============================================================
Tentukan pilihan menu yang ingin anda lihat
1. Menu Makanan
2. Menu Minuman
3. Kembali
============================================================
                """)
                milih = str(input("Silahkan Pilih Opsi : "))
                if milih == "1" or milih.lower == "menu makanan":
                    List_Menu()
                    print('\nTekan [Enter] untuk kembali')
                    input()
                    os.system('cls')
                elif milih == "2" or milih.lower == "menu minuman":
                    List_Minuman()
                    print('\nTekan [Enter] untuk kembali')
                    input()
                    os.system('cls')
                elif milih == "3" or milih.lower == "kembali":
                    print('\nTekan [Enter] untuk kembali Ke Menu Admin')
                    input()
                    os.system('cls')
                    break
        elif choice == '2':
            while True:
                print("""
============================================================
Tentukan pilihan menu yang ingin anda tambahkan
1. Menu Makanan
2. Menu Minuman
3. Kembali
============================================================
                """)
                tambah = str(input("Pilih Menu yang ingin di tambahkan : "))
                if tambah == "1" or tambah.lower == "makanan" or tambah.lower == "menu makanan":
                    tambah_menu()
                    print('\nTekan [Enter] untuk kembali')
                    input()
                    os.system('cls')
                elif tambah == "2" or tambah.lower == "minuman" or tambah.lower == "menu minuman":
                    tambah_minuman()
                    print('\nTekan [Enter] untuk kembali')
                    input()
                    os.system('cls')
                elif tambah == "3" or tambah.lower == "kembali":
                    print('\nTekan [Enter] untuk kembali Ke Menu Admin')
                    input()
                    os.system('cls')
                    break
                else:
                    print("\nMaaf menu yang anda masukkan tidak tersedia")
        elif choice == '3':
            Up_menu()
            print('\nTekan [Enter] untuk kembali')
            input()
            os.system('cls')
        elif choice == '4':
            while True:
                print("""
============================================================
Tentukan pilihan menu yang ingin anda Hapus
1. Menu Makanan
2. Menu Minuman
3. Kembali
============================================================
                """)
                milih = str(input("Silahkan Pilih Opsi : "))
                if milih == "1" or milih == "Menu Makanan":
                    delete_Menu()
                    print('\nTekan [Enter] untuk kembali')
                    input()
                    os.system('cls')
                elif milih == "2" or milih == "Menu Minuman":
                    delete_minuman()
                    print('\nTekan [Enter] untuk kembali')
                    input()
                    os.system('cls')
                elif milih == "3" or milih == "Kembali":
                    print('\nTekan [Enter] untuk kembali Ke Menu Admin')
                    input()
                    os.system('cls')
                    break
        elif choice == '5':
            print("""
============================================================
          Anda Telah Log Out dari akun Admin
============================================================
        """)
            time.sleep(3)
            os.system('cls')
            break
def bayar(total):
    x = int(input("Nominal Pembayaran: Rp"))
    kembalian = x - total
    if kembalian >= 0:
        print("Kembalian: Rp%i" %kembalian)
    else:
        print("Uang Untuk Pembayaran Kurang!")
        bayar()    

def potongan_harga():
    print("="*60)
    total1 = sum(struk)
    Diskon = str(input("Masukkan Hari Pembelian : "))
    if Diskon.lower =="jum'at" or Diskon.lower == "jumat":
        total = total1 * 90/100
        print("""
============================================================
Selamat Anda Mendapatkan Potongan Jum'at Berkah Sebesar 10%!
Total Yang Harus Dibayar: Rp.{}
============================================================
""".format(total))
        print("")
        bayar(total)
    elif Diskon.lower == "sabtu" or Diskon.lower =="minggu":
        total = total1 * 75/100
        print("""
============================================================
Selamat Anda Mendapatkan Potongan Harga Sebesar 25%!
Total Yang Harus Dibayar: Rp.{}
============================================================
""".format(total))
        bayar(total)
    else:
        total = total1
        print("""
============================================================
Maaf Tidak ada Diskon Hari Ini...
Total Pembelian anda : Rp. {}
============================================================
""".format(total))
        bayar(total)
        time.sleep(4)
        os.system('cls')
def kasir():
    print("""
============================================================
            Daftar Makanan Warung Suka Mundur
============================================================
        """)
    menu
    for barang, value in menu.items():
        print(barang, ': Rp.', value)
    banyak_yang_dipesan = int(input("Berapa banyak makanan yang anda pesan: "))
    z = 0
    while z < banyak_yang_dipesan:
        print('------------------')
        print("Pesanan Ke -", 1+z)
        x = menu[input('Masukan Pesanan anda? :')]
        y = int(input('Berapa banyak yang anda ingin beli? :'))
        print("------------------")
        z += 1
        jumlah1 = x * y
        struk.append(jumlah1)
    minum = str(input("Apa anda ingin memesan Minuman? [Y/N] : "))
    if minum == "Y" or minum == "Yes" or minum == "y":
        print("""
============================================================
            Daftar Minuman Warung Suka Mundur
============================================================
        """)
        for barang, value in minuman.items():
            print(barang, ': Rp.', value)
        banyak_yang_dipesan = int(input("Berapa banyak makanan yang anda pesan: "))
        x = 0
        while x < banyak_yang_dipesan:
            print('------------------')
            x = minuman[input('Masukan Pesanan anda? :')]
            y = int(input('Berapa banyak yang anda ingin beli? :'))
            print('------------------')
            jumlah2 = x * y
            struk.append(jumlah2)
        potongan_harga()
    else:
        potongan_harga()

while True:
    print("""
============================================================
    Selamat Datang dalam Adminstrasi Warung Suka Mundur
============================================================
        Silahkan Masukkan Nickname dan Password anda
============================================================
        """)
    Nickname = str(input("Nickname : "))
    Pass = input("Password : ")
    if Nickname == Username and Pass == Pass1: 
            print("\n")
            main_menu()
    elif Nickname == Pegawai and Pass == Pass2:
        os.system("cls")
        print("="*60)
        print("Selamat datang dalam Program Kasir Warung Suka Mundur")
        kasir()
        yes = True
        while yes == True:
            berhenti = str(input("Kembali ke menu kasir? [Y/N] : "))
            if berhenti == "Y" or berhenti == "yes" or berhenti == "y":
                kasir()
                yes = True
            elif berhenti == "N" or berhenti == "No" or berhenti == "n":
                print("Terima Kasih Telah Menggunakan Program Kasir")
                break
    else: 
        print("""
    ================================================================
    |NickName atau Password yang anda masukkan salah Harap coba lagi|  
    ================================================================
        """)