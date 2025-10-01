print("""
    |================================|
    |  Login Kalkulator MUltifungsi  |
    |================================|
""")

username = (input("masukkan username anda : "))
password = (input("masukkan password anda : "))

if username == "Attar" and password == "046":
    print("""
    |============================|
    | 1. Konversi Satuan Panjang |
    | 2. Konversi Satuan Massa   |
    | 3. Konversi Satuan Suhu    |
    | 4. Konversi Satuan Waktu   |
    | 5. Konversi Mata Uang      |
    |============================|
    """)

    opsi = int(input("Masukkan nomor : "))

#konversi panjang
    if opsi == 1:
        print("\n<KONVERSI SATUAN PANJANG>")
        
        print("""
    |========================|
    | 1. feet to meter       |
    | 2. kilometer to meter  |
    | 3. centimeter to meter |
    |========================|
    """)

        panjang = int(input("Ingin Konversi Apa? "))

        if panjang == 1:
            feet1 = float(input("\nMasukkan nilai (feet) : "))
            feet2 = feet1 * 0.3048
            print(feet1, "feet", "==>", feet2, "meter")

        elif panjang == 2:
            km1 = float(input("\nMasukkan nilai (km) : "))
            km2 = km1 * 1000
            print(km1, "km", "==>", km2, "meter")

        elif panjang == 3:
            cm1 = float(input("\nMasukkan nilai (cm) : "))
            cm2 = cm1 / 100
            print(cm1, "cm", "==>", cm2, "meter")

        else:
            print("""
            |================|
            | TIDAK ADA OPSI |
            |================|
            """)
            
#konversi massa
    elif opsi == 2:
        print("\n<KONVERSI SATUAN MASSA>")

        print("""
    |=========================|
    | 1. pound to kilogram    |
    | 2. ton to kilogram      |
    | 3. gram to kilogram     |
    | 4. oz to kilogram       |
    | 5. miligram to kilogram |
    |=========================|
    """)
        
        massa = int(input("Ingin Konversi Apa? "))

        if massa == 1:
            pound1 = float(input("\nMasukkan Berat (pound) : "))
            pound2 = pound1 * 0.4535
            print(pound1, "pound", "==>", pound2, "kilogram")

        elif massa == 2:
            ton1 = float(input("\nMasukkan Berat (ton) : "))
            ton2 = ton1 * 1000
            print(ton1, "ton", "==>", ton2, "kilogram")
        
        elif massa == 3:
            gram1 = float(input("\nMasukkan Berat (gram) : "))
            gram2 = gram1 / 1000
            print(gram1, "gram", "==>", gram2, "kilogram")
        
        elif massa == 4:
            oz1 = float(input("\nMasukkan Berat (oz) : "))
            oz2 = oz1 * 0.0283
            print(oz1, "oz", "==>", oz2, "kilogram")
        
        elif massa == 5:
            miligram1 = float(input("\nMasukkan Berat (miligram) : "))
            miligram2 = miligram1 * 0.000001 
            print(miligram1, "miligram", "==>", miligram2, "kilogram")

        else:
            print("""
            |================|
            | TIDAK ADA OPSI |
            |================|
            """)

#konversi suhu
    elif opsi == 3:
        print("\n<KONVERSI SATUAN SUHU>")

        print("""
    |=========================|
    | 1. celcius to kelvin    |
    | 2. fahrenheit to kelvin |
    | 3. reamur to kelvin     |
    |=========================|
    """)
        
        suhu = int(input("Ingin Konversi Apa? "))

        if suhu == 1:
            celcius1 = float(input("\nMasukkan suhu (celcius) : "))
            celcius2 = celcius1 + 273.15
            print(celcius1, "celcius", "==>", celcius2, "kelvin")

        elif suhu == 2:
            fahrenheit1 = float(input("\nMasukkan suhu (fahrenheit) : "))
            fahrenheit2 = (fahrenheit1 + 459.67) * 5/9
            print(fahrenheit1, "fahrenheit", "==>", fahrenheit2, "kelvin")
        
        elif suhu == 3:
            reamur1 = float(input("\nMasukkan suhu (reamur) : "))
            reamur2 = (reamur1 / 0.8) + 273.15
            print(reamur1, "reamur", "==>", reamur2, "kelvin")
        
        else:
            print("""
            |================|
            | TIDAK ADA OPSI |
            |================|
            """)
        
