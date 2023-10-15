import os
import time
# print("LOADING.......0%")
# time.sleep(4)
# print("LOADING.......25%")
# time.sleep(6)
# print("LOADING.......75%")
# time.sleep(4)
# print("LOADING COMPLETE!!!")
# time.sleep(1)
# os.system("cls")

Username = ["Admin", "User"]
Password =["12345", "54321"]
sebagai = ["Admin", "User"]
# Warna Program
class color:
   b = '\033[94m'
   g = '\033[92m'
   y = '\033[93m'
   r = '\033[91m'
   u = '\033[95m'
   e = '\033[0m'
   bold = '\033[1m'

# Barang_Barang
Album = [
    ["Lalisa (Lisa)", 365000, 5, "album"],
    ["Love Shoot (EXO)", 305000, 5, "album"],
    ["-R- (Rose)", 490000, 5, "album"],
    ["Wings (BTS)", 2700000, 5, "album"],
    ["Be (BTS)", 363000, 5, "album"],
    ["Reload (NCT)", 286000, 5, "album"]
    ]

Photocards= [
    ["Chen EXO", 60000, 10, "photocards"],
    ["Xiumin EXO", 55000, 10, "photocards"],
    ["Taehyung BTS", 250000, 10, "photocards"],
    ["Jungkook BTS", 291000, 10, "photocards"]
    ]

Light_Stick = [
    ["Light Stick EXO", 665000, 15, "light stick"],
    ["Light Stick BTS", 450000, 15, "light stick"],
    ["Light Stick BB", 340000, 15, "light stick"],
    ["Light Stick NCT", 645000, 15, "light stick"]
    ]

poster = [
    ["Poster EXO", 22000, 20, "poster"],
    ["Poster BTS", 22000, 20, "poster"],
    ["Poster Lisa", 20000, 20, "poster"],
    ["Poster NCT", 22000, 20, "poster"]
    ]

Kaos = [
    ["Kaos EXO (Putih)", 31000, 25, "kaos"],
    ["Kaos EXO (Hitam)", 33000, 25, "kaos"],
    ["Kaos BTS (Putih)", 28000, 25, "kaos"],
    ["Kaos BTS (Hitam)", 30000, 25, "kaos"]
    ]

pesanan = []

total_beli = []
# Menu Admin
def daftar_barang():
    time.sleep(1)
    os.system("cls")
    print(color.b + "||===========================================||")
    print("||            Daftar Stock Barang            ||")
    print("||===========================================||")
    print("||    1. Album                               ||")
    print("||    2. Photocards                          ||")
    print("||    3. Light_Stick                         ||")
    print("||    4. Poster                              ||")
    print("||    5. Kaos                                ||")
    print("||===========================================||" + color.e)
    lihat_data = input(color.g + "masukan data yang ingin di lihat :" + color.e)
    print(color.bold + "Nama\t\t\t\t|Harga\t\t\t|Stock\t\t\t|Jenis\t\t\t")
    if (lihat_data.lower() == "album" or lihat_data == "1"):
        Album.sort()
        for i in range(len(Album)):
            for j in range(len(Album[i])):
                print(Album[i][j], end= "\t\t\t")
            print()
    elif (lihat_data.lower() == "photocards" or lihat_data == "2"):
        Photocards.sort()
        for i in range(len(Photocards)):
            for j in range(len(Photocards[i])):
                print(Photocards[i][j], end = "\t\t\t ")
            print()
    elif (lihat_data.lower() == "light stick" or lihat_data == "3"):
        Light_Stick.sort()
        for i in range(len(Light_Stick)):
            for j in range(len(Light_Stick[i])):
                print(Light_Stick[i][j], end = "\t\t\t ")
            print()
    elif (lihat_data.lower() == "poster" or lihat_data == "4"):
        poster.sort()
        for i in range(len(poster)):
            for j in range(len(poster[i])):
                print(poster[i][j], end = "\t\t\t ")
            print()
    elif (lihat_data.lower() == "kaos" or lihat_data == "5"):
        Kaos.sort()
        for i in range(len(Kaos)):
            for j in range(len(Kaos[i])):
                print(Kaos[i][j], end = "\t\t\t ")
            print()
    else:
        print(color.r + "saat ini hanya data diatas yang tersedia!" + color.e)
    print()
def tambah_stock(x,y):
    while True: 
        NS_tam  = input(color. u + "Nama : ")
        try:
            HS_tam = int(input("Harga : "))
            JuS_tam = int(input("Jumlah : "))
            JeS_tam = str(input("Jenis : " + color.e))
        except:
            print("Error")
            continue
        if 0 <= JuS_tam:
            if HS_tam >= 0:
                if  x >= JuS_tam:
                    Nama = y
                    tambah = [NS_tam.title(), HS_tam, JuS_tam, JeS_tam.lower()]
                    print(color.y + "berhasil menambahkan!")
                    print(color.y + "data {} berhasil diperbarui".format(Nama) + color.e)
                    return tambah
                else:
                    print("Stock Yang Anda Masukkan melibihi Kapasitas")
                    continue
            else :
                print("Data Yang Anda Masukkan Kurang tepat")
                continue
        else:
            print("Data Yang Anda Masukkan Kurang tepat")
            continue
