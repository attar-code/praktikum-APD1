angka = int(input("Masukkan angka : "))

if angka < 0:
    print("angka kecil")
elif angka > 0 and angka < 10:
    print("angka ini dalam range 0 sampai 10")
    if angka == 4:
        print("angka merupakan", angka)
else:
    print("angka besar")