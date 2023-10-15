import os
import time

def cls():
    os.system("cls")
def daftar_gaji(x, y, z, bonus1, bonus2, bonus3, Gaji_Pokok, Nama, lvl):
    Total = x + y + z
    bonus = bonus1 + bonus2 + bonus3
    Total_Gaji = bonus1 + bonus2 + bonus3 + Gaji_Pokok
    print(f"""
Karyawan : {Nama}
Level    : {lvl}
>================================================<
<               Hasil Kerja Karyawan             >
>------------------------------------------------<
|Coklat         |Banyak :\t{x} \tBonus : {bonus1}                 
|Strawberry     |Banyak :\t{y} \tBonus : {bonus2}                 
|Kacang         |Banyak :\t{z} \tBonus : {bonus3}
<------------------------------------------------>   
|Total Permen   |        \t{Total} \tBonus : {bonus}
|Total Gaji Anda|\t\t\tRp. {Total_Gaji}
>================================================<
""")
def lvl_A(Gaji_Pokok, nama, lvl):
    while True:    
        print('''
-----------------------
Varian Rasa Coklat
-----------------------''')
        while True:    
            try:    
                x = int(input("Masukkan Jumlah Coklat Yang Dibungkus : "))
                if x < 0:
                    continue
                break
            except ValueError:
                print("Input Salah")
        if x >= 3000 and x <= 6000:
            sisa1 = 6000 - x
            if 5001 <= x <= 6000:
                bonus1 = Gaji_Pokok * 0.35
            elif 4000 <= x:
                bonus1 = Gaji_Pokok * 0.30
            elif 3000 <= x:
                bonus1 = Gaji_Pokok * 0.25
            else:
                bonus1 = 0
        else:
            sisa1 = 6000
            bonus1 = 0
        print('''
-----------------------
Varian Rasa Strawberry
-----------------------''')
        while True:    
            try:    
                y = int(input("Masukkan Jumlah Strawberry Yang Dibungkus : "))
                if y < 0:
                    continue
                break
            except ValueError:
                print("Input Salah")
        sisa2 = sisa1 - y
        if sisa2 >= 3000:
            if 5001 <= y <= 6000:
                bonus2 = Gaji_Pokok * 0.40
            elif 4000 <= y:
                bonus2 = Gaji_Pokok * 0.30
            elif 3000 <= y:
                bonus2 = Gaji_Pokok * 0.15
            else:
                bonus2 = 0
        else:
            sisa2 = sisa1
            bonus2 = 0
        print('''
-----------------------
Varian Rasa Kacang
-----------------------''')
        while True:    
            try:    
                z = int(input("Masukkan Jumlah Kacang Yang Dibungkus : "))
                print("===============================================")
                if z < 0:
                    continue
                break
            except ValueError:
                print("Input Salah")
        sisa3 = sisa2  - z
        if sisa3 >= 3000:
            if 5001 <= z <= 6000:
                bonus3 = Gaji_Pokok * 0.40
            elif 4000 <= z:
                bonus3 = Gaji_Pokok * 0.30
            elif 3000 <= z:
                bonus3 = Gaji_Pokok * 0.15
            else:
                bonus3 = 0
        else:
            sisa3 = sisa2
            bonus3 = 0
        time.sleep(3)
        cls()
        while True:
            while True:
                print(f"""
-------------------------------------
Berikut Banyak Permen Yang Dibungkus
-------------------------------------
Coklat\t\t:\t{x}
Strawberry\t:\t{y}
Kacang\t\t:\t{z}
-------------------------------------
""")
                try:
                    Ask = str(input("Apakah data Diatas Telah Benar? \n [Yes/No] \n Jawab : ")).upper()
                    break
                except:
                    print("Tolong Jawab Dengan Benar...")
                    continue
            if Ask == "Y" or Ask == "YES":
                daftar_gaji(x, y, z, bonus1, bonus2, bonus3, Gaji_Pokok, nama, lvl)
                break
            elif Ask == "N" or Ask == "NO":
                print("Silahkan Masukkan Ulang data dengan Tepat...")
                break
            else:
                print("Pilihan Yang Anda Masukkan Salah!")
        if  Ask == "N" or Ask == "NO":
            continue
        else:
            print("""
=============================================
    Terima Kasih Telah Bekerja Untuk Kami
        Tetap Semangat dan Berusaha
         Menjadi Karyawan terbaik
=============================================
""")
            input("Tekan Enter Untuk Kembali...")
            break
