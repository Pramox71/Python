print("masukan elemen matriks dipisahkan dengan spasi")
print("contoh :2 4")
str_arr = input("masukan baris pertama: ").split(' ')
bar1 = [int(num) for num in str_arr]

str_arr = input("masukan baris kedua  : ").split(' ')
bar2 = [int(num) for num in str_arr]
det = (bar1[0] * bar2[1]) - (bar1[1] * bar2[0])


print("""
A = [a , b]
    [c , d])

Rumus dari determinan adalah D = a.d-b.c
""")
print("Nilai determinannya adalah : ",det)
print("\n\n matriks : ")
print("|",bar1,"|")
print("|",bar2,"|")
if det == 0:
    print("Matriks tidak memiliki invers")
else:
	m11 = bar1[0]
	m12 = bar1[1]
	m21 = bar2[0]
	m22 = bar2[1]
	print("\n\n Invers matriks :")
	print("|", round(m11/det,3), round(m21/det,3), "|")
	print("|", round(m12/det,3), round(m22/det,3), "|")