def menu_admin():
    while True:
        print(color.b + "||===========================================||")
        print("||               MENU ADMIN                  ||")
        print("||===========================================||")       
        print("||    1. Tambahkan stock                     ||")
        print("||    2. Lihat Stock                         ||")
        print("||    3. Perbarui jumlah stock               ||")
        print("||    4. Hapus stock                         ||")
        print("||    5. Logout                              ||")
        print("||===========================================||" + color.e)

        pilihan1 = input(color.g + "Masukkan pilihan : " + color.e)
        if pilihan1.lower() == "tambahkan stock" or pilihan1 == "1":
            print(color.b + "||===========================================||")
            print("||           Tambah Barang Baru              ||")
            print("||===========================================||")
            print("||    1. Album                               ||")
            print("||    2. Photocards                          ||")
            print("||    3. Light Stick                         ||")
            print("||    4. Poster                              ||")
            print("||    5. Kaos                                ||")
            print("||===========================================||" + color.e)
            data_toko_b = input(color.g + "masukan data yang ingin diperbarui atau di tambahkan :" + color.e)
            print(color.bold + "Nama\t\t\t\t|Harga\t\t\t|Stock\t\t\t|Jenis\t\t\t")
            if data_toko_b == "1" or data_toko_b.lower() == "album":
                for i in range(len(Album)):
                    for j in range(len(Album[i])):
                        print(Album[i][j], end= "\t\t\t")
                    print()
                x = 5
                y = "album"
                while True: 
                    Tanya = str(input("Apakah Anda Yakin Ingin Menambah Data? [Y/N] : "))
                    if Tanya.lower() == "y" or Tanya.lower()=="yes":
                        Album.append(tambah_stock(x, y))
                        break
                    elif Tanya.lower()=="n" or Tanya.lower()=="no":
                        break
                    else:
                        print("Error")
                        continue
                time.sleep(2)
                os.system("cls")
            elif data_toko_b == "2" or data_toko_b.lower() == "photocards":
                for i in range(len(Photocards)):
                    for j in range(len(Photocards[i])):
                        print(Photocards[i][j], end = "\t\t\t ")
                    print()        
                x = 10
                y = "photocards"
                while True: 
                    Tanya = str(input("Apakah Anda Yakin Ingin Menambah Data? [Y/N] : "))
                    if Tanya.lower() == "y" or Tanya.lower()=="yes":
                        Photocards.append(tambah_stock(x, y))
                        break
                    elif Tanya.lower()=="n" or Tanya.lower()=="no":
                        print(color.e + color.y + "||===========================================||")
                        print("||          Kembali ke menu ADMIN           ||")
                        print("||===========================================||" + color.e)
                        break
                    else:
                        print("Error")
                        continue
                time.sleep(2)
                os.system("cls")
            elif data_toko_b == "3" or data_toko_b.lower() == "light stick":
                for i in range(len(Light_Stick)):
                    for j in range(len(Light_Stick[i])):
                        print(Light_Stick[i][j], end = "\t\t\t ")
                    print()
                x = 15
                y = "light stick"
                while True: 
                    Tanya = str(input("Apakah Anda Yakin Ingin Menambah Data? [Y/N] : "))
                    if Tanya.lower() == "y" or Tanya.lower()=="yes":
                        Light_Stick.append(tambah_stock(x, y))
                        break
                    elif Tanya.lower()=="n" or Tanya.lower()=="no":
                        print(color.e + color.y + "||===========================================||")
                        print("||          Kembali ke menu ADMIN           ||")
                        print("||===========================================||" + color.e)
                        break
                    else:
                        print("Error")
                        continue
                time.sleep(2)
                os.system("cls")
            elif data_toko_b == "4" or data_toko_b.lower() == "poster":
                for i in range(len(poster)):
                    for j in range(len(poster[i])):
                        print(poster[i][j], end = "\t\t\t ")
                    print()
                x = 20
                y = "poster"
                while True: 
                    Tanya = str(input("Apakah Anda Yakin Ingin Menambah Data? [Y/N] : "))
                    if Tanya.lower() == "y" or Tanya.lower()=="yes":
                        poster.append(tambah_stock(x, y))
                        break
                    elif Tanya.lower()=="n" or Tanya.lower()=="no":
                        print(color.e + color.y + "||===========================================||")
                        print("||          Kembali ke menu ADMIN           ||")
                        print("||===========================================||" + color.e)
                        break
                    else:
                        print("Error")
                        continue
                time.sleep(2)
                os.system("cls")
            elif data_toko_b == "5" or data_toko_b.lower() == "kaos":
                for i in range(len(Kaos)):
                    for j in range(len(Kaos[i])):
                        print(Kaos[i][j], end = "\t\t\t ")
                    print()
                x = 25
                y = "kaos"
                while True: 
                    Tanya = str(input("Apakah Anda Yakin Ingin Menambah Data? [Y/N] : "))
                    if Tanya.lower() == "y" or Tanya.lower()=="yes":
                        Kaos.append(tambah_stock(x, y))
                        break
                    elif Tanya.lower()=="n" or Tanya.lower()=="no":
                        print(color.e + color.y + "||===========================================||")
                        print("||          Kembali ke menu ADMIN           ||")
                        print("||===========================================||" + color.e)
                        break
                    else:
                        print("Error")
                        continue
                time.sleep(2)
                os.system("cls")
            else:
                print(color.r + "saat ini hanya data diatas yang tersedia" + color.e)
                time.sleep(2)
                os.system("cls")
        elif (pilihan1 == "2" or pilihan1.lower() == "lihat stock"):
            daftar_barang()
            while True:
                lihat_lagi = str(input("Apakah anda ingin melihat menu lainnya? [Y/N] : "))
                if lihat_lagi.lower() == "yes" or lihat_lagi.lower() == "y":
                    print()
                    print("=====================")
                    print("Harap Tunggu Sebentar")
                    print("=====================")
                    time.sleep(5)
                    os.system("cls")
                    daftar_barang()
                    continue
                elif lihat_lagi.lower() == "no" or lihat_lagi.lower() == "n":
                    print(color.e + color.y + "||===========================================||")
                    print("||          Kembali ke menu ADMIN           ||")
                    print("||===========================================||" + color.e)
                    time.sleep(2)
                    os.system("cls")
                    break
                else:
                    print()
                    print("======================================")
                    print("Pilihan yang anda masukkan tidak valid")
                    print("======================================")
                    time.sleep(3)
                    os.system("cls")
                    continue
        elif (pilihan1 == "3" or pilihan1.lower == "update stock baru"):
            print(color.b + "||===========================================||")
            print("||            UPDATE STOCK BARANG            ||")
            print("||===========================================||")
            print("||    1. Album                               ||")
            print("||    2. Photocards                          ||")
            print("||    3. Light Stick                         ||")
            print("||    4. Poster                              ||")
            print("||    5. Kaos                                ||")
            print("||===========================================||" + color.e)
            print("\n Tekan [Enter] Untuk Batal")
            tambah_jumlah = input(color.g + "masukan data yang ingin di tambah jumlah stocknya :" + color.e)
            print(color.bold + "Nama\t\t\t\t|Jumlah\t\t\t|Harga\t\t\t|Jenis\t\t\t")
            if (tambah_jumlah.lower() == "album" or tambah_jumlah == "1"):
                for i in range(len(Album)):
                    for j in range(len(Album[i])):
                        print(Album[i][j], end = "\t\t\t ")
                    print()
                cek_barang1 = len(Album) - 1
                N_barang1 = input(color.e + color.g + "Masukkan judul Album : ")
                while (cek_barang1 >= 0):
                    if (N_barang1 == Album[cek_barang1][0]):
                        break
                    else:
                        cek_barang1 -= 1
                if (cek_barang1 >= 0):
                    while True:
                        try:
                            PJ_barang = int(input("Masukkan jumlah Album: " + color.e))
                        except:
                            print("Error")
                            continue
                        if 0 < PJ_barang <= 5:
                            Album[cek_barang1][2] = PJ_barang
                            break
                        else:
                            print("Maaf Stock tidak sesuai kapasitas"+ color.e)
                            continue
                    print(color.y + "data jumlah Album berhasil di perbarui" + color.e)
                else:
                    print(color.r + "Maaf nama Album yang dimasukkan tidak ada" + color.e)
            elif (tambah_jumlah.lower() == "photocards" or tambah_jumlah == "2"):
                for i in range(len(Photocards)):
                    for j in range(len(Photocards[i])):
                        print(Photocards[i][j], end = "\t\t\t ")
                    print()
                cek_barang1 = len(Photocards) - 1
                N_barang1 = input(color.e + color.g + "Masukkan Nama Photocards : ")
                while (cek_barang1 >= 0):
                    if (N_barang1 == Photocards[cek_barang1][0]):
                        break
                    else:
                        cek_barang1 -= 1
                if (cek_barang1 >= 0):
                    while True:
                        try:
                            PJ_barang = int(input("Masukkan jumlah Photocards: " + color.e))
                        except:
                            print("Error")
                            continue
                        if 0 < PJ_barang <= 10:
                            Photocards[cek_barang1][2] = PJ_barang
                            break
                        else:
                            print("Maaf Stock tidak sesuai kapasitas" + color.e)
                            continue
                    print(color.y + "data jumlah Photocards berhasil di perbarui" + color.e)
                else:
                    print(color.r + "Maaf nama Photocards yang dimasukkan tidak ada" + color.e)
            elif (tambah_jumlah.lower() == "light stick" or tambah_jumlah == "3"):
                for i in range(len(Light_Stick)):
                    for j in range(len(Light_Stick[i])):
                        print(Light_Stick[i][j], end = "\t\t\t ")
                    print()
                cek_barang1 = len(Light_Stick) - 1
                N_barang1 = input(color.e + color.g + "Masukkan Nama Light Stick : ")
                while (cek_barang1 >= 0):
                    if (N_barang1 == Light_Stick[cek_barang1][0]):
                        break
                    else:
                        cek_barang1 -= 1
                if (cek_barang1 >= 0):
                    while True:
                        try:
                            PJ_barang = int(input("Masukkan jumlah Light Stick : " + color.e))
                        except:
                            print("Error")
                            continue
                        if 0 < PJ_barang <= 15:
                            Light_Stick[cek_barang1][2] = PJ_barang
                            break
                        else:
                            print("Maaf Stock tidak sesuai kapasitas" + color.e)
                            continue
                    print(color.y + "data jumlah Light Stick berhasil di perbarui" + color.e)
                else:
                    print(color.r + "Maaf nama Light Stick yang dimasukkan tidak ada" + color.e)
            elif (tambah_jumlah.lower() == "poster" or tambah_jumlah == "4"):
                for i in range(len(poster)):
                    for j in range(len(poster[i])):
                        print(poster[i][j], end = "\t\t\t ")
                    print()
                cek_barang1 = len(poster) - 1
                N_barang1 = input(color.e + color.g + "Masukkan Nama poster : ")
                while (cek_barang1 >= 0):
                    if (N_barang1 == poster[cek_barang1][0]):
                        break
                    else:
                        cek_barang1 -= 1
                if (cek_barang1 >= 0):
                    while True:
                        try:
                            PJ_barang = int(input("Masukkan jumlah poster : " + color.e))
                        except:
                            print("Error")
                            continue
                        if 0 < PJ_barang <= 20:
                            poster[cek_barang1][2] = PJ_barang
                            break
                        else:
                            print("Maaf Stock tidak sesuai kapasitas" + color.e)
                            continue
                    print(color.y + "data jumlah poster berhasil di perbarui" + color.e)
                else:
                    print(color.r + "Maaf nama poster yang dimasukkan tidak ada" + color.e)
            elif (tambah_jumlah.lower() == "kaos" or tambah_jumlah == "5"):
                for i in range(len(Kaos)):
                    for j in range(len(Kaos[i])):
                        print(Kaos[i][j], end = "\t\t\t ")
                    print()
                cek_barang1 = len(Kaos) - 1
                N_barang1 = input(color.e + color.g + "Masukkan Nama Kaos : ")
                while (cek_barang1 >= 0):
                    if (N_barang1 == Kaos[cek_barang1][0]):
                        break
                    else:
                        cek_barang1 -= 1
                if (cek_barang1 >= 0):
                    while True:
                        try:
                            PJ_barang = int(input("Masukkan jumlah Kaos : " + color.e))
                        except:
                            print("Error")
                            continue
                        if 0 < PJ_barang <= 25:
                            Kaos[cek_barang1][2] = PJ_barang
                            break
                        else:
                            print("Maaf Stock tidak sesuai kapasitas" + color.e)
                            continue
                    print(color.y + "data jumlah Kaos berhasil di perbarui" + color.e)
                else:
                    print(color.r + "Maaf nama Kaos yang dimasukkan tidak ada" + color.e)
            else:
                print(color.r + "data salah!" + color.e)
            print(color.e + color.y + "||===========================================||")
            print("||          Kembali ke menu Admin            ||")
            print("||===========================================||" + color.e)
            time.sleep(3)
            os.system("cls")
        elif (pilihan1 == "4" or pilihan1.lower == "hapus stock"):
            print(color.b + "||===========================================||")
            print("||            DELETE STOCK BARANG            ||")
            print("||===========================================||")
            print("||    1. Album                               ||")
            print("||    2. Photocards                          ||")
            print("||    3. Light Stick                         ||")
            print("||    4. Poster                              ||")
            print("||    5. Kaos                                ||")
            print("||===========================================||" + color.e)
            hapus_data = input(color.g + "masukan nama data yang ingin di hapus :" + color.e)
            print(color.bold + "Nama\t\t\t|Jumlah\t\t\t|Harga\t\t\t|Jenis\t\t\t")
            if (hapus_data.lower() == "album" or hapus_data == "1"):
                for i in range(len(Album)):
                    for j in range(len(Album[i])):
                        print(Album[i][j], end = "\t\t\t ")
                    print()
                a1 = 3
                cek_barang2 = len(Album) - 1
                N_barang2 = input(color.e + color.g + "Masukkan salah satu judul album yang ingin di hapus: " + color.e)
                while cek_barang2 >= 0:
                    if (N_barang2 == Album[cek_barang2][0]):
                        break
                    else:
                        cek_barang2 -= 1
                if (cek_barang2 >= 0):
                    while a1 >= 0:
                        Album[cek_barang2].pop(a1)
                        a1 -= 1
                    Album.sort()
                    del Album[0]
                    print(color.y + "berhasil menghapus Data Album" + color.e)
                else:
                    print(color.r + "Maaf nama Album yang anda masukkan tidak ada" + color.e)
            elif (hapus_data.lower() == "photocards" or hapus_data == "2"):
                for i in range(len(Photocards)):
                    for j in range(len(Photocards[i])):
                        print(Photocards[i][j], end = "\t\t\t ")
                    print()
                a1 = 3
                cek_barang2 = len(Photocards) - 1
                N_barang2 = input(color.e + color.g + "Masukkan salah satu Photocards yang ingin di hapus: " + color.e)
                while cek_barang2 >= 0:
                    if (N_barang2 == Photocards[cek_barang2][0]):
                        break
                    else:
                        cek_barang2 -= 1
                if (cek_barang2 >= 0):
                    while a1 >= 0:
                        Photocards[cek_barang2].pop(a1)
                        a1 -= 1
                    Photocards.sort()
                    del Photocards[0]
                    print(color.y + "berhasil menghapus Data Photocards" + color.e)
                else:
                    print(color.r + "Maaf Photocards yang anda masukkan tidak ada" + color.e)
            elif (hapus_data.lower() == "light stick" or hapus_data == "3"):
                for i in range(len(Light_Stick)):
                    for j in range(len(Light_Stick[i])):
                        print(Light_Stick[i][j], end = "\t\t\t ")
                    print()
                a1 = 3
                cek_barang2 = len(Light_Stick) - 1
                N_barang2 = input(color.e + color.g + "Masukkan salah satu Light Stick yang ingin di hapus: " + color.e)
                while cek_barang2 >= 0:
                    if (N_barang2 == Light_Stick[cek_barang2][0]):
                        break
                    else:
                        cek_barang2 -= 1
                if (cek_barang2 >= 0):
                    while a1 >= 0:
                        Light_Stick[cek_barang2].pop(a1)
                        a1 -= 1
                    Light_Stick.sort()
                    del Light_Stick[0]
                    print(color.y + "berhasil menghapus Data Light Stick" + color.e)
                else:
                    print(color.r + "Maaf Light Stick yang anda masukkan tidak ada" + color.e)
            elif (hapus_data.lower() == "poster" or hapus_data == "4"):
                for i in range(len(poster)):
                    for j in range(len(poster[i])):
                        print(poster[i][j], end = "\t\t\t ")
                    print()
                a1 = 3
                cek_barang2 = len(poster) - 1
                N_barang2 = input(color.e + color.g + "Masukkan salah satu poster yang ingin di hapus: " + color.e)
                while cek_barang2 >= 0:
                    if (N_barang2 == poster[cek_barang2][0]):
                        break
                    else:
                        cek_barang2 -= 1
                if (cek_barang2 >= 0):
                    while a1 >= 0:
                        poster[cek_barang2].pop(a1)
                        a1 -= 1
                    poster.sort()
                    del poster[0]
                    print(color.y + "berhasil menghapus Data poster" + color.e)
                else:
                    print(color.r + "Maaf poster yang anda masukkan tidak ada" + color.e)
            elif (hapus_data.lower() == "kaos" or hapus_data == "5"):
                for i in range(len(Kaos)):
                    for j in range(len(Kaos[i])):
                        print(Kaos[i][j], end = "\t\t\t ")
                    print()
                a1 = 3
                cek_barang2 = len(Kaos) - 1
                N_barang2 = input(color.e + color.g + "Masukkan salah satu Kaos yang ingin di hapus: " + color.e)
                while cek_barang2 >= 0:
                    if (N_barang2 == Kaos[cek_barang2][0]):
                        break
                    else:
                        cek_barang2 -= 1
                if (cek_barang2 >= 0):
                    while a1 >= 0:
                        Kaos[cek_barang2].pop(a1)
                        a1 -= 1
                    Kaos.sort()
                    del Kaos[0]
                    print(color.y + "berhasil menghapus Data Kaos" + color.e)
                else:
                    print(color.r + "Maaf Kaos yang anda masukkan tidak ada" + color.e)
            else:
                print(color.r + "saat ini hanya ada data yang diatas" + color.e)
        elif (pilihan1 == "5" or pilihan1.lower == "log out"):    
            time.sleep(3)
            os.system("cls")
            print(color.e + color.y + "||===========================================||")
            print("||          Kembali ke menu Admin            ||")
            print("||===========================================||" + color.e)
            break
        else:
            print(color.e + color.y + "||===========================================||")
            print("||  Pilihan Yang Anda Masukkan Tidak Valid   ||")
            print("||===========================================||" + color.e)
            time.sleep(2)
            os.system("cls")
            continue