def lvl_B(Gaji_Pokok, nama, lvl):
    while True:    
        print('''
-----------------------
Varian Rasa Coklat
-----------------------''')
        while True:    
            try:    
                x = int(input("Masukkan Jumlah Coklat Yang Dibungkus : "))
                if x < 0:
                    continue
                break
            except ValueError:
                print("Input Salah")
        if x >= 3000 and x <= 6000:
            sisa1 = 6000 - x
            if 5001 <= x <= 6000:
                bonus1 = Gaji_Pokok * 0.25
            elif 4000 <= x:
                bonus1 = Gaji_Pokok * 0.20
            elif 3000 <= x:
                bonus1 = Gaji_Pokok * 0.15
            else:
                bonus1 = 0
        else:
            sisa1 = 6000
            bonus1 = 0
        print('''
-----------------------
Varian Rasa Strawberry
-----------------------''')
        while True:    
            try:    
                y = int(input("Masukkan Jumlah Strawberry Yang Dibungkus : "))
                if y < 0:
                    continue
                break
            except ValueError:
                print("Input Salah")
        sisa2 = sisa1 - y
        if sisa2 >= 3000:
            if 5001 <= y <= 6000:
                bonus2 = Gaji_Pokok * 0.30
            elif 4000 <= y:
                bonus2 = Gaji_Pokok * 0.20
            elif 3000 <= y:
                bonus2 = Gaji_Pokok * 0.07
            else:
                bonus2 = 0
        else:
            sisa2 = sisa1
            bonus2 = 0
        print('''
-----------------------
Varian Rasa Kacang
-----------------------''')
        while True:    
            try:    
                z = int(input("Masukkan Jumlah Kacang Yang Dibungkus : "))
                print("===============================================")
                if z < 0:
                    continue
                break
            except ValueError:
                print("Input Salah")
        sisa3 = sisa2  - z
        if sisa3 >= 3000:
            if 5001 <= z <= 6000:
                bonus3 = Gaji_Pokok * 0.30
            elif 4000 <= z:
                bonus3 = Gaji_Pokok * 0.20
            elif 3000 <= z:
                bonus3 = Gaji_Pokok * 0.07
            else:
                bonus3 = 0
        else:
            sisa3 = sisa2
            bonus3 = 0
        time.sleep(3)
        cls()
        while True:
            while True:
                print(f"""
-------------------------------------
Berikut Banyak Permen Yang Dibungkus
-------------------------------------
Coklat\t\t:\t{x}
Strawberry\t:\t{y}
Kacang\t\t:\t{z}
-------------------------------------
""")
                try:
                    Ask = str(input("Apakah data Diatas Telah Benar? \n [Yes/No] \n Jawab : ")).upper()
                    break
                except:
                    print("Tolong Jawab Dengan Benar...")
                    continue
            if Ask == "Y" or Ask == "YES":
                daftar_gaji(x, y, z, bonus1, bonus2, bonus3, Gaji_Pokok, nama, lvl)
                break
            elif Ask == "N" or Ask == "NO":
                print("Silahkan Masukkan Ulang data dengan Tepat...")
                break
            else:
                print("Pilihan Yang Anda Masukkan Salah!")
        if  Ask == "N" or Ask == "NO":
            continue
        else:
            print("""
=============================================
    Terima Kasih Telah Bekerja Untuk Kami
        Tetap Semangat dan Berusaha
         Menjadi Karyawan terbaik
=============================================
""")
            input("Tekan Enter Untuk Kembali...")
            break
