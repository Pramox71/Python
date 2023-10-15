def loops():
    def Konversi_mata_uang():
        print("Konversi mata uand IDR --> Mata uang asing")
        print("==========================================")
        print ('1. USD')
        print ('2. SGD')
        print ('3. EUR')
        print ('4. JPY')
    def USD():
        IDR = int(input("Masukkan Nominal = Rp."))
        USD = float(IDR/14135.29)
        print("Mata USD = $", USD)
    def SGD():
        IDR = int(input("Masukkan Nominal = Rp."))
        SGD = float(IDR/10529.00)
        print("Mata SGD = $", SGD)
    def EUR():
        IDR = int(input("Masukkan Nominal = Rp."))
        EUR = float(IDR/16486.33)
        print("Mata SGD = €", EUR)
    def JPY():
        IDR = int(input("Masukkan Nominal = Rp."))
        JPY = float(IDR/123.97)
        print("Mata SGD = ¥", JPY)
    Konversi_mata_uang()
    choose = int(input("Pilih mata uang yang diinginkan : "))
    if choose == 1:
        USD()
    elif choose == 2:
        SGD()
    elif choose == 3:
        EUR()
    elif choose == 4:
        JPY()
    else:
        print("Mata Uang tidak teridentifikasi")
    Y = True
    while Y == True:
        x = str(input("Apakah anda ingin mengkorvesi ulang? Yes/No :"))
        if x == "Yes":
            loops()
            Y = False
        elif x == "No":
            print("Selesai")
            Y = True
            break
        else:
            print("Tidak Terdefinisi")
            loops()    
            Y = False  
loops()