def menu_user():
    while True:
        print(color.b + "||===========================================||")
        print("||               MENU PELANGGAN              ||")
        print("||===========================================||")       
        print("||    1. Beli Stock                          ||")
        print("||    2. Bayar                               ||")
        print("||    3. Log out                             ||")
        print("||===========================================||" + color.e)
        pilihan2 = input(str(color.g + "Masukkan pilihan beli atau logout : " + color.e))
        if pilihan2 == "1" or pilihan2.lower() == "beli stock":
            print(color.b + "||===========================================||")
            print("||           DAFTAR STOCK BARANG             ||")
            print("||===========================================||")
            print("||    1. Album                               ||")
            print("||    2. Photocards                          ||")
            print("||    3. Light Stick                         ||")
            print("||    4. Poster                              ||")
            print("||    5. Kaos                                ||")
            print("||===========================================||" + color.e)
            yg_dijual = input(color.g + "anda mau beli apa? :" + color.e)
            if (yg_dijual == "1" or yg_dijual.lower() == "album"):
                print(color.bold + "ini adalah beberapa Album yang dijual")
                print(color.bold + "Nama\t\t\t|Harga\t\t\t|Jumlah\t\t\t|Jenis\t\t\t")
                for i in range(len(Album)):
                    for j in range(len(Album[i])):
                        print(Album[i][j], end = "\t\t\t ")
                    print()
                cek_barang3 = len(Album) - 1
                B_barang = input(color.e + color.g + "Masukkkan nama Album yang mau anda beli: " + color.e)
                while cek_barang3 >= 0:
                    if B_barang == Album[cek_barang3][0]:
                        break
                    else:
                        cek_barang3 -= 1
                if cek_barang3 >= 0 :
                    if B_barang == Album[cek_barang3][0]:
                        Jenis = Album[cek_barang3][3]
                        try:
                            JB_barang = int(input(color.g + "Masukkan jumlah barang yang dibeli: " + color.e))
                        except:
                            print("Jumlah Yang anda masukkan salah")
                            continue
                        if JB_barang <= 0:
                            print(color.e + color.r + "maaf jumlah pesanan anda tidak valid" + color.e)
                        elif JB_barang <= Album[cek_barang3][2]:
                            T_Harga = JB_barang * Album[cek_barang3][1]
                            struk = [B_barang, JB_barang, T_Harga, Jenis]
                            total_beli.append(struk)
                            pesanan.append(T_Harga)
                            total_beli.sort()
                            sisa_barang = Album[cek_barang3][2] - JB_barang
                            Album[cek_barang3][2] = sisa_barang
                            print("\n||===========================================||")
                            print("||         Produk Berhasil Di Pesan          ||")
                            print("||===========================================||")
                            time.sleep(4)
                            os.system("cls")
                        else:
                            print("Maaf kami kekurangan stock barang")
                else:
                    print("Nama barang yang anda cari belum ada dalam stock")
            elif (yg_dijual == "2" or yg_dijual.lower() == "photocards"):
                print(color.bold + "ini adalah beberapa Photocards yang dijual")
                print(color.bold + "Nama\t\t\t|Harga\t\t\t|Jumlah\t\t\t|Jenis\t\t\t")
                for i in range(len(Photocards)):
                    for j in range(len(Photocards[i])):
                        print(Photocards[i][j], end = "\t\t\t ")
                    print()
                cek_barang3 = len(Photocards) - 1
                B_barang = input(color.e + color.g + "Masukkkan nama Photocards yang mau anda beli: " + color.e)
                while cek_barang3 >= 0:
                    if B_barang == Photocards[cek_barang3][0]:
                        break
                    else:
                        cek_barang3 -= 1
                if cek_barang3 >= 0 :
                    if B_barang == Photocards[cek_barang3][0]:
                        Jenis = Photocards[cek_barang3][3]
                        try:
                            JB_barang = int(input(color.g + "Masukkan jumlah barang yang dibeli: " + color.e))
                        except:
                            print("Jumlah Yang anda masukkan salah")
                            continue
                        if JB_barang <= 0:
                            print(color.e + color.r + "maaf jumlah pesanan anda tidak valid" + color.e)
                        elif JB_barang <= Photocards[cek_barang3][2]:
                            T_Harga = JB_barang * Photocards[cek_barang3][1]
                            struk = [B_barang, JB_barang, T_Harga, Jenis]
                            total_beli.append(struk)
                            pesanan.append(T_Harga)
                            total_beli.sort()
                            sisa_barang = Photocards[cek_barang3][2] - JB_barang
                            Photocards[cek_barang3][2] = sisa_barang
                            print("\n||===========================================||")
                            print("||         Produk Berhasil Di Pesan          ||")
                            print("||===========================================||")
                            time.sleep(4)
                            os.system("cls")
                        else:
                            print("Maaf kami kekurangan stock barang")
                else:
                    print("Nama barang yang anda cari belum ada dalam stock")
            elif (yg_dijual == "3" or yg_dijual.lower() == "light stick"):
                print(color.bold + "ini adalah beberapa Light Stick yang dijual")
                print(color.bold + "Nama\t\t\t|Harga\t\t\t|Jumlah\t\t\t|Jenis\t\t\t")
                for i in range(len(Light_Stick)):
                    for j in range(len(Light_Stick[i])):
                        print(Light_Stick[i][j], end = "\t\t\t ")
                    print()
                cek_barang3 = len(Light_Stick) - 1
                B_barang = input(color.e + color.g + "Masukkkan nama Light Stick yang mau anda beli: " + color.e)
                while cek_barang3 >= 0:
                    if B_barang == Light_Stick[cek_barang3][0]:
                        break
                    else:
                        cek_barang3 -= 1
                if cek_barang3 >= 0 :
                    if B_barang == Light_Stick[cek_barang3][0]:
                        Jenis = Light_Stick[cek_barang3][3]
                        try:
                            JB_barang = int(input(color.g + "Masukkan jumlah barang yang dibeli: " + color.e))
                        except:
                            print("Jumlah Yang anda masukkan salah")
                            continue
                        if JB_barang <= 0:
                            print(color.e + color.r + "maaf jumlah pesanan anda tidak valid" + color.e)
                        elif JB_barang <= Light_Stick[cek_barang3][2]:
                            T_Harga = JB_barang * Light_Stick[cek_barang3][1]
                            struk = [B_barang, JB_barang, T_Harga, Jenis]
                            total_beli.append(struk)
                            pesanan.append(T_Harga)
                            total_beli.sort()
                            sisa_barang = Light_Stick[cek_barang3][2] - JB_barang
                            Light_Stick[cek_barang3][2] = sisa_barang
                            print("\n||===========================================||")
                            print("||         Produk Berhasil Di Pesan          ||")
                            print("||===========================================||")
                            time.sleep(4)
                            os.system("cls")
                        else:
                            print("Maaf kami kekurangan stock barang")
                else:
                    print("Nama barang yang anda cari belum ada dalam stock")
            elif (yg_dijual == "4" or yg_dijual.lower() == "poster"):
                print(color.bold + "ini adalah beberapa Poster yang dijual")
                print(color.bold + "Nama\t\t\t|Harga\t\t\t|Jumlah\t\t\t|Jenis\t\t\t")
                for i in range(len(poster)):
                    for j in range(len(poster[i])):
                        print(poster[i][j], end = "\t\t\t ")
                    print()
                cek_barang3 = len(poster) - 1
                B_barang = input(color.e + color.g + "Masukkkan nama Poster yang mau anda beli: " + color.e)
                while cek_barang3 >= 0:
                    if B_barang == poster[cek_barang3][0]:
                        break
                    else:
                        cek_barang3 -= 1
                if cek_barang3 >= 0 :
                    if B_barang == poster[cek_barang3][0]:
                        Jenis = poster[cek_barang3][3]
                        try:
                            JB_barang = int(input(color.g + "Masukkan jumlah barang yang dibeli: " + color.e))
                        except:
                            print("Jumlah Yang anda masukkan salah")
                            continue
                        if JB_barang <= 0:
                            print(color.e + color.r + "maaf jumlah pesanan anda tidak valid" + color.e)
                        elif JB_barang <= poster[cek_barang3][2]:
                            T_Harga = JB_barang * poster[cek_barang3][1]
                            struk = [B_barang, JB_barang, T_Harga, Jenis]
                            total_beli.append(struk)
                            pesanan.append(T_Harga)
                            total_beli.sort()
                            sisa_barang = poster[cek_barang3][2] - JB_barang
                            poster[cek_barang3][2] = sisa_barang
                            print("\n||===========================================||")
                            print("||         Produk Berhasil Di Pesan          ||")
                            print("||===========================================||")
                            time.sleep(4)
                            os.system("cls")
                        else:
                            print("Maaf kami kekurangan stock barang")
                else:
                    print("Nama barang yang anda cari belum ada dalam stock")
            elif (yg_dijual == "5" or yg_dijual.lower() == "kaos"):
                print(color.bold + "ini adalah beberapa Poster yang dijual")
                print(color.bold + "Nama\t\t\t|Harga\t\t\t|Jumlah\t\t\t|Jenis\t\t\t")
                for i in range(len(poster)):
                    for j in range(len(poster[i])):
                        print(poster[i][j], end = "\t\t\t ")
                    print()
                cek_barang3 = len(poster) - 1
                B_barang = input(color.e + color.g + "Masukkkan nama Poster yang mau anda beli: " + color.e)
                while cek_barang3 >= 0:
                    if B_barang == poster[cek_barang3][0]:
                        break
                    else:
                        cek_barang3 -= 1
                if cek_barang3 >= 0 :
                    if B_barang == poster[cek_barang3][0]:
                        Jenis = poster[cek_barang3][3]
                        try:
                            JB_barang = int(input(color.g + "Masukkan jumlah barang yang dibeli: " + color.e))
                        except:
                            print("Jumlah Yang anda masukkan salah")
                            continue
                        if JB_barang <= 0:
                            print(color.e + color.r + "maaf jumlah pesanan anda tidak valid" + color.e)
                        elif JB_barang <= poster[cek_barang3][2]:
                            T_Harga = JB_barang * poster[cek_barang3][1]
                            struk = [B_barang, JB_barang, T_Harga, Jenis]
                            total_beli.append(struk)
                            pesanan.append(T_Harga)
                            total_beli.sort()
                            sisa_barang = poster[cek_barang3][2] - JB_barang
                            poster[cek_barang3][2] = sisa_barang
                            print("\n||===========================================||")
                            print("||         Produk Berhasil Di Pesan          ||")
                            print("||===========================================||")
                            time.sleep(4)
                            os.system("cls")
                        else:
                            print("Maaf kami kekurangan stock barang")
                else:
                    print("Nama barang yang anda cari belum ada dalam stock")
            else:
                print("Mohon Maaf Pilihan yang anda masukkan salah")
        elif pilihan2 == "2" or pilihan2.lower() == "bayar":
            while True:
                print(color.bold + "Nama\t\t\t|Harga\t\t\t|Jumlah\t\t\t|Jenis\t\t\t")
                for i in range(len(total_beli)):
                    for j in range(len(total_beli[i])):
                        print(total_beli[i][j], end = "\t\t\t ")
                    print()
                total_pesanan = sum(pesanan)
                print("Total pesanan anda : {}" .format(total_pesanan))
                print("||===========================================||")
                print("||   1. Pesan Lagi                           ||")
                print("||   2. Bayar                                ||")
                print("||===========================================||")
                bayar1 = input(color.r + "Masukkan Pilihan anda")
                if bayar1 == "1" or bayar1.lower() == "pesan lagi":
                    print(color.e + color.y + "||===========================================||")
                    print("||        Kembali ke menu Pelanggan          ||")
                    print("||===========================================||" + color.e)
                    os.system("cls")
                    break
                elif bayar1 == "2" or bayar1.lower() == "bayar":
                    print("Total yang harus dibayar : {}" .format(total_pesanan))
                    try:
                        bayar_ok = int(input("Nominal Pembayaran : Rp."))
                    except:
                        print("ERROR")
                        continue
                    kembalian = total_pesanan - bayar_ok
                    if kembalian >= 0:
                        print("\n||===========================================||")
                        print("||         Produk Berhasil Di Bayar          ||")
                        print("||===========================================||")
                        time.sleep(1)
                        os.system("cls")
                        print(color.bold + "Nama\t\t\t|Harga\t\t\t|Jumlah\t\t\t|Jenis\t\t\t")
                        for i in range(len(total_beli)):
                            for j in range(len(total_beli[i])):
                                print(total_beli[i][j], end = "\t\t\t ")
                            print()
                        print("Total pesanan    : \t\t\t{}".format(total_pesanan))
                        print("Total Pembayaran : \t\t\t{}".format(bayar_ok))
                        print("sisa kembalian   : \t\t\t{}".format(kembalian))
                        print("\n\n\n")
                        print("Tekan [Enter] untuk kembali ke Menu Pelanggan")
                        input()
                        break
                    else:
                        print("Nominal yang anda masukkan kurang")
                        continue
                else:
                    print("Pilihan Yang anda masukkan tidak valid")
        elif pilihan2 == "3" or pilihan2.lower() == "log out":
            print(color.e + color.y + "||===========================================||")
            print("||        Kembali ke menu Login              ||")
            print("||===========================================||" + color.e)
            os.system("cls")
            break