#konversi waktu
    elif opsi == 4:
        print("\n<KONVERSI SATUAN WAKTU>")

        print("""
    |===================|
    | 1. menit to detik |
    | 2. jam to detik   |
    |===================|
    """)
        
        waktu = int(input("Ingin Konversi Apa? "))

        if waktu == 1:
            menit1 = float(input("\nMasukkan Waktu (menit) : "))
            menit2 = menit1 * 60
            print(menit1, "menit", "==>", menit2, "detik")

        elif waktu == 2:
            jam1 = float(input("\nMasukkan Waktu (jam) : "))
            jam2 = jam1 * 3600
            print(jam1, "jam", "==>", jam2, "detik")

        else:
            print("""
            |================|
            | TIDAK ADA OPSI |
            |================|
            """)

#konversi kurs mata uang
    elif opsi == 5:
        print("\n<KONVERSI MATA UANG>")

        print("""
    |==============================|
    | 1. dolar to idr (sebaliknya) |
    | 2. yen to idr (sebaliknya)   |
    | 3. won to idr (sebaliknya)   |
    |==============================|
    """)
        uang = int(input("Ingin Konversi Apa? "))

        if uang == 1:

            print("""
        |=================|
        | 1. dolar to idr |
        | 2. idr to dolar |
        |=================|
            """)
            DolarIdr = int(input("1 atau 2? "))

            if DolarIdr == 1:
                print("\nDolar To Idr")
                dolar1 = float(input("Berapa dolar? "))
                dolar2 = dolar1 * 16600
                print(dolar1, "dolar", "==>", dolar2, "idr")

            elif DolarIdr == 2:
                print("\nIdr To Dolar")
                idr1 = float(input("Berapa idr? "))
                idr2 = idr1 * 0.000060
                print(idr1, "idr", "==>", idr2, "dolar")

            else:
                print("""
            |================|
            | TIDAK ADA OPSI |
            |================|
                """)

        elif uang == 2:

            print("""
        |===============|
        | 1. yen to idr |
        | 2. idr to yen |
        |===============|
            """)
            YenIdr = int(input("1 atau 2? "))

            if YenIdr == 1:
                print("\nYen To Idr")
                yen1 = float(input("Berapa yen? "))
                yen2 = yen1 * 112.81
                print(yen1, "yen", "==>", yen2, "idr")

            elif YenIdr == 2:
                print("\nIdr To Yen")
                idr1 = float(input("Berapa idr? "))
                idr2 = idr1 * 0.0089
                print(idr1, "idr", "==>", idr2, "yen")

            else:
                print("""
            |================|
            | TIDAK ADA OPSI |
            |================|
                """)

        elif uang == 3:

            print("""
        |===============|
        | 1. won to idr |
        | 2. idr to won |
        |===============|
            """)
            WonIdr = int(input("1 atau 2? "))

            if WonIdr == 1:
                print("\nWon To Idr")
                won1 = float(input("Berapa won? "))
                won2 = won1 * 11.89
                print(won1, "won", "==>", won2, "idr")

            elif WonIdr == 2:
                print("\nIdr To Won")
                idr1 = float(input("Berapa idr? "))
                idr2 = idr1 * 0.084
                print(idr1, "idr", "==>", idr2, "won")

            else:
                print("""
            |================|
            | TIDAK ADA OPSI |
            |================|
                """)

        else:
            print("""
        |================|
        | TIDAK ADA OPSI |
        |================|
            """)
        
    else:
        print("""
    |================|
    | TIDAK ADA OPSI |
    |================|
        """)

else:
    print("""
    |===================================|
    | USERNAME ATAU PASSWORD ANDA SALAH |
    |===================================|
        """)