def lvl_C(Gaji_Pokok, nama, lvl):
    while True:    
        print('''
-----------------------
Varian Rasa Coklat
-----------------------''')
        while True:    
            try:    
                x = int(input("Masukkan Jumlah Coklat Yang Dibungkus : "))
                if x < 0:
                    continue
                break
            except ValueError:
                print("Input Salah")
        if x >= 3000 and x <= 6000:
            sisa1 = 6000 - x
            if 5001 <= x <= 6000:
                bonus1 = Gaji_Pokok * 0.15
            elif 4000 <= x:
                bonus1 = Gaji_Pokok * 0.10
            elif 3000 <= x:
                bonus1 = Gaji_Pokok * 0.05
            else:
                bonus1 = 0
        else:
            sisa1 = 6000
            bonus1 = 0
        print('''
-----------------------
Varian Rasa Strawberry
-----------------------''')
        while True:    
            try:    
                y = int(input("Masukkan Jumlah Strawberry Yang Dibungkus : "))
                if y < 0:
                    continue
                break
            except ValueError:
                print("Input Salah")
        sisa2 = sisa1 - y
        if sisa2 >= 3000:
            if 5001 <= y <= 6000:
                bonus2 = Gaji_Pokok * 0.20
            elif 4000 <= y:
                bonus2 = Gaji_Pokok * 0.10
            elif 3000 <= y:
                bonus2 = Gaji_Pokok * 0.05
            else:
                bonus2 = 0
        else:
            sisa2 = sisa1
            bonus2 = 0
        print('''
-----------------------
Varian Rasa Kacang
-----------------------''')
        while True:    
            try:    
                z = int(input("Masukkan Jumlah Kacang Yang Dibungkus : "))
                print("===============================================")
                if z < 0:
                    continue
                break
            except ValueError:
                print("Input Salah")
        sisa3 = sisa2  - z
        if sisa3 >= 3000:
            if 5001 <= z <= 6000:
                bonus3 = Gaji_Pokok * 0.20
            elif 4000 <= z:
                bonus3 = Gaji_Pokok * 0.10
            elif 3000 <= z:
                bonus3 = Gaji_Pokok * 0.05
            else:
                bonus3 = 0
        else:
            sisa3 = sisa2
            bonus3 = 0
        time.sleep(3)
        cls()
        while True:
            while True:
                print(f"""
-------------------------------------
Berikut Banyak Permen Yang Dibungkus
-------------------------------------
Coklat\t\t:\t{x}
Strawberry\t:\t{y}
Kacang\t\t:\t{z}
-------------------------------------
""")
                try:
                    Ask = str(input("Apakah data Diatas Telah Benar? \n [Yes/No] \n Jawab : ")).upper()
                    break
                except:
                    print("Tolong Jawab Dengan Benar...")
                    continue
            if Ask == "Y" or Ask == "YES":
                daftar_gaji(x, y, z, bonus1, bonus2, bonus3, Gaji_Pokok, nama, lvl)
                break
            elif Ask == "N" or Ask == "NO":
                print("Silahkan Masukkan Ulang data dengan Tepat...")
                break
            else:
                print("Pilihan Yang Anda Masukkan Salah!")
        if  Ask == "N" or Ask == "NO":
            continue
        else:
            print("""
=============================================
    Terima Kasih Telah Bekerja Untuk Kami
        Tetap Semangat dan Berusaha
         Menjadi Karyawan terbaik
=============================================
""")
            input("Tekan Enter Untuk Kembali...")
            break
while True:
    cls()
    print("""
===============================================
    Selamat Datang di PT. Permen Suka Pelit
            Penghitung Gaji Karyawan
===============================================

    [1] Hitung Gaji Anda 
    [2] Keluar dari Program
    
===============================================
""")
    pilihan = str(input("Masukkan Pilihan Anda : ")).title()
    if pilihan == "1" or pilihan == "Hitung Gaji Anda" or pilihan == "Hitung Gaji":
        time.sleep(1)
        cls()
        while True:    
            print("""
===============================================
            Menghitung Gaji Karyawan
===============================================""")
            nama = str(input("Masukkan Nama Karyawan : ")).upper()
            print("Level Karyawan PT. Permen Suka Pelit\nA\nB\nC")
            level = str(input("Masukkan Level Karyawan : ")).upper()
            if level == "A":
                time.sleep(3)
                cls()
                print(f"""
===============================================
Menghitung Gaji Karyawan Level {level}""")
                Gaji_Pokok = 7000
                lvl_A(Gaji_Pokok, nama, level)
                break
            elif level == "B":
                time.sleep(3)
                cls()
                print(f"""
===============================================
Menghitung Gaji Karyawan Level {level}""")
                Gaji_Pokok = 5000
                lvl_B(Gaji_Pokok, nama, level)
                break
            elif level == "C":
                time.sleep(3)
                cls()
                print(f"""
===============================================
Menghitung Gaji Karyawan Level {level}""")
                Gaji_Pokok = 5000
                lvl_C(Gaji_Pokok, nama, level)
                break
            else:
                print()
                print("Level Yang Anda Masukkan Salah")
                time.sleep(2)
                cls()
                continue
    elif pilihan == "2" or pilihan == "Keluar Dari Program" or pilihan == "Keluar":
        print("Terima Kasih Telah Menggunakan Program Kami")
        break