# Menu Login
while True:
    print("""
||===========================================||
||                   LOGIN                   ||
||===========================================||
||  Silahkan Masukkan Username dan Password  ||     
""")
    login = input("Username : ")
    Pasword = input("Password : ")
    cek = len(Username) - 1
    while cek >= 0:
        if login == Username[cek]:
            if Pasword == Password[cek]:
                break
            else:
                cek -= 1
        else:
            cek -= 1
    if cek == -1:
        print(color.r + "Maaf username atau password yang anda masukkan salah")
        print("Harap Tunggu Sebentar lalu coba lagi!" + color.e)
        time.sleep(2)
        os.system("cls")
    elif sebagai[cek] == "Admin":
        print("""
||===========================================||
||         WELCOME TO THE ADMIN MENU         ||
||===========================================||
||       K-POP STORE "STUFF AND ALBUM"       || 
        """)
        time.sleep(3)
        os.system("cls")
        print("""
||===========================================||
||        BEGIN YOUR DAY WITH A SMILE        ||
||===========================================||
||              ENJOY YOUR WORK              || 
        """)
        time.sleep(3)
        os.system("cls")
        menu_admin()
        print(color.y + "||===========================================||")
        print("||               Terimakasih                 ||")
        print("||           Kembali ke menu login           ||")
        print("||===========================================||" + color.e)
        time.sleep(3)
        os.system("cls")
    elif sebagai[cek] == "User":
        print("""
||===========================================||
||          WELCOME TO THE USER MENU         ||
||===========================================||
||       K-POP STORE "STUFF AND ALBUM"       || 
||===========================================||        
        """)
        time.sleep(3)
        os.system("cls")
        print("""
||===========================================||
||        BEGIN YOUR DAY WITH A SMILE        ||
||===========================================||
||            ENJOY YOUR SHOPPING            || 
||===========================================||
        """)
        time.sleep(3)
        os.system("cls")
        menu_user()
        print(color.y + "||===========================================||")
        print("||       Terima kasih telah berbelanja       ||")
        print("||===========================================||")
        print("||           Kembali ke menu login           ||")
        print("||===========================================||" + color.e)
        time.sleep(3)
        os.system("cls")