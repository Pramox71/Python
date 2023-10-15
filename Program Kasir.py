def menu1():
    a = int(input("Pilih Pesanan Makanan: "))
    if a == 1:
        print("Nasi Goreng Rp. 12000")
        a = 12000
    elif a == 2:
        print("Ayam Lalapan Rp. 15000")
        a = 15000
    elif a == 3:
        print("Mie Goreng Rp. 12000")
        a = 12000
    elif a == 4:
        print("Ayam Geprek Rp. 10000")
        a = 10000
    else:
        print("Anda Salah Memasukkan Menu, Silahkan Input Menu Kembali!")
        menu1()
    b = int(input("Berapa Porsi Makanan Yang Dipesan: "))
    harga1 = a*b
    print("Total Makanan: Rp.", harga1)
    print("---------------------------------------")
    def menu2():
        b = int(input("Pilih Pesanan Minuman: "))
        if b == 1:
            print("Teh Rp. 3000")
            b = 3000
        elif b == 2:
            print("Jeruk Rp. 3000")
            b = 3000
        elif b == 3:
            print("Air Mineral Rp. 5000")
            b = 5000
        elif b == 4:
            print("Kopi Rp. 4000")
            b = 4000
        else:
            print("Anda Salah Memasukkan Menu, Silahkan Input Menu Kembali!")
            menu2()
        c = int(input("Berapa Makanan Yang Dipesan: "))
        harga2 = b*c
        print("Total Minuman: Rp.%i" %harga2)
        total = harga1 + harga2
        print("---------------------------------------") 
        print("Total: Rp.%i" %total)
        print ("Berikut Nama-Nama Hari saat Pembelian")
        print("1. Minggu\n2. Senin\n3. Selasa\n4. Rabu\n5. Kamis\n6. Ju'mat\n7. Sabtu\n8. Hari Besar")
        diskon = str(input("Masukkan Hari saat pembelian : "))
        if diskon == "1" or diskon =="WeekEnd":
            total = total * 90/100
            print("Selamat Anda Mendapatkan Potongan Harga Sebesar 10%!")
            print("Total Yang Harus Dibayar: Rp.%i" %total)
        elif diskon == "8" or diskon == "Hari Besar":
            total = total * 75/100
            print("Selamat Anda Mendapatkan Potongan Harga Sebesar 25%!")
            print("Total Yang Harus Dibayar: Rp.%i" %total)
        else: 
            print("Hari ini adalah hari biasa")
            print("Mohon maaf tidak ada diskon hari ini")
            print("Total Yang Harus Dibayar: Rp.%i" %total)
        def bayar():
            x = int(input("Nominal Pembayaran: Rp"))
            kembalian = x - total
            if kembalian >= 0:
                print("Kembalian: Rp%i" %kembalian)
            else:
                print("Uang Untuk Pembayaran Kurang!")
                bayar()
        bayar()
    menu2()
print("Selamat Datang di Program Kasir Pintar!")
print("---------------------------------------")
menu_makanan = ["Daftar Makanan         Daftar Minuman","1. Nasi Goreng         1. Teh Hangat/Dingin", "2. Ayam Lalapan        2. Jeruk Hangat/Dingin", "3. Mie Goreng          3. Air Mineral", "4. Ayam Geprek         4. Kopi"]
for i in menu_makanan:
    print(i)
print("---------------------------------------")
menu1()